mkdir -p ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
"> ~/.streamlit/config.toml

# Download nltk models
python -m nltk.downloader -d ~/.nltk_data punkt stopwords
