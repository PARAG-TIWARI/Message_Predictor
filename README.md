# Message Predictor

**A machine learning–based SMS spam detection system using TF-IDF and Multinomial Naive Bayes, deployed with Streamlit.** :contentReference[oaicite:1]{index=1}

## 🚀 Project Overview

This project implements a text classification model that predicts whether a given SMS message is **Spam** or **Not Spam (Ham)**. It uses classic Natural Language Processing (NLP) techniques and a Machine Learning model, then provides a simple web interface for real-time predictions.

The model is built using:
- **TF-IDF Vectorization** for converting text messages to numeric features.
- **Multinomial Naive Bayes** classifier for detecting spam messages.
- **Streamlit** for deployment and UI.

## 🧠 How It Works

1. **Text Processing**
   - Convert raw SMS text into lowercase.
   - Remove punctuation and stopwords (optional in preprocessing).
   - Convert text into TF-IDF features.

2. **Model Prediction**
   - A pre-trained Naive Bayes model is used to classify the message.
   - Predictions are shown interactively using Streamlit.

## 📁 Repository Structure

Message_Predictor/
├── app.py # Streamlit app code
├── model.pkl # Pickled trained ML model
├── vectorizer.pkl # Pickled TF-IDF vectorizer
├── requirements.txt # Python dependencies
├── setup.sh # Setup script (if applicable)
├── Procfile # For deployment (Heroku/Streamlit etc.)
└── .gitignore


## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PARAG-TIWARI/Message_Predictor.git
   cd Message_Predictor
Create a Python virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows
Install dependencies:

pip install -r requirements.txt
▶️ Run the App (Locally)
Once installed, start the Streamlit app:

streamlit run app.py
A browser window will open where you can enter any SMS text to classify it as Spam or Not Spam.

📦 Deployment
You can deploy this app to platforms like Streamlit Community Cloud or Heroku using the included Procfile and setup.sh. These files help streamline deployment.

🧪 Model Performance
The Multinomial Naive Bayes model with TF-IDF vectorization is a standard and effective approach for text classification tasks such as SMS spam detection, known for high precision and reasonable accuracy on balanced text datasets. 

🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request with improvements.

📜 License
This project is open source and available under the MIT License.


---

If you want, I can also generate badges (e.g., for license, model accuracy, Python version) or a *Project Demo GIF* section to make it more engaging!
::contentReference[oaicite:3]{index=3}
