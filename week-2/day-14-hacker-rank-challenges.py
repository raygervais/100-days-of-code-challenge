# Hacker Rank Challenges - 06
## Challenge: String Formatting
def print_formatted(number):
    length = len(bin(number)[2::])
    
    for i in range(1, number + 1):
        _octal = oct(i)[2::]
        _hex = hex(i)[2::].upper()
        _binary = bin(i)[2::]
        
        if length == 1:
            spacer = ' ' * (length + 1)
        else:
            spacer = ' ' * length
        
        final_line = str(i).rjust(length) + ' ' + _octal.rjust(length) + ' ' \
            + _hex.rjust(length) + ' ' + _binary.rjust(length)
        
        print(final_line)
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
## Challenge: Capitalize
def capitalize(string):
    names = string.split(' ')
    fixed_names = list()
    
    for i in names:
        fixed_names.append(i.capitalize())
        
    return ' '.join(fixed_names)
    
if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
    
## Challenge: The Minion Game
def minion_game(string):
    _vowels = 'AEIOU'

    _kevin_score  = 0
    _stuart_score = 0
    
    for i in range(len(string)):
        if string[i] in _vowels:
            _kevin_score += (len(string)-i)
        else:
            _stuart_score += (len(string)-i)

    if _kevin_score > _stuart_score:
        print ("Kevin", _kevin_score)
    elif _kevin_score < _stuart_score:
        print ("Stuart", _stuart_score)
    else:
        print ("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
        
    
