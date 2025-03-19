# partition labels

class Solution(object):
    def partitionLabels(self, s):
        last_index = {char: idx for idx, char in enumerate(s)}

        #initializing pointers
        result = []
        start = end = 0

        # iterate through the string
        for idx, char in enumerate(s):
            end = max(end, last_index[char])
            if idx == end:
                result.append(end-start+1)
                start = idx + 1
        return result