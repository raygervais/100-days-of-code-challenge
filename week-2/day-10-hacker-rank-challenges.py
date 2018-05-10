# HackerRank Challenges 03

## Challenge: Finding The Percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    query_sum = sum(float(i) for i in student_marks[query_name])
    query_avg = float(query_sum / len(student_marks[query_name]))
    
    print('{:.2f}'.format(query_avg))
    
## Challenge: Numpy Sum and Prod
import numpy

n, _, m = input()
my_array = list()

for _ in range(0, int(n)):
    l, _, r = input()
    my_array.append([int(l), int(r)])

my_array = numpy.array([my_array])
my_sum = numpy.sum(my_array, axis = 0)
my_prod = numpy.prod(my_array)

print(my_prod)

'''
import numpy

n, _, m = input()
my_array = list()

for _ in range(0, int(n)):
    temp = input()
    my_array.append(map(int (i) for i in temp.split(' '))

my_array = numpy.array([my_array])
my_sum = numpy.sum(my_array, axis = 0)
my_prod = numpy.prod(my_array)

print(my_prod)
'''
