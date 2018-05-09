# HackerRank Challenges 02

# Challenge: Loops!
if __name__ == '__main__':
    n = int(input())
    
    for val in range(0, n + 1):
        if val < n:
            print(val * val)

# Challenge: Find The Runner Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    mx = max(arr)

    # Remove Current Max
    res = list(filter(lambda a: a != mx, arr))
    print(max(res))
       
    

