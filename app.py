from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import wordninja
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    joined = ' '.join(words)
    final = ' '.join(wordninja.split(joined))  
    return final

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get the JSON data from the frontend
    review = data.get('review')
    
    # Vectorize the input review
    review_vectorized = vectorizer.transform([review])
    
    # Predict sentiment (0 or 1)
    sentiment = model.predict(review_vectorized)[0]
    
    return jsonify({'sentiment': 'positive' if sentiment == 1 else 'negative'})

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
