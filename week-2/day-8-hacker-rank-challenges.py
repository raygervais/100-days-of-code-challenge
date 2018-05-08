# HackerRank Challenges 01

# Challenge: Hello, World!
if __name__ == '__main__':
    print("Hello, World!")

# Challenge: Python If-Else
if __name__ == '__main__':
    n = int(input('Enter a Number '))
    if n % 2 != 0:
        print('Weird')

    elif n % 2 == 0:
        if n >= 2 and n <= 5:
            print('Not Weird')
        elif n >=6 and n <= 20:
            print('Weird')
        else:
            print('Not Weird')
    else:
        print('Weird')

# Challenge: Arithmetic Operators
if __name__ == '__main__':
    a = int(input('Enter First Number '))
    b = int(input('Enter Second Number '))

    # Calculate Various Arithmetics
    sum = a + b
    difference = a - b
    product = a * b
    
    # Print Results
    print(sum)
    print(difference)
    print(product)

# Challenge: Divsion
if __name__ == '__main__':
    a = int(input('Enter First Number '))
    b = int(input('Enter Second Number '))
    
    int_div = a // b
    float_div = a / b
    
    print(int_div)
    print(float_div)

# Challenge: Write a Function (Leap Year)
def is_leap(year):
    leap = False
    
    def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap
    ''' What I wish I could make work.
    return (year % 4 == 0 and
            year % 100 != 0 and
            year % 400 == 0)
    '''     
if __name__ == '__main__':        
    year = int(input('Enter a Year '))
    print(is_leap(year))
    
# Challenge: Print Function
if __name__ == '__main__':
    n = int(input())
    for num in range(1, n + 1):
        print(num, end = '')


 
