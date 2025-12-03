import streamlit as st
import nltk
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# ============================
# Load NLTK Dependencies
# ============================
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

# ============================
# Text Preprocessing Function
# ============================
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    filtered_words = []
    for word in text:
        if word.isalnum():
            filtered_words.append(word)

    filtered_words = [
        ps.stem(word)
        for word in filtered_words
        if word not in stopwords.words('english') and word not in string.punctuation
    ]

    return " ".join(filtered_words)

# ============================
# Load Vectorizer and Model
# ============================
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# ============================
# Streamlit UI
# ============================
st.title("📩 SMS / Message Spam Classifier")

input_msg = st.text_area("Enter the message:", height=150)

if st.button("Predict"):
    if input_msg.strip() == "":
        st.warning("Please enter a message before predicting.")
    else:
        # 1. Transform message
        transformed_sms = transform_text(input_msg)

        # 2. Vectorize transformed text
        vectorized_sms = vectorizer.transform([transformed_sms])

        # 3. Predict
        prediction = model.predict(vectorized_sms)[0]

        # 4. Result display
        if prediction == 1:
            st.error("🚨 **SPAM Message Detected!**")
        else:
            st.success("✔️ **This is NOT Spam (HAM).**")
