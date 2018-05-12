# Hacker Rank Challenges - 05
## Challenge: String Validators
def string_comp(string, cmpfct) -> bool:
    for s in string:
        if eval("'" + s + "'." + cmpfct + '()'):
            return True
        
    return False

if __name__ == '__main__':
    s = input()
    
    # Alphanumeric Characters
    if string_comp(s, 'isalnum'):
        print(True)
    else:
        print(False)
    
    # Alphabetical Characters
    if string_comp(s, 'isalpha'):
        print(True)
    else:
        print(False)
        
    # Digit Characters
    if string_comp(s, 'isdigit'):
        print(True)
    else:
        print(False)
    
    # Lowercase Characters
    if string_comp(s, 'islower'):
        print(True)
    else:
        print(False)
    
    # Upercase Characters
    if string_comp(s, 'isupper'):
        print(True)
    else:
        print(False)
        
## Challenge: Text-Alignment
#Replace all ______ with rjust, ljust or center. 

if __name__ == '__main__':
    thickness = int(input()) #This must be an odd number
    c = 'H'

    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))    

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
## Challenge: Text-Wrap
def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

