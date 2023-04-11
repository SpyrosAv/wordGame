# AVOURIS SPYRIDON 

#Δήλωση βιβλιοθήκης random
import random

print("\n\n----Game starting----\n\n")

#Δήλωση αρχείου και ανάγνωση των γραμμών του
file = open("words.txt", "r")
read = file.read().splitlines()

# Επιλογή τυχαίας λέξης(γραμμής) από το αρχείο
word = random.choice(read)

guesses = " "

# Προκαθορισμένος αριθμός γύρων
turns = 5

# Όσο το turns είναι θετικό:
while turns > 0:
    if(len(word)>=4) :              # στις λέξεις με μήκος πάνω απο 4 
        letterReveal = word[0:3]    # φανερώνονται οι 3 πρώτοι χαρακτήρες
    else:
        letterReveal = word[0]      # αλλιώς μόνο ο πρώτος χαρακτήρας
    # μετρητής για τον αριθμό αποτυχιών του χρήστη
    failed = 0
    
    print("\nThe word is: ", end='')
    print(letterReveal, end='')
    # εκτύπωση υπολοιπόμενων χαρακτήρων της λέξης αρχικά με τη χρήση 
    # της κάτω παύλας και στη συνέχεια (αν μαντεύει σωστά ο χρήστης),
    # με την κανονική τους μορφή
    for char in word[len(letterReveal):]:
        
        if char in guesses:
            print(char, end='')
           
        else:
            print("_ ", end='')
             
            # Αύξηση failed κατά 1 κάθε φορά που ο χρήστης μαντέυει λάθος
            failed += 1

    # Ο χρήστης κερδίζει εάν δεν έχει κάνει καμία λάθος μαντεψιά
    if failed == 0:
        print("\n\n!!! Congratulations, you won !!!")
         
        # εκτύπωση της λέξης στην κανονική της μορφή
        print("The word was: ", word)
        break
     
    # Το πρόγραμμα ζητάει απο τον χρήστη να μαντέψει
    # έναν (ή και περισσότερους) χαρακτήρα/-ες.
    guess = input("\nGuess a character: ")
     
    # Αποθήκευση προσωρινής μαντεψιάς.
    guesses += guess
     
    # Εάν ο χαρακτήρας δεν υπάρχει στην λέξη:
    if guess not in word:
        # Μείωση των γύρων κατά 1.
        turns -= 1
         
        # Εκτυπώνεται το μηνυμα
        print("\nWrong...There is no such character in the word.")
         
        # μαζί με τις εναπομείναντες προσπάθειες
        print("You have", + turns, 'more guesses.')

        # Εάν τελειώσουν οι προκαθορισμένοι γύροι, τότε ο χρήστης χάνει.
        if turns == 0:
            print("\n    You lost. \n\n    :(\n\n    Game over.")
            print("The word was \"",word,"\".\n")
    
    # Αλλιώς, ο χρήστης συνεχίζει τις μαντεψιές.
    else:
        print("\nRight!")