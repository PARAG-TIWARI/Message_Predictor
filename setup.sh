#!/usr/bin/env bash
set -euo pipefail

mkdir -p "$HOME/.streamlit" "$HOME/.nltk_data"

cat > "$HOME/.streamlit/config.toml" <<EOF
[server]
port = ${PORT:-8501}
enableCORS = false
headless = true
EOF

# NLTK 3.8+ may use punkt_tab in addition to punkt for word_tokenize.
python -m nltk.downloader -d "$HOME/.nltk_data" punkt punkt_tab stopwords
