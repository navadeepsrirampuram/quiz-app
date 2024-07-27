name = input("enter your name: ")
wish = input("do you want to play the game : ").lower()
score = 0
if wish == "yes":
    print("let's start the game")
    print("Welcome to the game"+"  "+name)
    question1 = input("what is the addition of 2+3: ")
    if question1 == "5" :
        print("correct")
        score+=1
    else:
        
        print("incorrect")
    question2 = input("what is the fullform of cpu : ").lower()
    if question2 == "central processing unit" :
        print("correct")
        score+=1
    else:
        print("incorrect")
    question3 = input("who is the father of computers : ").lower
    if question3 == "charles babbage" :
        print("correct")
        score+=1
    else:
        print("incorrect")
    question4 = input("who created python : ").lower()
    if question4 == "guido van rossum" :
        print("correct")
        score+=1
    else:
        print("incorrect")
else:
    print("Game Over")
print("your total score is " + str(score) )
print("you got " + str((score/4)*100))


