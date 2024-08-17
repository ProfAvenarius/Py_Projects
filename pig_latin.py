# Description: Transforms any input string into pig latin.
# Author: DCE
# Date: Aug.17, 2024


vowels = ["a", "e", "i", "o", "u"]

GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"  # Closest to orange
RESET = "\033[0m"

while True:
    words_pig = []
    print ("\n\n\n")
    sent_before = input ("Enter a sentence that you want to translate into Pig Latin: \n\n")
    print ("\n\n")
    sent_list = sent_before.split()
    words = len(sent_list)
    n=0
    while n < (words):
        word_eng = sent_list[n].lower()
        word_eng = word_eng.strip(",.!?;:")
        if word_eng[0] in vowels:
            word_pig = word_eng + "way"
        else:
            first_let = word_eng[0]
            word_trim = word_eng[1:]
            word_pig = word_trim + first_let + "ay"
        words_pig.append(word_pig) 
        n += 1

    sent_pig = " ".join(words_pig).capitalize()
    if not sent_pig.endswith('.'):
        sent_pig += '.'
    print ("The Pig Latin translation is:")
    print()
    print (f"{GREEN}{sent_pig}{RESET}")
    print ("\n\n\n")
    choice = input("Would you like to translate another? Hit return to continue or enter 'Q' to quit.").upper()
    if choice == "Q":
        break
print("\n\n\n")
