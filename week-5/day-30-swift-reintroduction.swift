// Hello World
print("Hello, World!")

// Variables and Printing
let apples = 3
let oranges = 5

let appleSummary = "I have \(apples) apples"

// Arrays
var shoppingList = ["iPhone X2", "iMac Pro", "Apple Watch 4", "iPad Pro 12.9"]
var osVersionList = [
    "iOS": "12",
    "macOS": "10.14",
    "watchOS": "4"
]

var leakList = [String]()

// Control Flow
let days = 0...100
for day in days {
    if day % 2 == 0 {
        print("Even")
    } else {
        print("Odd")
    }
}

// Optionals
let nickName: String? = nil
let defaultName = "User"
let greeting = "Good Morning \(nickName ?? defaultName)!"

// Functions and Function Values
func makeIncrementor() -> ((Int) -> Int) {
    func addOne(number: Int) -> Int {
        return 1 + number
    }
    return addOne
}

var increment = makeIncrementor()
var inc = increment(10)

func hasAnyMatches(list: [Int], condition: (Int) -> Bool) -> Bool {
    for item in list {
        if condition(item) {
            return true
        }
    }
    
    return false
}

func lessThanTen(number: Int) -> Bool {
    return number < 10
}

var numbers = [20, 19, 7, 12]
hasAnyMatches(list: numbers, condition: lessThanTen)

// Class

class Shape {
    var numberOfSides = 0
    
    func simpleDescription() -> String {
        return "A shape with \(numberOfSides) sides."
    }
}

var shape = Shape()
shape.numberOfSides = 11
var shapeDesc = shape.simpleDescription()