"""
Word Occurrences
Estimate: 30 minutes
Actual:   32 minutes
"""

def count_word_occurrences(text):

    words = text.split()


    word_occurrences = {}


    for word in words:

        word = word.lower()
        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1


    max_word_length = max(len(word) for word in word_occurrences.keys())


    results = []
    for word, count in sorted(word_occurrences.items()):
        results.append((word, count, max_word_length))
    return results


def main():
    user_text = input("Enter a string: ")
    word_occurrences = count_word_occurrences(user_text)

    if word_occurrences:

        for word, count, max_length in word_occurrences:
            print(f"{word:{max_length}} : {count}")
    else:
        print("No words to count.")



main()
