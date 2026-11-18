# Message Predictor — SMS Spam Classification

Message Predictor is a small NLP and machine-learning application that classifies a user-entered SMS/message as **spam** or **ham**. It uses a TF-IDF vectorizer and a trained classifier exposed through a Streamlit interface.

This is a project demonstration, not a hosted messaging-security product.

## How it works

1. Convert the input text to lowercase and tokenize it with NLTK.
2. Remove non-alphanumeric tokens and English stopwords.
3. Apply Porter stemming.
4. Transform the processed text using the saved TF-IDF vectorizer.
5. Pass the sparse feature vector to the saved classifier.
6. Display the spam/ham prediction.

The trained artifacts are stored in the repository:
- `vectorizer.pkl` — fitted TF-IDF vectorizer.
- `model.pkl` — fitted classifier.

The model is loaded once per Streamlit process using `st.cache_resource`. NLTK stopwords are also cached instead of being reconstructed for every token.

## Technology

- Python
- NLTK (tokenization, stopwords and Porter stemming)
- scikit-learn (TF-IDF and classification artifacts)
- Streamlit

## Run locally

Use the Python version compatible with the saved scikit-learn artifact. The repository does not currently record the exact library versions used to train the pickle files; a matching training environment may be required if loading fails.

~~~bash
git clone https://github.com/PARAG-TIWARI/Message_Predictor.git
cd Message_Predictor

python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
~~~

Download the NLTK data used by the app:

~~~bash
bash setup.sh
~~~

On Windows without Bash, run:

~~~bash
python -m nltk.downloader punkt punkt_tab stopwords
~~~

Start Streamlit:

~~~bash
streamlit run app.py
~~~

Open the local address shown by Streamlit (normally `http://localhost:8501`).

## Deployment status

The repository includes a `Procfile` and a setup script, but it does not provide a current public Streamlit/Heroku deployment URL or a deployment receipt. Treat it as a locally runnable project unless a working hosted URL is added and verified.

## Current limitations

- No dataset source, licence or train/test split description is documented in the repository.
- No committed evaluation report, confusion matrix or per-class precision/recall is available.
- The exact training dependency versions for the pickle artifacts are not recorded.
- No automated tests currently cover text preprocessing or predictions.
- A text classifier can produce false positives/negatives; it should not be treated as a definitive phishing or security filter.

## Recommended next improvements

1. Record the dataset source, licence and data split used to train the model.
2. Add reproducible training code and pin artifact-compatible dependency versions.
3. Publish accuracy, precision, recall, F1 and a confusion matrix from a held-out test set.
4. Add tests for empty messages, punctuation, URLs, numbers and unusual input.
5. Add a live demo only after deployment is configured and its URL has been verified.

## Repository files

~~~text
Message_Predictor/
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── setup.sh
└── Procfile
~~~

[GitHub repository](https://github.com/PARAG-TIWARI/Message_Predictor) · [GitHub profile](https://github.com/PARAG-TIWARI)
