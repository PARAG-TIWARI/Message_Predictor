import os
import pickle
import string

import nltk
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Keep NLTK's user data directory available in local and hosted environments.
nltk.data.path.append(os.path.expanduser("~/.nltk_data"))

ps = PorterStemmer()


@st.cache_resource
def load_nltk_resources():
    """Load reusable NLP resources once per Streamlit process."""
    return set(stopwords.words("english"))


@st.cache_resource
def load_artifacts():
    """Load the trained TF-IDF vectorizer and classifier once per process."""
    with open("vectorizer.pkl", "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)

    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    return vectorizer, model


def transform_text(text, stop_words=None):
    """Apply the same lowercase, token, stopword and stemming steps to a message."""
    stop_words = stop_words if stop_words is not None else load_nltk_resources()
    tokens = nltk.word_tokenize(str(text).lower())

    filtered_words = [
        ps.stem(word)
        for word in tokens
        if word.isalnum() and word not in stop_words and word not in string.punctuation
    ]

    return " ".join(filtered_words)


st.set_page_config(page_title="Message Spam Classifier", page_icon="📩")
st.title("SMS / Message Spam Classifier")
st.write("Enter a message to classify it as spam or ham.")

try:
    vectorizer, model = load_artifacts()
    stop_words = load_nltk_resources()
except (FileNotFoundError, LookupError, pickle.UnpicklingError) as exc:
    st.error(
        "The classifier could not load its model files or NLTK language data. "
        "Follow the repository setup instructions and restart the app."
    )
    st.exception(exc)
    st.stop()

input_sms = st.text_area("Enter the message:", height=150)

if st.button("Predict"):
    if not input_sms.strip():
        st.warning("Please enter a message.")
    else:
        try:
            transformed_sms = transform_text(input_sms, stop_words)
            vectorized_sms = vectorizer.transform([transformed_sms])
            prediction = model.predict(vectorized_sms)[0]

            if prediction == 1:
                st.error("SPAM message detected.")
            else:
                st.success("Not spam (ham).")
        except LookupError:
            st.error(
                "NLTK tokenizer data is missing. Run the setup script to install "
                "the punkt and punkt_tab resources."
            )
