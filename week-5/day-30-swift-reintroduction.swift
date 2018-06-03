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

var leakList =[String]()

// Control Flow
let days = 0..100
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



