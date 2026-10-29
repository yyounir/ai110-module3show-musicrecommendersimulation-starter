# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **MusicFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

> This model generates recommendations based on the user's preference on genre, mood, energy, danceability, and whether the user likes acoustic or not. It makes assumptions based on what the user likes and aligns that data that is given by the dataset csv file. This is designed for classroom exploration and not a production app for real users, because its a command line server with fixed sample profiles and edge cases.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

> The recommender compares each song with the user's preferences and adds up points
to produce a score. A song earns 3 points for matching the preferred genre and
2 for matching the preferred mood. For energy, valence, danceability, and tempo,
it awards up to 2 points per feature, with closer values to the user's target
earning more points. The normalized features use a 0-to-1 scale, while tempo
uses a 120 BPM scale. If an acoustic preference is provided, acoustic songs earn
up to 1 point when the user likes acoustic music, and less when they do not.
Songs are sorted from highest to lowest total score, and the top requested
number are returned with an explanation of the points earned for each feature.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset

> The app uses a small, static CSV dataset of 17 example songs (data/songs.csv). Each row has an ID, title, artist, genre, mood, and audio-style features: energy, tempo (BPM), valence, danceability, and acousticness. Data was added to narrow the user's interests.
> 
> The dataset captures a few broad preferences—genre, mood, energy, tempo, valence, danceability, and acousticness—but musical taste is much richer. It doesn’t represent things like favorite artists, subgenres, instruments or vocals, lyrics and language, song era, familiarity, or listening context.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

> It works best for clear, feature-based tastes that match the fields in the dataset. For example, someone who likes upbeat, energetic pop gets sensible matches like “Sunrise City” or “Gym Hero”; a chill, acoustic-leaning listener is well represented by the lofi tracks; and an intense rock fan can match with “Storm Runner.”

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

> The energy gap doesn’t inherently favor high-energy users. The scoring is symmetric: energy contributes 4 × max(0, 1 − |target − song|). A low-energy target can score just as well as a high-energy one when a song is close to it.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

> I tested out High Energy pop, Chill Lofi, and Deep Intense Rock, as well as some edge case profiles. It has given me the correct song recommendations and the score helped me fully understand how the mood fits well with the songs that were selected. What surprised me was how well it gave the score based on the interests of the user which is excellent for recommending songs.
> 
> I have tested main.py multiple times and learned that there were several cases where I was recommended Sunrise City from the Chill Lofi profile because based on the data for this profile, the user loves lofi, and a chill mood which matches the recommendation well. 


---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

> - Add richer features and preferences where it includes favorite artists, subgenres, instruments, vocals, language, release era, and listening context
> - Make explanations clearer: Explain the strongest matches in plain language
> - Increase diversity in the results: Avoid filling the top five with very similar songs
> - Handle more complex tactics: Let users provide several favorite songs or describe different listening modes,
> - Learn from feedback where you use likes, skips, saves, and listening history to update recommendations over time, while allowing users to adjust or reset what the model has learned.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

> Something that I have learned from this experience is that I was able to pinpoint the favorite songs that I need recommendation by what my interests were. For example, there were several cases where I was recommended Sunrise City from the Chill Lofi profile because based on the data for this profile, the user loves lofi, and a chill mood which matches the recommendation well. 
