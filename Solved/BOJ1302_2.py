import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    books = dict()
    for _ in range(N):
        book = sys.stdin.readline().split()[0]
        if book in books:
            books[book] += 1
        else:
            books[book] = 1
    max_sold = max(books.values())
    answer = []
    for book, number in books.items():
        if number == max_sold:
            answer.append(book)
    answer.sort()
    print(answer[0])