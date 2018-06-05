// Swift Functions

// Submodule: Defining and Calling Functions
func showMessage(name: String) {
    print("The function call worked \(name)!")
}

showMessage(name: "Ray")

// Submodule: Returning Values

func getSwiftVersion() -> Float {
    return 4.1
}

func getLanguageName() -> String {
    return "Swift"
}

print("""
Current Language and Version:
    \(getLanguageName()) => \(getSwiftVersion())
""")

// Submodule: Correctly Ignoring Return Values
func noValueReturned () {
    let _ = 1
    let _ = "A"
    let _ = "#iOS13BetterHaveDarkTheme"
    return
}

noValueReturned()

// Submodule: Naming Functions in Swift
func show(message: String) {
    print("The provided message is: '\(message)'")   
}

show(message: "Here we go again!")

// Swift Data Types
// Submodule: Using Enumerations

enum MediaType: String {
    case book = "Paper Adventure"
    case movie = "Explosion Fest"
    case music = "Rock Show"
    case game = "Social Destractor"
}

var itemName: String = "Eragon"
var itemId: Int = 123
var itemType = MediaType.book

print("I've been looking into the \(itemType.rawValue): \(itemName)")
