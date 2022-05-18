symbols = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": ".-", "h": "....", "i": "..",
    "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
}

# Taking input from a user
data = input("Enter text: ")

length = len(data)

# Convert to Morse code in list comprehension
output = [symbols.get(data[i]) for i in range(length) if data[i] in symbols.keys()]

print(' '.join(output))