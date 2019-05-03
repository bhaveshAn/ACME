from word_search import WordSearch


t = int(input("Enter number of Pages / Queries : "))
word_search = WordSearch()
q = 0

for _ in range((t * 2)):

    input_list = input().strip().split()

    if input_list[0] == "P":
        word_search.insert(input_list[1:])
    elif input_list[0] == "Q":
        ans = word_search.search(input_list[1:])
        q += 1
        print("Q{0}:".format(q), end=" ")
        if len(ans) <= 5:
            for i in ans:
                print(i, end=" ")
        else:
            for i in ans[:5]:
                print(i, end=" ")
        print()
