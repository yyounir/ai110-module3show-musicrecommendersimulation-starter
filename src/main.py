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

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)
    print_recommendations(recommendations)


if __name__ == "__main__":
    main()
