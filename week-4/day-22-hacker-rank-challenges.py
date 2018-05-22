# HackerRank Challenges 07

## Challenge: Exceptions
if __name__ == '__main__':
    for _ in range(int(input())):
        try:
            first, second = (int (i) for i in input().split(' '))
            result = first // second
            print(result)
        except (ZeroDivisionError, ValueError) as e:
            print('Error Code:', e)

## Challenge: Invalid RegEx
import re

if __name__ == '__main__':
    for _ in range(int(input())):
        ans = True
        try:
            reg = re.compile(input())
        except e:
            ans = False
        
        print(ans)
    
