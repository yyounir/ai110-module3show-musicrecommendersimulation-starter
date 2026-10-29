import csv
import math
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass

DEFAULT_USER_PROFILE: Dict[str, object] = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.8,
    "likes_acoustic": False,
    "target_tempo_bpm": 120,
    "target_valence": 0.8,
    "target_danceability": 0.75,
}


def _finite_number(value: object, label: str) -> float:
    """Validate and convert a feature value to a finite number."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be numeric")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{label} must be finite")
    return number


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs ranked by preference score."""
        ranked_songs = sorted(
            self.songs,
            key=lambda song: score_song(vars(user), vars(song))[0],
            reverse=True,
        )
        return ranked_songs[:max(k, 0)]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain how a song matches the user's preferences."""
        _, reasons = score_song(vars(user), vars(song))
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    csv_file_path = Path(csv_path)
    if not csv_file_path.is_absolute() and not csv_file_path.exists():
        project_root_path = Path(__file__).resolve().parent.parent / csv_file_path
        if project_root_path.exists():
            csv_file_path = project_root_path

    with csv_file_path.open(newline="", encoding="utf-8") as csv_file:
        songs = []
        for row in csv.DictReader(csv_file):
            row["id"] = int(row["id"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            for field in ("energy", "valence", "danceability", "acousticness"):
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a song's preference score and human-readable reasons."""
    score = 0.0
    reasons: List[str] = []

    for preference_keys, song_key, label, points in (
        (("favorite_genre", "genre"), "genre", "Genre", 3.0),
        (("favorite_mood", "mood"), "mood", "Mood", 2.0),
    ):
        preference = next(
            (user_prefs[key] for key in preference_keys
             if user_prefs.get(key) is not None),
            None,
        )
        song_value = song.get(song_key)
        if preference is None or song_value is None:
            continue
        if not isinstance(preference, str) or not isinstance(song_value, str):
            raise TypeError(f"{label} preferences and song values must be strings")
        if preference.strip().casefold() == song_value.strip().casefold():
            score += points
            reasons.append(f"{label} match (+{points:g} points)")
        else:
            reasons.append(f"{label} mismatch (+0 points)")

    numeric_features = (
        (("target_energy", "energy"), "energy", "Energy", 1.0),
        (("target_valence", "valence"), "valence", "Valence", 1.0),
        (("target_danceability", "danceability"), "danceability", "Danceability", 1.0),
        (("target_tempo_bpm", "tempo_bpm"), "tempo_bpm", "Tempo", 120.0),
    )
    for preference_keys, song_key, label, distance_scale in numeric_features:
        target = next(
            (user_prefs[key] for key in preference_keys
             if user_prefs.get(key) is not None),
            None,
        )
        value = song.get(song_key)
        if target is None or value is None:
            continue

        target_value = _finite_number(target, label)
        song_value = _finite_number(value, label)
        if distance_scale == 1.0 and not (
            0.0 <= target_value <= 1.0 and 0.0 <= song_value <= 1.0
        ):
            raise ValueError(f"{label} target and song value must be between 0 and 1")
        if distance_scale != 1.0 and (target_value < 0 or song_value < 0):
            raise ValueError(f"{label} target and song value must be non-negative")

        feature_points = 2.0 * max(
            0.0, 1.0 - abs(target_value - song_value) / distance_scale
        )
        score += feature_points
        reasons.append(
            f"{label} similarity: {feature_points:.2f}/2 points "
            f"(target {target_value:g}, song {song_value:g})"
        )

    likes_acoustic = user_prefs.get("likes_acoustic")
    acousticness = song.get("acousticness")
    if likes_acoustic is not None and acousticness is not None:
        if not isinstance(likes_acoustic, bool):
            raise TypeError("likes_acoustic preference must be a boolean")
        acoustic_value = _finite_number(acousticness, "Acousticness")
        if not 0.0 <= acoustic_value <= 1.0:
            raise ValueError("Song acousticness must be between 0 and 1")
        acoustic_points = float(
            acoustic_value if likes_acoustic else 1.0 - acoustic_value
        )
        score += acoustic_points
        reasons.append(
            f"Acoustic preference similarity: {acoustic_points:.2f}/1 point"
        )

    if not reasons:
        reasons.append("No comparable preferences were provided.")
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs with scores and explanations."""
    ranked_songs = sorted(
        ((song, *score_song(user_prefs, song)) for song in songs),
        key=lambda recommendation: recommendation[1],
        reverse=True,
    )
    return [
        (song, score, "; ".join(reasons))
        for song, score, reasons in ranked_songs[:max(k, 0)]
    ]
