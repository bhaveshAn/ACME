class TrieNode(object):
    def __init__(self, char):

        self.char = char
        self.children = []
        self.word_finished = False
        self.occured = []


class WordSearch(object):
    def __init__(self):
        self.c = 0
        self.root = TrieNode("*")

    def insert(self, word_list):

        self.c += 1
        for word in word_list:
            self.insert_one(word)

    def insert_one(self, word):
        node = self.root

        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        node.word_finished = True
        node.occured.append("p" + str(self.c))

    def search(self, word_list):
        ans = []

        for word in word_list:
            querys = self.search_one(word)
            for q in querys:
                if q not in ans:
                    ans.append(q)
        return ans

    def search_one(self, word):

        node = self.root

        for char in word:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
        return node.occured
