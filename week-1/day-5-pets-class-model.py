# Dog  Class

class Dog:
    breed = ''
    name = ''
    is_good_boy = True
    tricks = []

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        self.tricks = []

    def _add_new_trick(self, trick):
        for t in self.tricks:
            if t == trick:
                return
        
        self.tricks.append(trick)
    
    def _add_new_bag_of_tricks(self, bag_tricks):
        for trick in bag_tricks:
            self._add_new_trick(trick)
        return

    def _remove_old_trick_comparitor(trick, comparitor):
        return trick != comparitor

    def _remove_old_trick(self, trick):
        self.tricks = map(self._remove_old_trick_comparitor, self.tricks)
        return

##########################################################################################
# Main Testing Logic
##########################################################################################
# My First Dog
good_boy = Dog('Beagle', 'Tucker')
good_boy._add_new_bag_of_tricks(['Sleeping', 'Eating', 'Fetching'])
    
print('Meet {}'.format(good_boy.name))

if good_boy.is_good_boy == True:
    print(good_boy.name + ' is a good boy / girl!')

print(good_boy.name + ' can do the following tricks really well:')
    
for trick in good_boy.tricks:
    print(' - ' + trick)

# Get User Input
your_dog_name = input('What is your Dog\'s name? ')
your_dog_breed = input('What is your Dog\'s breed? ')

your_dog = Dog(your_dog_breed, your_dog_name)

print('Meet {}!'.format(your_dog.name))

if your_dog.is_good_boy == True:
    print(your_dog.name + ' is a good boy / girl!')

print('We don\'t know what tricks they can do!')

your_dog_tricks = input('Please enter the tricks your dog can do here, seperated by comma: ')
your_dog_tricks = your_dog_tricks.split(',')

for trick in your_dog_tricks:
    # Reverse String
    trick = trick[::-1]
    
    # Clear Out White Space from User Input
    while trick[len(trick) - 1] == " ":
        trick = trick.strip()
    
    # Reverse Back to Current Order
    trick = trick[::-1]
    while trick[len(trick) - 1] == " ":
        trick = trick.strip()

your_dog._add_new_bag_of_tricks(your_dog_tricks)

for trick in your_dog.tricks:
    print(' - ' + trick)