class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dic = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                wordPattern = word[:j] + "*" + word[j+1:]
                dic[wordPattern].append(word)
        visitingWord = set([beginWord])
        que = deque([beginWord])
        result = 1
        while que:
            for i in range(len(que)):
                word = que.popleft()
                if word == endWord:
                    return result
                for j in range(len(word)):
                    wordPattern = word[:j] + "*" + word[j+1:]
                    for dicWord in dic[wordPattern]:
                        if dicWord not in visitingWord:
                            visitingWord.add(dicWord)
                            que.append(dicWord)
            result +=1
        return 0

        

# class Solution:
# 	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		# if endWord not in wordList:
		# 	return 0
		# nei = collections.defaultdict(list)
		# wordList.append(beginWord)
		# for word in wordList:
		# 	for j in range(len(word)):
		# 		pattern = word[:j] + "*" + word[j+1:]
		# 		nei[pattern].append(word)
		# visit = set([beginWord])
		# que = deque([beginWord])
		# res = 1
		# while que:
		# 	for i in range(len(que)):
		# 		word = que.popleft()
		# 		if word == endWord:
		# 			return res
		# 		for j in range(len(word)):
		# 			pattern = word[:j] + "*" + word[j+1:]
		# 			for neiW in nei[pattern]:
		# 					visit.add(neiW)
		# 					que.append(neiW)
		# 	res += 1
		# return 0			
        