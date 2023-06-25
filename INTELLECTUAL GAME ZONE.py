def quiz():
    print("""1.COUNTRIES AND CAPITALS \n2.INDIA STATES AND CAPITAL""")
    ques=int(input("enter your choice:"))
    global score
    score=0
    match ques:
        case 1:
            print("1.what is the capital of 'FRANCE'???")
            print("a.Budapest \nb.Paris \nc.Italy")
            in1=input("choose your answer:")
            match in1:
                case 'a':
                    print("INCORRECT ANSWER")
                case 'b':
                    score+=1
                    print("GREAT JOB!!! CORRECT ANSWER")
                case 'c':
                    print("INCORRECT ANSWER")
                case other:
                    print("enter a valid choice")

            print("2.What is the capital of 'RUSSIA'???")
            print("a.Moscow \nb.Beijing \nc.Kyiv")
            in2=input("choose your answer:")
            match in2:
                case 'a':
                    score+=1
                    print("GREAT JOB!!! CORRECT ANSWER")
                case 'b':
                    print("INCORRECT ANSWER")
                case 'c':
                    print("INCORRECT ANSWER")
                case other:
                    print("enter a valid choice")

            print("YOUR SCORE IS:",score)
        case 2:
             print("1.what is the capital of 'KARNATAKA'???")
             print("a.delhi \nb.Banglore \nc.Mumbai")
             in3=input("choose your answer:")
             match in3:
                case 'a':
                    print("INCORRECT ANSWER")
                case 'b':
                    score+=1
                    print("GREAT JOB!!! CORRECT ANSWER")
                case 'c':
                    print("INCORRECT ANSWER")
                case other:
                    print("enter a valid choice")
             print("2.What is the capital of 'GUJARAT'???")
             print("a.Gandhinagar \nb.dispur \nc.shillong")
             in4=input("choose your answer:")
             match in4:
                case 'a':
                    score+=1
                    print("GREAT JOB!!! CORRECT ANSWER")
                case 'b':
                    print("INCORRECT ANSWER")
                case 'c':
                    print("INCORRECT ANSWER")
                case other:
                    print("enter a valid choice")
             print("YOUR SCORE IS:",score)
def sicbo():
    import random
    min=1
    max=6
    roll_again='y'
    while roll_again=='y':
     print("ROLLING DICE GAME")
     print("guess 2 numbers between '1-6'")
     guess1=int(input("enter guess 1:"))
     guess2=int(input("enter guess 2:"))
     print("the values are:")
     dice1=random.randint(min,max)
     print(dice1)
     dice2=random.randint(min,max)
     print(dice2)
     if(guess1==dice1) and (guess2==dice2):
       print("great job good guess, you are a genius")
     else:
       print("sorry , shall we play again")
       roll_again=input("roll the dice again?(y/n):").lower()
     print("___________________________________")
def number_sequence():
    def fibo():
      print("FIBONACCI NUMBERS")
      e=int(input("enter the end value:"))
      n=0
      n1=1
      print(n)
      print(n1)
      for i in range(e):
   
       n2=n+n1
       print(n2)
       n=n1
       n1=n2
    def fact():
      import math
      print("FACTORIAL")
      a=int(input("enter a value:"))
      fac=math.factorial(a)
      print(f"the factorial of {a} is :", fac)
    def even():
      print("PRINTING EVEN NUMBERS")
      b=int(input("enter the start range:"))
      c=int(input("enter the end range:"))
      for i in range(b,c+1):
        if i%2==0:
            print(i)
    def odd():
      print("PRINTING ODD NUMBERS")
      b=int(input("enter the start range:"))
      c=int(input("enter the end range:"))
      for i in range(b,c):
        if i%2!=0:
            print(i)
    def prime():
      print("PRIME NUMBER GENERATION")
      b=int(input("enter the start range:"))
      c=int(input("enter the end range:"))
      for number in range(b,c):
        if number>1:
          if(number==2) or (number==3)or (number==5):
              print(number)
      for number in range(b,c):
        if number>1:
            if(number%2!=0) and (number%3!=0) and (number%5!=0):
                print(number)
          
    print("\n\nGENERATING NUMBER SEQUENCE")
    print("_______________________________")
    print("\nWHICH NUMBER SEQUENCE YOU WANT TO TRY???")
    print("1.Odd number generator \n2.Even number generator \n3.Fibonacci number sequence")
    print("4.Factorial of a number \n5.Prime number generator")
    choice=int(input("enter your choice:"))
    match choice:
      case 1:
        odd()
        print("_______________________________")
      case 2:
        even()
        print("_______________________________")
      case 3:
        fibo()
        print("_______________________________")
      case 4:
        fact()
        print("_______________________________")
      case 5:
        prime()
        print("_______________________________")
      case other:
        print("enter a valid choice")
def pattern():
    def triangle():
      rows=int(input("enter a number:"))
      for i in range(rows):
       for j in range(rows-i-1):
          print(end=" ")
       for j in range(i+1):
          print("*",end=" ")
       print()




    def diamond():
     rows=int(input("enter a number:"))
     for i in range(rows):
      for j in range(rows-i-1):
        print(end=" ")
      for j in range(i+1):
        print("*",end=" ")
      print()
     for i in range(rows-1,0,-1):
       for j in range(rows-i):
         print(end=" ")
       for j in range(i):
         print("*",end=" ")
       print()
    
        
    


    def odd_stars():
     rows = int(input('Enter the number of rows: '))

     for i in range(rows,0,-1):
         for j in range(rows-i):
             print(' ', end='') 
    
         for j in range(2*i-1):
             print('*',end='') 
         print()



    def square():
     print("\nSQUARE PATTERN")
     rows=int(input("enter a number:"))
     for i in range(rows):
         for j in range(rows):
          print("*",end= " ")
         print()



    def pascal():
     print("\nPASCAL TRIANGLE")
     a=int(input("Enter a number:"))
     for i in range(a):
      print(11**i)
    print("\n*PATTERN PRINTING*")
    print("which pattern you want to try???")
    print("\n1.Triangle Pattern \n2.Diamond Pattern \n3.Square pattern \n4. Pascal triangle")
    choice=int(input("\nenter your choice:"))
    match choice:
       case 1:
           print("TRIANGLE PATTERN")
           triangle()
           
       case 2:
           print("DIAMOND PATTERN")
           diamond()
       case 3:
          
           square()
       case 4:
        
           pascal()
       case other:
        print("enter a valid choice")
def sci_quiz():
    print("\n\t\t***SCIENCE QUIZ****\n\n")
    questions=("1.How many planets are there in solar system?",
               "2.What is the hardest natural substance on earth?",
               "3.what is the largest planet in the solar system?",
               "4.What is the smallest unit of life called?",
               "5.What is the chemical symbol of 'WATER'?")
    options=(("a.7","b.8","c.3","d.9"),
             ("a.iron","b.bronze","c.diamond","d.ruby"),
             ("a.jupiter","b.earth","c.saturn","d.mars"),
             ("a.cell","b.mitochondria","c.pytoplanktons","d.plasma"),
             ("a.co2","b.o2","c.H2O","d.CH3"))
    answers=["b","c","a","a","c"]
    guesses=[]
    score=0
    n=0
    for ques in questions:
        print("_________________________________________________________")
        print(ques)
       
        for opt in options[n]:
            print(opt)
        guess=input("\nEnter your choice of answer:")
        guesses.append(guess)
        if guess==answers[n]:
            
            score+=1
            
            print("\n\ngreat job!!! correct")
        else:
            print(f"\n\nsorry!!! INCORRECT ANSWER\nthe correct ansert is {answers[n]}")
        n+=1

        
    print("********************************************************")
    print("\n\nYOUR SCORE IS:",score)
    final_score=int(score/len(questions)*100)
    print("\n\nYOUR OVERALL SCORE IN PERCENTAGE IS:", final_score,"%")
    print("\n\n********************************************************")
            

def start():
  print("\n\n**INTELLECTUAL GAME ZONE**")
  print("___________________________________")
  print("WHICH GAME YOU WANT TO PLAY??? \n\n1.GK QUIZ \n\n2.SICBO(guessing the dice)")
  print("\n3.GENERATING NUMBER SEQUENCE \n\n4.PATTERN PRINTING")
  print("\n5.SCIENCE QUIZ\n\n")
  choice=int(input("\n\nENTER YOUR CHOICE:"))
  match choice:
    case 1:
        quiz()
    case 2:
        sicbo()
    case 3:
        number_sequence()
    case 4:
        pattern()
    case 5:
        sci_quiz()
    case other:
        print("enter a valid choice")
print("***********************************************************")
print("\n\n\t\t WELCOME TO INTELLECTUAL GAME ZONE\n\n")
print("***********************************************************")
name=input("\nEnter your name:")
names=name.upper()
start()

while(True):
 fin=input("\n\nDo you want to continue playing other games???(y/n)").lower()
 if(fin=='y'):
    start()
 else:
    print("********************************************************")
    print(f"\t\t{names} THANKS FOR PLAYING  \n \t\tHOPE YOU HAD FUN \n\t\tSEE YOU SOON")
    print("********************************************************")
    break
 
  
        
        
                    
                    

