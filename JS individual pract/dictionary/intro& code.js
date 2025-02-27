there no JS biult in dictionary as python has.
but we can use objects to achieve similar functionality.
in JS objectsa are collection of key-value pairs, making them quite similar to dictionaries.

// Creating a dictionary-like object
const dictionary = {
    "apple": "A fruit that is red or green",
    "banana": "A yellow fruit that monkeys love",
    "cat": "A small domesticated carnivorous mammal"
};

// Accessing values
console.log(dictionary["apple"]);  // Output: A fruit that is red or green
console.log(dictionary["banana"]); // Output: A yellow fruit that monkeys love

// Adding new key-value pairs
dictionary["dog"] = "A domesticated carnivorous mammal that barks";
console.log(dictionary["dog"]);    // Output: A domesticated carnivorous mammal that barks

// Removing key-value pairs
delete dictionary["cat"];
console.log(dictionary["cat"]);    // Output: undefined

