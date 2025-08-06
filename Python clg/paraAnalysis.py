# Input: Two paragraphs
para1 = "Python is a powerful programming language. It is easy to learn and fun to use."
para2 = "Learning a programming language like Python can be fun and rewarding."

# Step 1: Convert to lowercase
para1 = para1.lower()
para2 = para2.lower()

# Step 2: Split into words
words1 = para1.split()
words2 = para2.split()

# Step 3: Remove punctuation manually
punctuations = ".,!?"

cleaned_words1 = []
for word in words1:
    for p in punctuations:
        word = word.replace(p, "")
    if word not in cleaned_words1:
        cleaned_words1.append(word)

cleaned_words2 = []
for word in words2:
    for p in punctuations:
        word = word.replace(p, "")
    if word not in cleaned_words2:
        cleaned_words2.append(word)

# Step 4: Find common words
common_words = []
for word in cleaned_words1:
    if word in cleaned_words2 and word not in common_words:
        common_words.append(word)

# Step 5: Find total unique words from both paragraphs
all_unique_words = []
for word in cleaned_words1 + cleaned_words2:
    if word not in all_unique_words:
        all_unique_words.append(word)

# Output
print("Unique words in paragraph 1:", cleaned_words1)
print("Unique words in paragraph 2:", cleaned_words2)
print("\nCommon words between both paragraphs:", common_words)
print("\nTotal count of unique words in both paragraphs:", len(all_unique_words))
