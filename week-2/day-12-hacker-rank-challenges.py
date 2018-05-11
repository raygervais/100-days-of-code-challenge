# Hacker Rank Challenges - 04
## Challenge: Lists
if __name__ == '__main__':
    N = int(input())
    lst = list()
    
    for _ in range(0, N):
        cmd = input()
        op = cmd.split(' ')[0]
        vals = cmd.split(' ')
        vals.pop(0)
        
        vals = list(map(int, vals))
        
        if op == 'insert':
            lst.insert(vals[0], vals[1])
        elif op == 'append':
            lst.append(vals[0])
        elif op == 'remove':
            lst.remove(vals[0])
        elif op == 'sort':
            lst.sort()
        elif op == 'pop':
            lst.pop(len(lst) -1)
        elif op == 'reverse':
            lst = lst[::-1]
        elif op == 'print':
            print(lst)
                
## Challenge: Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    tuple_list = tuple(int (i) for i in integer_list)
    hash_res = hash(tuple_list)
    print(hash_res)
    
## Challenge: Swap-Case
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
## Challenge: Split and Join
def split_and_join(line):
    _split = line.split(' ')
    return '-'.join(_split)
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
## Challenge: What's Your Name
def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))
  
## Challenge: Mutate String
def mutate_string(string, position, character):
    str = list(string)
    str[position] = character
    return ''.join(str)

## Challenge: Find a String
def count_substring(string, sub_string):
    count = 0
    last_index = 0
    
    for i in range(0, len(string)):
        idx = string.find(sub_string, last_index)
        if idx != -1 and idx != last_index:
            count += 1
            last_index = idx + 1
            
    return count
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
