# Most common word

import re
from collections import Counter

def mostCommonWord(paragraph, banned):
    # Clean the paragraph
    words = re.findall(r'\w+', paragraph.lower())  # Extract words only S
    
    # Count word frequencies
    word_count = Counter(words)
    
    #Remove banned words
    for word in banned:
        if word in word_count:
            del word_count[word]
    
    # Return the most common word
    return max(word_count, key=word_count.get)
