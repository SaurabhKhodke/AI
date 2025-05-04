import re
from collections import Counter
from string import ascii_lowercase

# Expanded corpus
corpus_text = """
the of and to in is that it was for you he be with on as I his they at are have 
this not but had by from she or we an there her were will would do been their has 
more if no when what so up out them can who me about some could into its only now 
other new your which time these two may then do down should because each any those
spelling correct university college semester education algorithm implementation
""".lower()

def words(text):
    return re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower())

def create_vocabulary():
    return Counter(words(corpus_text))

def edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in ascii_lowercase]
    inserts = [L + c + R for L, R in splits for c in ascii_lowercase]
    return set(deletes + transposes + replaces + inserts)

def known(words, vocab):
    return set(w for w in words if w in vocab)

def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def spell_check(word, vocab):
    if word in vocab:
        return word
    
    # Try 1-edit candidates first
    candidates = known(edits1(word), vocab)
    if candidates:
        return max(candidates, key=lambda w: vocab[w])
    
    # Then try 2-edit candidates
    candidates = known(edits2(word), vocab)
    if candidates:
        return max(candidates, key=lambda w: vocab[w])
    
    return word

Vocabulary = create_vocabulary()

# Get user input
user_input = input("Enter words separated by space: ").lower()
test_words = user_input.split()

# Check each word
for word in test_words:
    print(f"{word} → {spell_check(word, Vocabulary)}")





