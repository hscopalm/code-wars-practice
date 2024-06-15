"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    pig = ""

    for word in text.split(" "):
        if word.isalnum():
            pig += word[1:] + word[:1] + "ay "
        else:
            pig += word + " "

    return pig[:-1]


print(pig_it("Test string !"))
