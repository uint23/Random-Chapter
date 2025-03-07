import random
import textwrap

# Load the full WEB Bible text
with open("web.txt", "r", encoding="utf-8") as file:
    lines = [line.rstrip() for line in file.readlines()]

bible = {}
current_book = None
current_chapter = None

# Processing state
current_verse_text = ""
current_verse_number = None

for line in lines:
    if line.startswith("Book ") and len(line.split()) >= 3:
        parts = line.split(maxsplit=2)
        current_book = parts[2].strip()
        bible[current_book] = {}
        current_chapter = None
        continue

    if current_book is None:
        continue  # Skip junk before first book

    if line[:3].isdigit() and ":" in line[:6]:
        if current_verse_number is not None and current_chapter is not None:
            full_verse = f"{current_verse_number}. {current_verse_text.strip()}"
            bible[current_book][current_chapter].append(full_verse)
        
        chapter_verse, verse_text = line.split(" ", 1)
        chapter, verse = chapter_verse.split(":")
        chapter = str(int(chapter))
        verse = str(int(verse))

        if chapter not in bible[current_book]:
            bible[current_book][chapter] = []

        current_chapter = chapter
        current_verse_number = verse
        current_verse_text = verse_text

    else:
        current_verse_text += " " + line.strip()

if current_verse_number is not None and current_chapter is not None:
    bible[current_book][current_chapter].append(f"{current_verse_number}. {current_verse_text.strip()}")

if not bible:
    raise ValueError("No books detected. Please check the file format.")

# Pick a random book and chapter
random_book = random.choice(list(bible.keys()))
random_chapter = random.choice(list(bible[random_book].keys()))
verses = bible[random_book][random_chapter]

# Center helper
def center_text(text, width=90):
    return text.center(width)

# Print header
line_width = 90
print("=" * line_width)
print(center_text(f"📖 {random_book} - Chapter {random_chapter}", line_width))
print("=" * line_width)

# Print verses without gaps, with wrapping for long lines
for verse in verses:
    verse_number, verse_text = verse.split(". ", 1)

    wrapped_lines = textwrap.wrap(verse_text, width=line_width - len(verse_number) - 2)

    if wrapped_lines:
        print(f"{verse_number}. {wrapped_lines[0]}")
        for line in wrapped_lines[1:]:
            print(f"{' ' * (len(verse_number) + 2)}{line}")
    else:
        print(f"{verse_number}. {verse_text}")

print("=" * line_width)
