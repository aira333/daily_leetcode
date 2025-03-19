# top k frequent words

from collections import Counter
 
def topKFrequent(words, k):
    freq = Counter(words)
    
    sorted_words = sorted(freq.keys(), key=lambda word: (-freq[word], word))
    
    return sorted_words[:k]


# Time complexity: O(nlogn) where n is the number of words

# Space complexity: O(n) for the freq dictionary

# Optimized solution using heap

from collections import Counter
import heapq

def topKFrequent(words, k):
    freq = Counter(words)
    
    heap = [(c_count, word) for word, c_count in freq.items()]
    heapq.heapify(heap)
    
    result = [heapq.heappop(heap)[1] for _ in range(k)]
    
    return result

# Time complexity: O(nlogk) where n is the number of words

# Space complexity: O(n) for the freq dictionary and O(k) for the heap


    
    