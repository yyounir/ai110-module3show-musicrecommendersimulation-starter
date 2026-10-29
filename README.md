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

Scoring awards 1.5 points for a genre match and 2 points for a mood match.
Energy earns up to 4 points, while valence, danceability, and tempo each earn
up to 2 points based on closeness to the user's target:
`max_points * max(0, 1 - abs(song_value - target) / scale)`. The scale is 1 for
normalized 0-to-1 features and 120 BPM for tempo, so matching a user's target
scores higher than simply having a high or low feature value. An acoustic
preference adds up to 1 point in proportion to the song's acousticness. This
experimental weighting doubles energy's influence and halves genre's.

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
   Final score: 7.42
   Reasons:
   - Genre match (+1.5 points)
   - Mood match (+2 points)
   - Energy similarity: 3.92/4 points (target 0.8, song 0.82)

2. Rooftop Lights
   Final score: 5.84
   Reasons:
   - Genre mismatch (+0 points)
   - Mood match (+2 points)
   - Energy similarity: 3.84/4 points (target 0.8, song 0.76)

3. Gym Hero
   Final score: 4.98
   Reasons:
   - Genre match (+1.5 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 3.48/4 points (target 0.8, song 0.93)

4. Velvet Weekend
   Final score: 3.96
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 3.96/4 points (target 0.8, song 0.79)

5. Night Drive Loop
   Final score: 3.80
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 3.80/4 points (target 0.8, song 0.75)

```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

### Output for Stress Test
```aiignore
================================================
TOP RECOMMENDATIONS
================================================

1. Sunrise City
   Final score: 13.34
   Reasons:
   - Genre match (+3 points)
   - Mood match (+2 points)
   - Energy similarity: 1.84/2 points (target 0.9, song 0.82)
   - Valence similarity: 1.92/2 points (target 0.8, song 0.84)
   - Danceability similarity: 1.88/2 points (target 0.85, song 0.79)
   - Tempo similarity: 1.88/2 points (target 125, song 118)
   - Acoustic preference similarity: 0.82/1 point

2. Gym Hero
   Final score: 11.65
   Reasons:
   - Genre match (+3 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.94/2 points (target 0.9, song 0.93)
   - Valence similarity: 1.94/2 points (target 0.8, song 0.77)
   - Danceability similarity: 1.94/2 points (target 0.85, song 0.88)
   - Tempo similarity: 1.88/2 points (target 125, song 132)
   - Acoustic preference similarity: 0.95/1 point

3. Rooftop Lights
   Final score: 10.27
   Reasons:
   - Genre mismatch (+0 points)
   - Mood match (+2 points)
   - Energy similarity: 1.72/2 points (target 0.9, song 0.76)
   - Valence similarity: 1.98/2 points (target 0.8, song 0.81)
   - Danceability similarity: 1.94/2 points (target 0.85, song 0.82)
   - Tempo similarity: 1.98/2 points (target 125, song 124)
   - Acoustic preference similarity: 0.65/1 point

4. Velvet Weekend
   Final score: 8.24
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.78/2 points (target 0.9, song 0.79)
   - Valence similarity: 1.92/2 points (target 0.8, song 0.76)
   - Danceability similarity: 1.92/2 points (target 0.85, song 0.89)
   - Tempo similarity: 1.78/2 points (target 125, song 112)
   - Acoustic preference similarity: 0.84/1 point

5. Island Rhythm
   Final score: 7.81
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.64/2 points (target 0.9, song 0.72)
   - Valence similarity: 1.84/2 points (target 0.8, song 0.88)
   - Danceability similarity: 1.92/2 points (target 0.85, song 0.81)
   - Tempo similarity: 1.65/2 points (target 125, song 104)
   - Acoustic preference similarity: 0.76/1 point

Profile: Chill Lofi

================================================
TOP RECOMMENDATIONS
================================================

1. Library Rain
   Final score: 13.67
   Reasons:
   - Genre match (+3 points)
   - Mood match (+2 points)
   - Energy similarity: 1.90/2 points (target 0.4, song 0.35)
   - Valence similarity: 2.00/2 points (target 0.6, song 0.6)
   - Danceability similarity: 1.96/2 points (target 0.6, song 0.58)
   - Tempo similarity: 1.95/2 points (target 75, song 72)
   - Acoustic preference similarity: 0.86/1 point

2. Midnight Coding
   Final score: 13.50
   Reasons:
   - Genre match (+3 points)
   - Mood match (+2 points)
   - Energy similarity: 1.96/2 points (target 0.4, song 0.42)
   - Valence similarity: 1.92/2 points (target 0.6, song 0.56)
   - Danceability similarity: 1.96/2 points (target 0.6, song 0.62)
   - Tempo similarity: 1.95/2 points (target 75, song 78)
   - Acoustic preference similarity: 0.71/1 point

3. Focus Flow
   Final score: 11.68
   Reasons:
   - Genre match (+3 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 2.00/2 points (target 0.4, song 0.4)
   - Valence similarity: 1.98/2 points (target 0.6, song 0.59)
   - Danceability similarity: 2.00/2 points (target 0.6, song 0.6)
   - Tempo similarity: 1.92/2 points (target 75, song 80)
   - Acoustic preference similarity: 0.78/1 point

4. Spacewalk Thoughts
   Final score: 9.95
   Reasons:
   - Genre mismatch (+0 points)
   - Mood match (+2 points)
   - Energy similarity: 1.76/2 points (target 0.4, song 0.28)
   - Valence similarity: 1.90/2 points (target 0.6, song 0.65)
   - Danceability similarity: 1.62/2 points (target 0.6, song 0.41)
   - Tempo similarity: 1.75/2 points (target 75, song 60)
   - Acoustic preference similarity: 0.92/1 point

5. Coffee Shop Stories
   Final score: 8.24
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.94/2 points (target 0.4, song 0.37)
   - Valence similarity: 1.78/2 points (target 0.6, song 0.71)
   - Danceability similarity: 1.88/2 points (target 0.6, song 0.54)
   - Tempo similarity: 1.75/2 points (target 75, song 90)
   - Acoustic preference similarity: 0.89/1 point

Profile: Deep Intense Rock

================================================
TOP RECOMMENDATIONS
================================================

1. Storm Runner
   Final score: 13.59
   Reasons:
   - Genre match (+3 points)
   - Mood match (+2 points)
   - Energy similarity: 1.92/2 points (target 0.95, song 0.91)
   - Valence similarity: 1.94/2 points (target 0.45, song 0.48)
   - Danceability similarity: 1.88/2 points (target 0.6, song 0.66)
   - Tempo similarity: 1.95/2 points (target 155, song 152)
   - Acoustic preference similarity: 0.90/1 point

2. Gym Hero
   Final score: 9.33
   Reasons:
   - Genre mismatch (+0 points)
   - Mood match (+2 points)
   - Energy similarity: 1.96/2 points (target 0.95, song 0.93)
   - Valence similarity: 1.36/2 points (target 0.45, song 0.77)
   - Danceability similarity: 1.44/2 points (target 0.6, song 0.88)
   - Tempo similarity: 1.62/2 points (target 155, song 132)
   - Acoustic preference similarity: 0.95/1 point

3. Thunder Bloom
   Final score: 8.63
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.98/2 points (target 0.95, song 0.96)
   - Valence similarity: 1.94/2 points (target 0.45, song 0.42)
   - Danceability similarity: 1.96/2 points (target 0.6, song 0.58)
   - Tempo similarity: 1.78/2 points (target 155, song 168)
   - Acoustic preference similarity: 0.97/1 point

4. Night Drive Loop
   Final score: 7.29
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.60/2 points (target 0.95, song 0.75)
   - Valence similarity: 1.92/2 points (target 0.45, song 0.49)
   - Danceability similarity: 1.74/2 points (target 0.6, song 0.73)
   - Tempo similarity: 1.25/2 points (target 155, song 110)
   - Acoustic preference similarity: 0.78/1 point

5. Sunrise City
   Final score: 6.78
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.74/2 points (target 0.95, song 0.82)
   - Valence similarity: 1.22/2 points (target 0.45, song 0.84)
   - Danceability similarity: 1.62/2 points (target 0.6, song 0.79)
   - Tempo similarity: 1.38/2 points (target 155, song 118)
   - Acoustic preference similarity: 0.82/1 point

Edge-case profile: Conflicting: High Energy, Sad

================================================
TOP RECOMMENDATIONS
================================================

1. Storm Runner
   Final score: 10.67
   Reasons:
   - Genre match (+3 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.98/2 points (target 0.9, song 0.91)
   - Valence similarity: 1.24/2 points (target 0.1, song 0.48)
   - Danceability similarity: 1.68/2 points (target 0.5, song 0.66)
   - Tempo similarity: 1.87/2 points (target 160, song 152)
   - Acoustic preference similarity: 0.90/1 point

2. Thunder Bloom
   Final score: 7.92
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.88/2 points (target 0.9, song 0.96)
   - Valence similarity: 1.36/2 points (target 0.1, song 0.42)
   - Danceability similarity: 1.84/2 points (target 0.5, song 0.58)
   - Tempo similarity: 1.87/2 points (target 160, song 168)
   - Acoustic preference similarity: 0.97/1 point

3. Night Drive Loop
   Final score: 6.41
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.70/2 points (target 0.9, song 0.75)
   - Valence similarity: 1.22/2 points (target 0.1, song 0.49)
   - Danceability similarity: 1.54/2 points (target 0.5, song 0.73)
   - Tempo similarity: 1.17/2 points (target 160, song 110)
   - Acoustic preference similarity: 0.78/1 point

4. Gym Hero
   Final score: 6.32
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.94/2 points (target 0.9, song 0.93)
   - Valence similarity: 0.66/2 points (target 0.1, song 0.77)
   - Danceability similarity: 1.24/2 points (target 0.5, song 0.88)
   - Tempo similarity: 1.53/2 points (target 160, song 132)
   - Acoustic preference similarity: 0.95/1 point

5. Sunrise City
   Final score: 5.90
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.84/2 points (target 0.9, song 0.82)
   - Valence similarity: 0.52/2 points (target 0.1, song 0.84)
   - Danceability similarity: 1.42/2 points (target 0.5, song 0.79)
   - Tempo similarity: 1.30/2 points (target 160, song 118)
   - Acoustic preference similarity: 0.82/1 point

Edge-case profile: No Preferences (Tie Check)

================================================
TOP RECOMMENDATIONS
================================================

1. Sunrise City
   Final score: 0.00
   Reasons:
   - No comparable preferences were provided.

2. Midnight Coding
   Final score: 0.00
   Reasons:
   - No comparable preferences were provided.

3. Storm Runner
   Final score: 0.00
   Reasons:
   - No comparable preferences were provided.

4. Library Rain
   Final score: 0.00
   Reasons:
   - No comparable preferences were provided.

5. Gym Hero
   Final score: 0.00
   Reasons:
   - No comparable preferences were provided.

Edge-case profile: Boundary Values and Unknown Labels

================================================
TOP RECOMMENDATIONS
================================================

1. Blue Hour Train
   Final score: 4.59
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 0.92/2 points (target 1, song 0.46)
   - Valence similarity: 1.42/2 points (target 0, song 0.29)
   - Danceability similarity: 0.98/2 points (target 1, song 0.49)
   - Tempo similarity: 0.60/2 points (target 0, song 84)
   - Acoustic preference similarity: 0.67/1 point

2. Midnight Coding
   Final score: 4.37
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 0.84/2 points (target 1, song 0.42)
   - Valence similarity: 0.88/2 points (target 0, song 0.56)
   - Danceability similarity: 1.24/2 points (target 1, song 0.62)
   - Tempo similarity: 0.70/2 points (target 0, song 78)
   - Acoustic preference similarity: 0.71/1 point

3. Night Drive Loop
   Final score: 4.37
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.50/2 points (target 1, song 0.75)
   - Valence similarity: 1.02/2 points (target 0, song 0.49)
   - Danceability similarity: 1.46/2 points (target 1, song 0.73)
   - Tempo similarity: 0.17/2 points (target 0, song 110)
   - Acoustic preference similarity: 0.22/1 point

4. Library Rain
   Final score: 4.32
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 0.70/2 points (target 1, song 0.35)
   - Valence similarity: 0.80/2 points (target 0, song 0.6)
   - Danceability similarity: 1.16/2 points (target 1, song 0.58)
   - Tempo similarity: 0.80/2 points (target 0, song 72)
   - Acoustic preference similarity: 0.86/1 point

5. Storm Runner
   Final score: 4.28
   Reasons:
   - Genre mismatch (+0 points)
   - Mood mismatch (+0 points)
   - Energy similarity: 1.82/2 points (target 1, song 0.91)
   - Valence similarity: 1.04/2 points (target 0, song 0.48)
   - Danceability similarity: 1.32/2 points (target 1, song 0.66)
   - Tempo similarity: 0.00/2 points (target 0, song 152)
   - Acoustic preference similarity: 0.10/1 point
```


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
