
'''class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        target = {}
        word_length = len(words[0])
        window = word_length * len(words)

        for word in words:
            target[word] = target.get(word, 0) + 1

        p1, p2 = 0, window
        result = []

        for _ in range(len(s) - window + 1):
            check = {}

            if s[p1:p1+word_length] not in target:
                p1 += 1
                p2 += 1
                continue

            temp = s[p1:p2]
            temp = [
                temp[i:i+word_length]
                for i in range(0, window, word_length)
            ]

            for item in temp:
                if item not in target:
                    break

                check[item] = check.get(item, 0) + 1

                if check[item] > target[item]:
                    break

            if check == target:
                result.append(p1)

            p1 += 1
            p2 += 1

        return result'''


from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        k = len(words)
        target = Counter(words)
        result = []

        for offset in range(word_length):
            left = offset
            seen = {}
            count = 0

            for right in range(offset, len(s) - word_length + 1, word_length):
                word = s[right:right + word_length]

                if word not in target:
                    seen = {}
                    count = 0
                    left = right + word_length
                    continue

                seen[word] = seen.get(word, 0) + 1
                count += 1

                # Too many copies of this word
                while seen[word] > target[word]:
                    left_word = s[left:left + word_length]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_length

                # Found a complete concatenation
                if count == k:
                    result.append(left)

                    # Remove leftmost word to keep sliding
                    left_word = s[left:left + word_length]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_length

        return result

