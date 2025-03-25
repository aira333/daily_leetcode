# Concatenated words

# Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

# Note: The number of elements of the given list will not exceed 10^4
# The elements in the given list will contain only lowercase letters.

# Intuition:

'''
We are given an array of strings that consist single 
words and concatenated words. We need to return all the
concatenated words in the array.

We can first put them in a set for faster lookup.

Then pick a word and chec if it can be formed by
concatenating two words from the set, now how do we 
check that?

Ex: catsdogcats
split at each and every letter and check if the
left part is in the set and the right part is in the
set.

c | atsdogcats
ca | tsdogcats
cat | sdogcats - yes # if prefix exists and either suffix exists or suffix can be formed by concatenating two words from the set
cats | dogcats  yes
catsd | ogcats
catsdo | gcats
catsdog | cats - yes
catsdogc | ats
catsdogca | ts 
catsdogcat | s
'''
# Approach:

# Put all the words in a set for faster lookup.
# For each word, temporarily run a loop from 1 to len(word) - 1
# Check if the left part is in the set and the right part is in the set.
# If yes, then add the word to the result.
# Return the result.


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)  #Store words in a set for quick lookup
        memo = {}  # Create a memoization dictionary to store results

        def is_concatenated(word):
            if word in memo:  # If we already checked this word, return the stored result
                return memo[word]

            for i in range(1, len(word)):  #  Try splitting the word at every position
                prefix, suffix = word[:i], word[i:]  # Split into two parts
                
                #Check if prefix is a word AND (suffix is a word OR can be split further)
                if prefix in word_set and (suffix in word_set or is_concatenated(suffix)):
                    memo[word] = True  # Store the result so we don't check again
                    return True  

            memo[word] = False  # If no split works, mark as False
            return False

        result = []  # List to store concatenated words
        for word in words:  #  Check each word in the list
            word_set.remove(word)  #  Temporarily remove the word to avoid using itself
            if is_concatenated(word):  # Check if it can be formed using other words
                result.append(word)  #  If yes, add it to the result list
            word_set.add(word)  # Put the word back in the set

        return result  # Return the list of concatenated words


