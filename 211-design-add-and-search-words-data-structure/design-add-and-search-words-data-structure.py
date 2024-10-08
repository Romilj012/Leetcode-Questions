class Node:
    def __init__(self):
        self.children = {}
        self.isComplete = False

class WordDictionary:
    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.isComplete = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            node = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in node.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.isComplete
        return dfs(0,self.root)
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


