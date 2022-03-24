"""
Created on Thu Mar 24 12:05:41 2022

@author: Administrator
"""

import itertools as it

numbers = list(range(10))

def getVal(word,sol):
    s = 0
    for letter in word:
        s = s*10 + sol[letter]
    return s

def solve(word):
    # split it into lhs ad rhs
    lhs, rhs = word.split('=')
    # split lhs into two parts
    l1, l2 = lhs.split('+')
    # create the list of used letters
    letters=set()
    letters.update(l1)
    letters.update(l2)
    letters.update(rhs)
    for perm in it.permutations(numbers,len(letters)):
        sol = dict(zip(letters,perm))
        if(sum(getVal(word,sol) for word in (l1,l2)) == getVal(rhs,sol)):
            print(str(getVal(l1,sol)),'+',str(getVal(l2,sol)),'=',str(getVal(rhs,sol)))
   
word = 'SEND+MORE=MONEY'
solve(word)
