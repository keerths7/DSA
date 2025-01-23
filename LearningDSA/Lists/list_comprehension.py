# list_comprehension helps in creating a new list from existing list

# using general approach

list1 = [1,2,3,4,5]
list2 = []

for i in list1:
    list2.append(i**2)
print(list2)

# using list comprehension

new_list = [i**2 for i in list1]
print(new_list)

# also works with str,list,range,tuple etc.

word = "Python"
listy = [i+"a" for i in word]
print(listy)

# Conditional list comprehension

# Filtering the values:

# printing only even numbers
even_list = [i for i in list1 if i%2 ==0]
print(even_list)

# printing square of the negative numbers
integers = [3,54,-2,4,-23,-34,3,-3,33,-43,-345,9,-66]
squared_negatives = [i ** 2 for i in integers if i < 0]
print(squared_negatives)

# printing only the consonants
def check_consonant(letter):
    vowels = "aeiou"
    if letter.isalpha() and letter.lower() not in vowels:
                return True

sentence = input("Enter any word: ")
vowel_list = [i for i in sentence if check_consonant(i)]
print(vowel_list)

# Transforming values based on a condition:

# printing the positive numbers as-is and negative numbers as "negative numbers"
integers = [3,54,-2,4,-23,-34,3,-3,33,-43,-345,9,-66]
negatives_and_positives = [i if i > 0 else "negative number" for i in integers]
print(negatives_and_positives)

# same solution using function
def neg_pos_finder(i):
    if i > 0:
        return i
    return "negative number"
negatives_and_positives = [neg_pos_finder(i) for i in integers]
print(negatives_and_positives)

