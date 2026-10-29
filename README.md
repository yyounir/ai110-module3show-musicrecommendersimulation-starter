# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

> For the given dataset, the most effective features for a simple, content-based recommendator would be: Genre, Mood, Energy, Valence, Dancability, and Tempo. When starting with those features, normalizing the numeri values and giving genre and mood clear weight.
> 
> To calculate the score for a numerical feature like energy is to use the user's preferred value rather than reward high or low values. A scoring rule and ranking rule is required because it tells us how well each song matches the user's preferences.
> 
> ```Song``` stores the ```id```, ```title```, ```artist```, ```genre```, ```mood```, ```energy```, ```tempo_bpm```, ```valence```, ```dancability```, and ```acousticness```.
> 
> ```UserProfile``` stores ```favorite_genre```, ```favorite_mood```, ```target_energy```, and ```likes_acoustic```.

### Plan:
```text
Input: User Preferences
(favorite genre, favorite mood, target energy, acoustic preference, etc.)
                         |
                         v
Process: Evaluate every song from songs.csv
For each song:
  - Compare its attributes with the user's preferences
  - Calculate a match score and collect reasons
                         |
                         v
Rank: Sort songs by score, highest first
                         |
                         v
Output: Top K Recommendations
(song details, score, and explanation)
```

Scoring awards 3 points for a genre match and 2 points for a mood match.
Each numeric preference (energy, valence, danceability, and tempo) earns up to
2 points based on closeness to the user's target:
`2 * max(0, 1 - abs(song_value - target) / scale)`. The scale is 1 for
normalized 0-to-1 features and 120 BPM for tempo, so matching a user's target
scores higher than simply having a high or low feature value. An acoustic
preference adds up to 1 point in proportion to the song's acousticness.

Potential biases to consider:
- **Catalog bias:** The small dataset covers some genres and moods better than others, so those songs have more chances to rank highly.
- **Preference bias:** Strong genre or mood weights can repeatedly favor a narrow set of songs and reduce variety.
- **Feature/proxy bias:** Broad labels such as genre and mood may not capture an individual's taste or the many ways people interpret those labels.
- **Popularity or representation bias:** If the catalog or its features reflect existing popularity or cultural representation gaps, recommendations may reinforce them.

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
================================================
TOP RECOMMENDATIONS
================================================

1. Sunrise City
   Final score: 6.96
   Reasons:
   - Genre match (+3 points)
   - Mood match (+2 points)
   - Energy similarity: 1.96/2 points (target 0.8, song 0.82)

2. Gym Hero
   Final score: 4.74
   Reasons:
   - Genre match (+3 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.74/2 points (target 0.8, song 0.93)

3. Rooftop Lights
   Final score: 3.92
   Reasons:
   - Genre mismatch (+0 points)
   - Mood match (+2 points)
   - Energy similarity: 1.92/2 points (target 0.8, song 0.76)

4. Velvet Weekend
   Final score: 1.98
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.98/2 points (target 0.8, song 0.79)

5. Night Drive Loop
   Final score: 1.90
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.90/2 points (target 0.8, song 0.75)

```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
