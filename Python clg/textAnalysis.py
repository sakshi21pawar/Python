text = input("Enter your text: ")
total_char = len(text)

space_count = 0
for char in text:
    if char == ' ':
        space_count += 1

# Frequency of words
words = text.split()
word_freq = {}

for word in words:
    word = word.lower()
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1  

print("\n--- Text Analysis ---")
print("Total characters:", total_char)
print("Total spaces:", space_count)
print("Word frequencies:")
for word, freq in word_freq.items():
    print(f"  {word}: {freq}")
