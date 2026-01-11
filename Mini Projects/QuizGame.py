#quiz game using list and tuples

questions = ("What company makes the Xperia line of smartphones?", 
             "Which city is home to the Brandenburg Gate?", 
             "What is the fourth state of matter, after solid, liquid, and gas?", 
             "What are plants that lose their leaves in autumn called?", 
             "Who is generally considered the inventor of the motor car?")
options = (("A.Samsung", "B.Sony", "C.Nokia", "D.Apple"), 
           ("A.Paris", "B.Berlin", "C.Rome", "D.London"),
           ("A.Ether", "B.Plasma ", "C.Jelly ", "D.Earth "), 
           ("A.Coniferous", "B.Evergreen", "C.Carnivorous", "D.Deciduous"), 
           ("A.Henry Ford ", "B.Karl Benz", "C.Gottlieb Daimler", "D.Nikola Tesla"))
answers = ("B", "B", "C", "D", "B")
guesses=[]  #appending user guess. so list.
score = 0
question_number = 0

#displaying the questions with options
for question in questions:
    print("------------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    
    #taking user input for answer
    guess = input("Enter the option (A, B, C, D): ").upper()
    guesses.append(guess)
    #scoring
    if guess == answers[question_number]:
        score = score+1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_number]} is the correct answer")
    question_number += 1
print("------------------------------")
print(f"Yor score is {score}")
print("------------------------------")

'''
Output:
------------------------------
What company makes the Xperia line of smartphones?
A.Samsung
B.Sony
C.Nokia
D.Apple
Enter the option (A, B, C, D): b
CORRECT!
------------------------------
Which city is home to the Brandenburg Gate?
A.Paris
B.Berlin
C.Rome
D.London
Enter the option (A, B, C, D): b
CORRECT!
------------------------------
What is the fourth state of matter, after solid, liquid, and gas?
A.Ether
B.Plasma
C.Jelly
D.Earth
Enter the option (A, B, C, D): b
INCORRECT
C is the correct answer
------------------------------
What are plants that lose their leaves in autumn called?  
A.Coniferous
B.Evergreen
C.Carnivorous
D.Deciduous
Enter the option (A, B, C, D): d
CORRECT!
------------------------------
Who is generally considered the inventor of the motor car?A.Henry Ford
B.Karl Benz
C.Gottlieb Daimler
D.Nikola Tesla
Enter the option (A, B, C, D): b
CORRECT!
------------------------------
Yor score is 4
------------------------------
'''