class Solution:
    def replaceWords(self, d: List[str], sentence: str) -> str:
        sentence = sentence.split()
        d = set(d)
        for i in range(len(sentence)):
            for j in range(1, len(sentence[i])):
                if sentence[i][:j] in d:
                    sentence[i] = sentence[i][:j]
                    break
        return " ".join(sentence)
