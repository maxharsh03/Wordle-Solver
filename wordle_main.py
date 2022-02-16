from copy import deepcopy
from word_import import *

# generates most probable word
class Word(object):
    def __init__(self, word_list):
        self.word_list = word_list
        self.letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.total_letters = len(word_list)*5
        self.probability = {}
        self.word_prob = {}
        self.new_word = ""

    # assign each letter an initial probability of 0 
    def reset(self):
        for i in range(len(self.letters)):
            self.probability[self.letters[i]] = 0    

    # based on the occurrence, we reassign the probability to each letter 
    # using P = (desired outcome/all outcomes)
    def assign__letter_probability(self): 
        for i in range(len(self.letters)):
            self.probability[self.letters[i]] /= self.total_letters
            key_list = list(self.probability.keys())
            value_list = list(self.probability.values())
            max_prob = max(value_list)

    def assign_word_probability(self):
        key_list = list(self.word_prob.keys())
        value_list = list(self.word_prob.values())
        max_prob = max(value_list)
        self.new_word = (key_list[value_list.index(max_prob)])
    
    def count(self):
        for i in range(len(self.word_list)):
            for j in range(5):
                self.probability[self.word_list[i][j]] += 1

    def word_probability(self):
        for i in range(len(self.word_list)):
            sum = 0
            repeats = []
            for j in range(5):
                if self.probability[self.word_list[i][j]] not in repeats:
                    sum += self.probability[self.word_list[i][j]]
                    repeats.append(self.probability[self.word_list[i][j]])
            self.word_prob[self.word_list[i]] = sum
        
    def main(self):
        self.reset()
        self.count()
        self.assign__letter_probability()
        self.word_probability()  
        self.assign_word_probability()
        return self.new_word


# algorithm to solve it 
score = 0
list_copy = deepcopy(word_list)
winner = False

def incorrect_letter(i, letter, num):
    for x in range(len(list_copy)-1,-1,-1):  # iterate from end of list        
        #quick test for repeat letters
        var = False
        for j in range(len(list_copy[x])):
            if list_copy[x][j] == letter and scoring_list[j] == 1:
                var = True
        if var:
            if list_copy[x][i] == letter:
                del list_copy[x]
        else: 
            if letter in list_copy[x]:
                del list_copy[x]
            
def misplaced_letter(i, letter, num):
    for x in range(len(list_copy)-1,-1,-1):
        if letter not in list_copy[x] or list_copy[x][i] == letter:
            del list_copy[x]
    
def correct_letter(i, letter, num):
    for x in range(len(list_copy)-1,-1,-1):
        if list_copy[x][i] != letter:
            del list_copy[x]

for i in range(6):
    scoring_list = []
    word = Word(list_copy)
    actual_word = word.main()
    print("Guess:", actual_word)
    print("Enter a 0 for an incorrect letter(gray), 1 for a correct letter(green), and 2 for incorrect placement(yellow): ")
    
    for k in range(5):
        scoring_list.append(int(input()))
    
    if 0 not in scoring_list and 2 not in scoring_list:  # means we guessed the word 1st try
        winner = True
        break
        
    for j in range(len(scoring_list)):
        if scoring_list[j] == 0:
            incorrect_letter(j, actual_word[j], len(list_copy))
        elif scoring_list[j] == 1:
            correct_letter(j, actual_word[j], len(list_copy))
        elif scoring_list[j] == 2: 
            misplaced_letter(j, actual_word[j], len(list_copy))

    scoring_list = []
    print("Number of words left: ", len(list_copy))
    print("All possible words left:", list_copy)

if winner:
    print("You won!")
else: 
    print("You lost!")
