# Nested loops, if/else example
# Giraffe language translator 


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print("Giraffe Language Translator")
print(translate(input("Enter a phrase: ")))
