mkdir -p ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
"> ~/.streamlit/config.toml

# Download NLTK data
mkdir -p ~/.nltk_data
python -m nltk.downloader -d ~/.nltk_data punkt
python -m nltk.downloader -d ~/.nltk_data stopwords
