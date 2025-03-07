import requests
import random

# Replace with your actual ESV API Key (Get one from https://api.esv.org/account/create)
ESV_API_KEY = "4e191e3881aa6afd2db462c2b73c7d57a4a45abc"

# List of Bible books and chapters to pull from (can expand this list if you want)
books_and_chapters = {
    "Proverbs": 31,
    "Psalms": 150,
    "Ecclesiastes": 12,
    "James": 5,
    "Matthew": 28,
    "Romans": 16,
    "Philippians": 4
}

# Randomly select a book and chapter
book = random.choice(list(books_and_chapters.keys()))
chapter = random.randint(1, books_and_chapters[book])
verse = random.randint(1, 30)  # Assuming up to 30 verses per chapter (adjust if needed)

# Build the request URL
url = f"https://api.esv.org/v3/passage/text/?q={book}+{chapter}:{verse}&include-footnotes=false&include-verse-numbers=false"

# Make the request
headers = {"Authorization": f"Token {ESV_API_KEY}"}
response = requests.get(url, headers=headers)

# Handle response
if response.status_code == 200:
    verse_text = response.json()['passages'][0].strip()
    print("=" * 50)
    print(f"📖 {book} {chapter}:{verse}")
    print(f"    \"{verse_text}\"")
    print("=" * 50)
else:
    print("❌ Failed to fetch verse. Check your API key or connection.")
