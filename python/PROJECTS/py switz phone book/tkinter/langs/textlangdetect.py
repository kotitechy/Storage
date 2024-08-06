from langdetect import detect

text = "namasthe anna garu"
language = detect(text)

print("Detected language:", language)
