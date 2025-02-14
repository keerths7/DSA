'''
Write a Python function count_words_frequency(words) that takes a list of words (or a string of words) as input and returns a dictionary with the frequency count of each word. 
'''

# Solution 1- Using dict logic 
# Time complexity: O(n)
# Space complexity: O(1)

def count_words_frequency(words):
    word_dict = {}
    if type(words) == str:
        words = words.split()
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

words = ["car", "cat", "bat", "car", "bat", "goat", "car"]
print(count_words_frequency(words))


# Solution 2- using .get() method
# Time complexity: O(n)
# Space complexity: O(1)
def count_words_frequency_get(words):
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word,0) + 1 
    return word_dict

words = ["car", "cat", "bat", "car", "bat", "goat", "car"]
print(count_words_frequency(words))