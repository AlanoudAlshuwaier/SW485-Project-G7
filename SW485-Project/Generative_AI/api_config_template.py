"""
API Configuration Template

Setup steps:
1. Get a Groq API key from https://console.groq.com
2. Create a .env file in the project root
3. Add: GROQ_API_KEY=your_key_here
4. Make sure .env is in .gitignore

This file documents the required environment variables.
The actual key is loaded from .env at runtime.
"""

import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")