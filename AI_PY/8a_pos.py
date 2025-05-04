import sys

def main():
    # Representing std::vector<std::pair<std::string, std::string>>
    # using a list of lists [word, tag]
    tagged_sentence = [
        ["The", "DT"],
        ["planet", "NN"],
        ["Jupiter", "NNP"],
        ["and", "CC"],
        ["its", "PPS"],
        ["moons", "NNS"],
        ["are", "VBP"],
        ["in", "IN"],
        ["effect", "NN"],
        ["a", "DT"],
        ["minisolar", "JJ"],
        ["system", "NN"],
        [",", ","],
        ["and", "CC"],
        ["Jupiter", "NNP"],
        ["itself", "PRP"],
        ["is", "VBZ"],
        ["often", "RB"],
        ["called", "VBN"],
        ["a", "DT"],
        ["star", "NN"],
        ["that", "IN"],
        ["never", "RB"],
        ["caught", "VBN"],
        ["fire", "NN"],
        [".", "."]
    ]

    try:
        minisolar_idx = -1
        for i, (word, tag) in enumerate(tagged_sentence):
            if word == "minisolar":
                 minisolar_idx = i
                 break
        if minisolar_idx != -1 and minisolar_idx + 1 < len(tagged_sentence):
             # Set the tag of the word after "minisolar" to "??"
             tagged_sentence[minisolar_idx + 1][1] = "??" # This is "system"
             print(f"Testing Rule 1: Changed tag of '{tagged_sentence[minisolar_idx + 1][0]}' to '??' for testing.")
    except IndexError:
         pass # Ignore if index out of bounds

    try:
        that_idx = -1
        caught_idx = -1
        for i, (word, tag) in enumerate(tagged_sentence):
            if word == "that":
                that_idx = i
            if word == "caught":
                caught_idx = i
        if that_idx != -1 and caught_idx != -1 and caught_idx == that_idx + 2:
            # Found the pattern, set the middle word's tag to "???"
             tagged_sentence[that_idx + 1][1] = "???" # This is "never"
             print(f"Testing Rule 3: Changed tag of '{tagged_sentence[that_idx + 1][0]}' to '???' for testing.")
    except IndexError:
        pass # Ignore if index out of bounds


    # Representing TagRule struct and rule vectors using lists of dictionaries
    # Each dictionary represents a rule
    two_letter_rules = [
        {"prevTag": "JJ", "nextTag": "", "resultTag": "NN"},

        {"prevTag": "DT", "nextTag": "", "resultTag": "JJ"},
        {"prevTag": "CC", "nextTag": "", "resultTag": "JJ"}
    ]

    three_letter_rules = [
        {"prevTag": "VBP", "nextTag": "NN", "resultTag": "NNP"},
        {"prevTag": "IN", "nextTag": "NN", "resultTag": "NNP"},
        {"prevTag": "IN", "nextTag": "VBN", "resultTag": "PPS"}
    ]

    # Fill in missing tags - Loop through the tagged sentence
    for i in range(len(tagged_sentence)):
        # Check for "???" tags first, as they have more specific rules (context of 2 neighbors)
        if tagged_sentence[i][1] == "???":
            # Apply three-letter rules (require previous and next tag)
            for rule in three_letter_rules:
                # Check boundaries for previous and next elements
                if i > 0 and i < len(tagged_sentence) - 1:
                    prev_tag = tagged_sentence[i - 1][1]
                    next_tag = tagged_sentence[i + 1][1]

                    if prev_tag == rule["prevTag"] and next_tag == rule["nextTag"]:
                        tagged_sentence[i][1] = rule["resultTag"]
                        break # Apply the first matching rule and move to the next token

        # Check for "??" tags
        elif tagged_sentence[i][1] == "??":
             # Apply two-letter rules (mostly require only previous tag based on C++ rules)
             for rule in two_letter_rules:
                 # Check boundary for previous element
                 if i > 0:
                     prev_tag = tagged_sentence[i - 1][1]
                     if prev_tag == rule["prevTag"]:
                         tagged_sentence[i][1] = rule["resultTag"]
                         break # Apply the first matching rule and move to the next token


    # Print out the tagged sentence with filled-in missing tags
    print("\nProcessed Tagged Sentence (Word/TAG):")
    for token in tagged_sentence:
        # Use sys.stdout.write for output similar to std::cout without spaces/newlines
        sys.stdout.write(token[0] + "/" + token[1] + " ")

    print() # Print a final newline


if __name__ == "__main__":
    main()