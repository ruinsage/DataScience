from itertools import product
from itertools import permutations
from itertools import combinations
from operator import itemgetter

students = {
    'jane, 22, C': 3,
    'dave, 32, A': 1,
    'sally, 17, B': 2
}
print(students.items())
print(sorted(students.items(), key=itemgetter(1)))




