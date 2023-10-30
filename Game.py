print("Welcome to the Crossroad trivia Game")
print("You have 5 crossroads to get to a house which has treasure")
print("Per crossroad you have one life")
print("In the house you will enconter a House which has the treasure")

def crossRoad1():
    print("You are in cross road 1 : History")
    lives = 1
    print("Which year did US get independence : ")
    if lives > 0 :
        print("Enter 1 to use life")
    ans     = str(input())

    if ans== "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "1776") :
            return False

    print("What was the name of first US president : ")
    if lives > 0 :
        print("Enter 1 to use life")

    ans = str(input())

    if ans == "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "George Washington") :
            return False

    print("What is the largest state of US : ")
    if lives > 0 :
        print("Enter 1 to use life")

    ans = str(input())

    if ans == "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "Alaska") :
            return False

    return True


def crossRoad2():
    print("You are in cross road 2 : Sports")
    lives = 1

    print("What country won the first World Cup in 1930? : ")
    if lives > 0 :
        print("Enter 1 to use life")
    ans     = str(input())

    if ans== "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "Uruguay") :
            return False

    print("Who is considered the GOAT of Basketball : ")
    if lives > 0 :
        print("Enter 1 to use life")

    ans = str(input())

    if ans == "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "Michael Jordan") :
            return False

    print("Which boxer was known as The Greatest and The People’s Champion : ")
    if lives > 0 :
        print("Enter 1 to use life")

    ans = str(input())

    if ans == "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "Muhammad Ali") :
            return False

    return True


def crossRoad3():
    print("You are in cross road 3 : Chemistry")
    lives = 1

    print("How many elements are there in the Periodic Table? : ")
    if lives > 0 :
        print("Enter 1 to use life")
    ans     = str(input())

    if ans== "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "118") :
            return False

    print("Who is considered the greatest Chemist of all times : ")
    if lives > 0 :
        print("Enter 1 to use life")

    ans = str(input())

    if ans == "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "Dmitri Mendeleev") :
            return False

    print("Who is considered the father of organic chemistry? : ")
    if lives > 0 :
        print("Enter 1 to use life")

    ans = str(input())
    if ans == "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "William Perkins") :
            return False

    return True


def crossRoad4():
    print("You are in cross road 4 : Physics")  
    lives = 1

    print("What is the anti-matter equivalent of an electron? : ")
    if lives > 0 :
        print("Enter 1 to use life")
    ans     = str(input())

    if ans == "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "positron") :
            return False

    print("What tool uses a magnetic needle that points in different directions? : ")
    if lives > 0 :
        print("Enter 1 to use life")

    ans = str(input())

    if ans == "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "compass") :
            return False

    print("What was the first sound-recording device called? : ")
    if lives > 0 :
        print("Enter 1 to use life")

    ans = str(input())
    if ans == "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "phonograph") :
            return False

    return True

def crossRoad5():
    print("You are in cross road 5: Unanimous : ")
    lives = 1

    print("What is the Capital city of Paraguay")
    if lives > 0 :
        print("Enter 1 to use life")
    ans     = str(input())

    if ans== "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "Asuncion") :
            return False

    print("The Cassegranian, Schmidt and Gregorian are all types of what scientific instrument?")
    if lives > 0 :
        print("Enter 1 to use life")
    ans     = str(input())

    if ans== "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "telescopes") :
            return False

    print("In which sea battle was Mark Antony defeated by Octavian in 31 BC?")
    if lives > 0 :
        print("Enter 1 to use life")
    ans     = str(input())

    if ans== "1" and lives > 0 :
        lives = lives - 1
    else :
        if (ans != "Actium") :
            return False
        
    return True


def Hall1Room1():
    print("You encounter a swamp with alligators, what do you do")
    decision = input("Enter 1 to walk through it, or Enter anyting else to get out : ")
    if decision == "1":
        print("The alligator sees you, want's to eat you")
        print("Enter 1 to use life or enter 2 to try and escape")
        ans = input("Enter 1 or 2")
        if ans == "1" :
            lives = lives - 1
        if ans == "2" :
            print("The alligator is chasing you")
            print("Answer this question to get a speed boost and stay alive")
            Quest = input("How many years can a alligator live up to?")
            if Quest  == "43" or "44" or "45" :
                print("You have survived")
            else :
                print("Sorry, you have been eaten. Game over.")
                return False
    else :
        print("Well tried but you could not get to the treasure.")
        return False

    return True

    
def Hall1Room2():
    print("You didn't notice that this was a swamp, and you fell in the swamp")
    print("You see a crocodile 10 ft behind you, and he notices you. He's coming towards you")
    print("You're trying to escape. Answer this question to get a swim boost")
    Quest = input("What are crocodile species called?")
    if Quest == "Dwarf Crocodile" :
        print("You have escaped by getting a swim boost")
    else :
        print("Sorry, you have been eaten. Game over")
        return False
    
    return True


def Hall2Room1():
    print("You encounter a deadly python snake. If you wake him up, he can potentially kill you.")
    print("In order to move on you need to answer a question")
    question = input("How many feet can a python grow up to.")

    if question == "33":
        print("You move on to the last stage before you get to the treasure")
    else :
        print("You have woke up the snake. He kills you")
        print("      Game Over      ")
        return False
    
    return True

        
def Hall2Room2():
    print("You encounter a King Kobra, which bites you in the neck, leading you to faint")
    print("Answer these 2 trivia questions to stay alive. Need to get both right")
    question = input("Which European country technically shares a border with Brazil, because one of its “overseas departments” does?")

    if question == "France" :
        print("You're almost to the treasure!")
    else :
        print("You died. Game over.")
        return False
    
    question = input("What actor said, “If you had been a public figure since the time you were a toddler… maybe you too would value privacy above all else”?")
    if question == " Jodie Foster" :
        print("You're almost to the treasure!")
    else :
        print("You died. Game over.")
        return False

    return True
    
def TreasureDoor():
    print("The wait's almost over. You're at the treasure door.")
    print("All you need to do is answer this puzzle, which contains a part of these")
    print(" ")
    print("The number of lilies in a pond double each day. It takes 48 days to fill the whole pond. How many days does it take to fill the pond with half the lilies.")
    puzzle = input("What do you think is the answer. Take your time")

    if puzzle == "47" :
        print("Woooooooooooooooohhhhhhhhhhh!!!!!!!!!!!! You just won $10 Million dollars and 50 pounds of Gold!!!!!!!!!!!!!!!")
        print("Congratulatulations!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else :
        print("I feel bad for you. Youre wrong. But, I think you were very close. Don't make this upset you. You're still a winner to make it to the Treasure Door. You still get $200,000 and 2 pounds of gold!")
        return False

    return True


# Main Program
entry = True
if (entry):
    entry = crossRoad1()
if (entry):
    entry = crossRoad2()
if (entry):
    entry = crossRoad3()
if (entry):
    entry = crossRoad4()
if (entry):
    entry = crossRoad5()

if (entry):
    print("You have made it through the 5 crossroads")
    print("The wait for the treasure ain't over yet")
    print("You have reached the house with treasure")
    print("This house has 2 Halls and each Hall has 2 Rooms")
    print("You are in Hall1")
    choice = int(input("Enter 1 to enter Room 1 or Enter anything else Enter Room 2 :"))
    if (choice == 1):
        entry = Hall1Room1()
    else :
        entry = Hall1Room2()

if (entry):
    print("You are in Hall2")
    choice = int(input("Enter 1 to enter Room 1 or Enter anything else Enter Room 2 :"))
    if (choice == 1):
        entry = Hall2Room1()
    else :
        entry = Hall2Room2()

if (entry):
    TreasureDoor()

if (entry):
    print("You're a winner!!!!")
else :
    print("Good luck next time")