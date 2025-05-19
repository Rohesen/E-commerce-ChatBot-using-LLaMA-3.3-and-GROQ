import streamlit
import pandas as pd
import dotenv
import chromadb
import sentence_transformers

try:
    import groq
except ImportError:
    groq = None

try:
    import semantic_router
except ImportError:
    semantic_router = None

import sqlite3
import sys

print("Python version:", sys.version)
print("streamlit version:", streamlit.__version__)
print("pandas version:", pd.__version__)
print("sqlite3 version:", sqlite3.version)
print("python-dotenv version:", dotenv.__version__)
print("chromadb version:", chromadb.__version__)
print("sentence_transformers version:", sentence_transformers.__version__)
print("groq version:", getattr(groq, '__version__', 'Not Installed'))
print("semantic-router version:", getattr(semantic_router, '__version__', 'Not Installed'))
