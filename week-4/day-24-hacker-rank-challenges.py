# HackerRank Challenges 08

## Challenge: Divmod
if __name__ == '__main__':
    res = divmod(int(input()), int(input()))
    
    print(res[0])
    print(res[1])
    print(res)
    
# Challege: POW
if __name__ == '__main__':
    a,b,c = (int(input()) for _ in range(3))
    
    print(pow(a, b))
    print(pow(a, b, c))

# Challenge: Integers Come in All Sizes
if __name__ == '__main__':
    
    a,b,c,d = (int(input()) for _ in range(4))
    res = (a**b) + (c**d)
    
    print(res)

# Challenge: Triangle Quest 1
for i in range(1,int(input())):
    # Thank God for Discussion and Insightful Comments 
    print((10**(i)//9)*i)