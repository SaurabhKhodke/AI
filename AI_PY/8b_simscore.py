import math
from collections import Counter

# Documents (lowercased and tokenized)
d = [
    'An apple a day keeps the doctor away'.lower().split(),
    'Never compare an apple to an orange'.lower().split(),
    'I prefer scikit-learn to orange'.lower().split()
]
compDoc = "I'd like an apple and a doctor".lower().split()

# Get all unique terms
terms = set()
for doc in d + [compDoc]:
    terms.update(doc)

# Compute TF (term frequency) for all docs
tf = []
for doc in d + [compDoc]:
    word_counts = Counter(doc)
    tf.append({word: count/len(doc) for word, count in word_counts.items()})

# Compute IDF (inverse document frequency)
idf = {}
for term in terms:
    doc_count = sum(1 for doc in d if term in doc)
    idf[term] = 1 + math.log((len(d) + 1) / (doc_count + 1))  # Smoothed

# Compute TF-IDF vectors
tfidf_vectors = []
for doc_tf in tf:
    vec = [doc_tf.get(term, 0) * idf.get(term, 0) for term in terms]
    tfidf_vectors.append(vec)

# Calculate cosine similarities between compDoc (last vec) and others
def cosine_sim(vec1, vec2):
    dot = sum(a*b for a,b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a*a for a in vec1))
    norm2 = math.sqrt(sum(a*a for a in vec2))
    return dot / (norm1 * norm2) if norm1 * norm2 != 0 else 0

similarities = [cosine_sim(tfidf_vectors[-1], vec) for vec in tfidf_vectors[:-1]]

print("Cosine Similarities:", similarities)
print(f"Most similar document: {similarities.index(max(similarities)) + 1}")