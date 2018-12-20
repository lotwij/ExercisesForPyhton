# Create a translation function where every vowel is turned into a "g"
def translate(phrase):
    translation = "" # "Translation" doesn't really cary any worth
    for letter in phrase:  # a for loop that says: go through the phrase by letter
        if letter in "AEIOUaeiou": #check is any vowels are there
            translation = translation + "g" # if so, replace the vowel by a g
        else:
            translation = translation + letter # and if the letter is not a vowel, just leave the letter
    return translation

print(translate(input("Enter a phrase: "))) # Create a starting phrase for people to enter their phrase to be translated



# Create a translation function where every vowel is turned into a "g"
def translate(phrase):
    translation = "" # "Translation" doesn't really cary any worth
    for letter in phrase:  # a for loop that says: go through the phrase by letter
        if letter.lower() in "aeiou": # NOW we check only lower case vowels
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"  # if so, replace the vowel by a g

        else:
            translation = translation + letter  # and if the letter is not a vowel, just leave the letter
    return translation

print(translate(input("Enter a phrase: "))) # Create a starting phrase for people to enter their phrase to be translated