# Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not.
import random
import functools
import requests
from bs4 import BeautifulSoup
import math
import string


def is_fibonacci(n: int) -> bool:
    '''
    returns True if n is a fibonacci number
    '''
    return any(list(map(lambda x: int(math.sqrt(x))**2 == x, [5*n*n + 4, 5*n*n - 4])))


# Using list comprehension (and zip/lambda/etc if required) write an expression that: PTS:100
#     add 2 iterables a and b such that a is even and b is odd
def add_even_odd(list1: list, list2: list) -> list:
    '''
    Adds the even numbers from list1 to the odd numbers from list2
    '''
    return [a+b for a in filter(lambda x: x % 2 + 1, list1) for b in filter(lambda x: x % 2 - 1, list2)]

#     strips every vowel from a string provided (tsai>>t s)


def strip_vowel(string):
    '''
    strips every vowel from a string provided 
    eg: (tsai>>t s)
    '''
    return [s for s in string if s not in ('a', 'e', 'i', 'o', 'u')]

#     acts like a ReLU function for a 1D array


def relu(arr: list) -> float:
    '''
    returns the relu func value for each element in the array
    '''
    return [max(0, x) for x in arr]

#     acts like a sigmoid function for a 1D array


def sigmoid(arr: list) -> float:
    '''
    acts like a sigmoid function for a 1D array
    '''
    return [1 / (1 + math.exp(-x)) for x in arr]
# a-z: 97-122

#     takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn


def shift_char(str: str, shift: int) -> str:
    return "".join([chr((ord(s) - ord('a') + shift) % 26 + ord('a')) for s in str.lower()])


# A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt PTS:200 (Links to an external site.)
def get_google_profanity_words():
    url = "https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    profanity_words = []
    for word in soup.find_all(
            "td", class_="blob-code blob-code-inner js-file-line"):
        word = str(word)
        profanity_words.append(
            word[word.index(">")+1:word.index("/")-1].strip())
    return profanity_words


def check_swear_words(text):
    profanity_words = get_google_profanity_words()
    text = text.replace(".", "")
    text = text.split()
    return any([True for x in text if x in profanity_words]), [x for x in text if x in profanity_words]


# Using reduce function: PTS:100
#     add only even numbers in a list


def add_even(input: list) -> any:
    return functools.reduce(lambda x, y: x+y, [x for x in input if x % 2 == 0], 0)


#     find the biggest character in a string (printable ascii characters)
def max_char(strs: str) -> chr:
    return functools.reduce(lambda a, b: a if a > b else b, strs)

#     adds every 3rd number in a list


def add_3rd_element(input: list) -> any:
    return functools.reduce(lambda x, y: x+y, [x for i, x in enumerate(input) if (i+1) % 3 == 0])


# Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates,
# where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 PTS:100
def random_license_number_1() -> list:
    return ["KA"+str(random.randint(10, 100))+random.choice(string.ascii_uppercase) +
            random.choice(string.ascii_uppercase) + str(random.randint(1000, 10000)) for _ in range(15)]


print(random_license_number_1())

# Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided.


def random_license_number_2(start: int, end: int) -> list:
    return [random.choice(["KA", "DL"])+str(random.randint(10, 100))+random.choice(string.ascii_uppercase) +
            random.choice(string.ascii_uppercase) + str(random.randint(start, end)) for _ in range(15)]


print(random_license_number_2(10, 100))

# Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided PTS:10


def random_license_number_3(st_c: str, numbers: int) -> str:
    return st_c + str(random.randint(10, 100))+random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(numbers)


def partial_fun(fn, st_c: str) -> str:
    return functools.partial(fn, st_c=(st_c), numbers=9999)
