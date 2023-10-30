import random

def randomWord():
    words = open('Hangmanwords.txt').read().splitlines()
    return random.choice(words).lower()

def createHiddenWord(word):
    hiddenWord = []
    for i in range(0,len(word)) :
        hiddenWord.append("-")
    return hiddenWord

def printHiddenWord(hiddenWord):
    out_str = " "
    print(out_str.join(hiddenWord))

def updateHiddenWord(hiddenWord, word, letter):
    for i in range(0,len(word)) :
        if letter == word[i]:
            hiddenWord[i] = letter
    return hiddenWord

def displayHangman(tries):
    stages = [  
                """
                --------
                |      |
                |      O
                |      |
                |     /|\\
                |     / \\
                -
                """,
                """
                --------
                |      |
                |      O
                |      |
                |     /|\\
                |     / 
                -
                """,
                """"
                --------
                |      |
                |      O
                |      |
                |     /|\\
                |      
                -
                """,
                """"
                --------
                |      |
                |      O
                |      |
                |     /|
                |     
                -
                """,
                """
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
                """,
                """
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
                """,
                """
                --------
                |      |
                |      
                |    
                |      
                |     
                -
                """
    ]
    print("tries left = ", tries)
    return stages[tries]

word = randomWord()

hiddenWord = createHiddenWord(word)
printHiddenWord(hiddenWord)

corr = False
tries = 6
while tries > 0 :
    userIn = input("Enter a guess letter or the full word ? : ").lower()

    if len(userIn) == 1: 
        if userIn not in word:
            tries = tries - 1
            hiddenWordStr = "".join(hiddenWord)
        else :
            hiddenWord = updateHiddenWord(hiddenWord, word, userIn)
            hiddenWordStr = "".join(hiddenWord)
    else : 
        if (userIn != word): 
            tries = tries - 1
            hiddenWordStr = "".join(hiddenWord)
        else : 
            hiddenWordStr = word

    if hiddenWordStr == word :
        corr = True
        break
    else :
        print(displayHangman(tries))
        printHiddenWord(hiddenWord)

if (corr) :
    print("Congratulations !! You guessed the correct word")
    print("Word = ", word)
else :
    print("Good Try !! Better luck next time")
    print("Word = ", word)
    print("Guessed Word", "".join(hiddenWord))