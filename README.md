# 🎬 IMDB Sentiment Analysis with NLP, Linear SVC, Flask & Docker

This project analyzes the sentiment of 50,000 movie reviews from the IMDB dataset using natural language processing and machine learning techniques. The final model achieves an F1 score of **~89%** on the test set.

## 📂 Dataset
- Source: [Stanford AI Lab - IMDB Sentiment Dataset](https://ai.stanford.edu/~amaas/data/sentiment/)
- Contains 25,000 positive and 25,000 negative reviews (balanced).
- Reviews are cleaned, preprocessed, and combined into a single DataFrame for ease of use.

## 🧰 Features
- 📦 **Data Handling**: Combines train/test and pos/neg reviews into one DataFrame. Handles duplicate entries and null values.
- 🧹 **Preprocessing**: HTML tag removal, lowercasing, URL stripping. Word splitting via `wordninja` to handle glued words. Lemmatization using `WordNetLemmatizer`. Stopword removal (using NLTK).
- 🧠 **Vectorization**: TF-IDF vectorization of processed text.
- 🔍 **Model Training**: Benchmarked multiple models: Logistic Regression, Naive Bayes, Linear SVC, LightGBM. Selected **Linear SVC** based on F1-score. Performed hyperparameter tuning with `GridSearchCV`.
- 📈 **Evaluation**: Accuracy, Precision, Recall, and F1 metrics. Visualization of performance.
- 💾 **Export**: Saves trained model and TF-IDF vectorizer with `pickle`.

## 🧪 Final Model: Linear SVC
```python
LinearSVC(
    C=1.0,
    loss='squared_hinge',
    max_iter=1000,
    tol=0.0001
)
```

## Test Set Results
| Metric    | Score |
| --------- | ----- |
| Accuracy  | 0.90  |
| Precision | 0.89  |
| Recall    | 0.90  |
| F1 Score  | 0.90  |

![Linear SVC Final Result](https://github.com/izaanz/movie-review-sentiment-analysis-nlp/blob/main/img/Linear%20SVC%20on%20Final%20Test.png)

## 🚀 Deployment
- The trained model is served using Flask.
- The app is containerized with Docker for easy deployment on any server.
- Once deployed, the service can be accessed at http://localhost:8080/predict .
- The API accepts a custom movie review via a POST request and returns whether the sentiment is positive or negative.

## 💾 Files
- nlp.ipynb – Main script for end-to-end data loading, preprocessing, modeling, and evaluation.
- model/model.pkl – Final trained Linear SVC model.
- model/vectorizer.pkl – TF-IDF vectorizer used to transform text data.
- app.py – Flask application for serving the model.
- Dockerfile – Instructions to build the containerized Flask API.
- requirements.txt Containing required libraries
- templates/index.html - Front-end for the Flask app

## 📦 Run Instructions
### 🔧 Train Locally
```bash
pip install -r requirements.txt
```
To access the entire code
```nlp.ipynp
```
🌐 Run Flask App (Local)
```bash
python app.py
```
🐳 Run with Docker
```bash
docker build -t imdb-sentiment-api .
docker run -p 5000:5000 imdb-sentiment-api
```
Requires Python 3.7+ and optionally Docker for deployment.

## ⚡Example Movie Reviews for Testing the Model (Generated with AI)
### Positive Reviews:
"An absolute masterpiece! The acting, direction, and storyline were all top-notch. I was glued to my seat the entire time, and the ending left me in awe. Highly recommend this movie to anyone who loves a good emotional rollercoaster!"

"This movie exceeded my expectations. It had great pacing, well-developed characters, and a plot that kept me engaged throughout. The visuals were stunning, and the soundtrack was perfectly chosen. Definitely worth watching again!"

"I was blown away by this film. The performances were fantastic, the story was engaging, and it had such an emotional depth that it really resonated with me. It's a film that stays with you long after the credits roll."

"One of the best films I've seen in years! It's a perfect blend of action, drama, and heartfelt moments. The director did an amazing job, and the cast was exceptional. I can't recommend it enough!"

"An inspiring and heartwarming movie. It had a perfect balance of humor, drama, and romance. The characters felt real, and the story was incredibly well-written. I walked out of the theater with a big smile on my face!"

### Negative Reviews:
"I honestly don't understand the hype around this movie. The plot was predictable, the acting was mediocre, and I just didn't feel connected to any of the characters. I was bored halfway through and couldn't wait for it to end."

"What a disappointment! The movie had a great premise but failed to deliver on every front. The pacing was slow, the dialogue was cringe-worthy, and the ending was completely unsatisfying. Definitely not worth the watch."

"This was a waste of time. The special effects were terrible, and the acting was flat. The story was unoriginal and felt like it was dragged out. I wouldn't recommend this movie to anyone, even if you're a fan of the genre."

"I don't know why this movie got such good reviews. It was slow, boring, and didn't offer anything new. The plot was clichéd, and the characters were one-dimensional. A huge letdown overall."

"A major disappointment. The movie tried too hard to be serious but ended up being incredibly dull. It lacked excitement, and I didn't care for the characters at all. I wouldn't recommend it, even to hardcore fans of the genre."

## Deployed on Cloud
The app is deployed on the cloud and can be accessed through the following link:

https://movie-review-sentiment-analysis-nlp.onrender.com/

![Cloud Deployment](https://movie-review-sentiment-analysis-nlp.onrender.com/)

## Contributions

Contributions to improve the model, enhance feature sets, or optimize the deployment process are welcome. Please submit a pull request with a clear description of your changes.
