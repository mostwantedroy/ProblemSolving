import sys

if __name__ == "__main__":
    document = sys.stdin.readline()[0:-1]
    words = sys.stdin.readline()[0:-1]
    print(list(document))
    
    length_document = len(document)
    length_words = len(words)
    print(length_document)
    print(length_words)
    count = 0
    i = 0

    while i <= length_document - length_words:  # OR length_document - i >= length_words
        print(document[i:i + length_words], words)
        if document[i:i + length_words] == words:
            count += 1
            i += length_words
        else:
            i += 1

    print(count)