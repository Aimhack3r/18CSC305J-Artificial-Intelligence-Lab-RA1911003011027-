import itertools
import pdb
def get_val(word, substitution):
    s = 0
    factor = 1
    for let in reversed(word):
        s += factor * substitution[let]
        factor *= 10
    return s
def solve(equation):
    l, r = equation.lower().replace(' ', '').split('=')
    print(l,r)
    l = l.split('+')
    print(l)
    lets = set(r)
    print(lets)
    for word in l:
        for let in word:
            lets.add(let)
    lets = list(lets)
    print(lets)
    digits = range(20)
    for perm in itertools.permutations(digits, len(lets)):
        sol = dict(zip(lets, perm))
 
        if sum(get_val(word, sol) for word in l) == get_val(r, sol):
            print(' + '.join(str(get_val(word, sol)) for word in l) + " = ",get_val(r, sol))
            
            
equation = input("ENTER EQUATION:")
solve(equation)
