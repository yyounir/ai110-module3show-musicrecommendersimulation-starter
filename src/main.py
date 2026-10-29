"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from typing import Dict, List, Tuple

from src.recommender import load_songs, recommend_songs


USER_PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.9,
        "target_tempo_bpm": 125,
        "target_valence": 0.8,
        "target_danceability": 0.85,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.4,
        "target_tempo_bpm": 75,
        "target_valence": 0.6,
        "target_danceability": 0.6,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.95,
        "target_tempo_bpm": 155,
        "target_valence": 0.45,
        "target_danceability": 0.6,
        "likes_acoustic": False,
    },
}

EDGE_CASE_PROFILES = {
    "Conflicting: High Energy, Sad": {
        "favorite_genre": "rock",
        "favorite_mood": "sad",
        "target_energy": 0.9,
        "target_valence": 0.1,
        "target_tempo_bpm": 160,
        "target_danceability": 0.5,
        "likes_acoustic": False,
    },
    "No Preferences (Tie Check)": {
        "favorite_genre": None,
        "favorite_mood": None,
        "target_energy": None,
        "target_valence": None,
        "target_tempo_bpm": None,
        "target_danceability": None,
        "likes_acoustic": None,
    },
    "Boundary Values and Unknown Labels": {
        "favorite_genre": "unknown genre",
        "favorite_mood": "unknown mood",
        "target_energy": 1.0,
        "target_valence": 0.0,
        "target_tempo_bpm": 0,
        "target_danceability": 1.0,
        "likes_acoustic": True,
    },
}


def print_recommendations(
    recommendations: List[Tuple[Dict, float, str]],
) -> None:
    print("\n" + "=" * 48)
    print("TOP RECOMMENDATIONS")
    print("=" * 48)

    if not recommendations:
        print("No recommendations found.")
        return

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']}")
        print(f"   Final score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.split("; "):
            print(f"   - {reason}")


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for profile_name, user_prefs in USER_PROFILES.items():
        print(f"\nProfile: {profile_name}")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(recommendations)

    for profile_name, user_prefs in EDGE_CASE_PROFILES.items():
        print(f"\nEdge-case profile: {profile_name}")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(recommendations)


if __name__ == "__main__":
    main()
