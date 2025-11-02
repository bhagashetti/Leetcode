class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels_count = [0] *n
        for i in range(n):
            if i==0:
                temp = len(words[i])
                if words[i][0] in "aeiou" and words[i][temp-1] in "aeiou":
                    vowels_count[i] = 1
            else:
                temp = len(words[i])
                if words[i][0] in "aeiou" and words[i][temp-1] in "aeiou":
                    vowels_count[i] = vowels_count[i-1] +1
                else:
                    vowels_count[i] = vowels_count[i-1]

        l = len(queries)
        output = []
        for i in range(l):
            i1 = queries[i][0]
            i2 = queries[i][1]
            if i1 == 0:
                output.append(vowels_count[i2])
            elif i1 > 0:
                output.append(vowels_count[i2]-vowels_count[i1-1])
        return output




