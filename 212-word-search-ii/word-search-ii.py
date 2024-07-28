class Node:
    def __init__(self):
        self.children = {}
        self.isComplete = False

            
    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.isComplete = True
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for char in words:
            root.insert(char)
        ROWS,COLS = len(board), len(board[0])
        res, visit = set(), set()
        def dfs(r,c,node,word):
            if(r<0 or c<0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] not in node.children):
                return 

            visit.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.isComplete:
                res.add(word)
            
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            visit.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        return list(res)

