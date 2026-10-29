import pytest

from src.recommender import (
    Song,
    UserProfile,
    Recommender,
    recommend_songs,
    score_song,
)
from src.main import print_recommendations

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_score_song_returns_weighted_score_and_explanations():
    score, reasons = score_song(
        {"genre": "pop", "mood": "happy", "energy": 0.8},
        {"genre": "pop", "mood": "happy", "energy": 0.6},
    )

    assert score == pytest.approx(6.6)
    assert isinstance(reasons, list)
    assert any("Genre match (+3 points)" in reason for reason in reasons)
    assert any("Mood match (+2 points)" in reason for reason in reasons)
    assert any("Energy similarity: 1.60/2 points" in reason for reason in reasons)


def test_recommend_songs_returns_top_k_sorted_by_score():
    songs = [
        {"title": "Lower", "genre": "lofi", "mood": "chill", "energy": 0.4},
        {"title": "Higher", "genre": "pop", "mood": "happy", "energy": 0.8},
        {"title": "Middle", "genre": "pop", "mood": "chill", "energy": 0.6},
    ]

    results = recommend_songs(
        {"genre": "pop", "mood": "happy", "energy": 0.8},
        songs,
        k=2,
    )

    assert [song["title"] for song, _, _ in results] == ["Higher", "Middle"]
    assert results[0][1] > results[1][1]
    assert all(explanation for _, _, explanation in results)


def test_print_recommendations_formats_score_and_each_reason(capsys):
    print_recommendations([
        (
            {"title": "Test Track"},
            6.6,
            "Genre match (+3 points); Energy similarity: 1.60/2 points",
        )
    ])

    output = capsys.readouterr().out
    assert "1. Test Track" in output
    assert "Final score: 6.60" in output
    assert "   - Genre match (+3 points)" in output
    assert "   - Energy similarity: 1.60/2 points" in output
