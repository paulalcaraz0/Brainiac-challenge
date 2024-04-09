attempted_questions = set()
correct_answers = 0 
user_account = {}

def num_one():
    print("""***QUESTION 1 FOR ROUND 2***
          
          Which continent is the largest by land area? """)
    return quiz("Your answer: ", "asia")
   

def num_two():
    print("""***QUESTION 2 FOR ROUND 2***
          
          What is the output of the following Python code?
          print(2 + 3 * 4) """)
    # 14 (The multiplication operation is performed before addition, so 3 * 4 is evaluated first, resulting in 12, which is then added to 2)
    return quiz("Your answer: ", 14)

def num_three():
    print("""***QUESTION 3 FOR ROUND 2***
          
          You have a basket containing 10 apples. You take away 2 apples. How many apples do you have now?
          *** number only answer*** """)
    # You took away 2 apples from the basket, but you still physically have them.
    return quiz("Your answer: ", 2)



def next_level():
        print("\nWELCOME TO THE NEXT LEVEL!!\n"
            "You will now answer 3 questions from Round 2.\n")

        correct_answers = 0

        for i in range(6, 9):
            if i == 6:
                if num_one():
                    correct_answers += 1
            elif i == 7:
                if num_two():
                    correct_answers += 1
            elif i == 8:
                if num_three():
                    correct_answers += 1

        print("\nCongratulations! You have completed the quiz.")
        print(f"You have answered {correct_answers} out of 3 questions correctly!")
        

        score = int(correct_answers / 3 * 100)
        print(f"Your score is: {score}%")
        exit()

def quiz(question, answer, max_attempts=5):
    global correct_answers 
    attempts = 0
    while attempts < max_attempts:
        guess = input(question)
        if guess.lower() == str(answer).lower():
            print("Congratulations! You got it right!\n")
            correct_answers += 1  
            return True
        else:
            attempts += 1
            if attempts < max_attempts:
                print("Sorry, that's incorrect. You have {} attempts left.".format(max_attempts - attempts))
    print("\nSorry, you've run out of attempts. The correct answer was {}.".format(answer))
    return False


def quest_one():
    print("1) What is the name of the largest organ in the human body? ")
    return quiz("Your answer: ", "skin")
    
def quest_two():
    print("2) What is the value of pi?")
    return quiz("Your answer: ", 3.14)

def quest_three():
    print("3) What popular messaging app was acquired by Facebook in 2014 for $19 billion?")
    return quiz("Your answer: ","WhatsApp" )

def quest_four():
    print("4) Who is considered the national hero of the Philippines, known for his role in the Philippine Revolution against Spanish colonial rule in the late 19th century?")
    return quiz("Your answer: ", "jose rizal" )

def quest_five():
    print("5) A farmer has 17 sheep, and all but 9 die. How many are left?")    
    return quiz("Your answer: ",9 )

def questions():
    print("""*Get ready to exercise those brain cells with a mix of intriguing questions! Here's what's I prepare for you:
         ***REMINDER YOUR SCORE SHOULD BE MORE THAN 50% TO PROCEED ONTO THE NEXT LEVEL***
          1. Let's dive into the realm of the human body!
          2. Prepare for some number magic in the world of math!
          3. Explore the wonders of technology with this question!
          4. Time to honor a national hero's legacy!
          5. Think logically and crack the puzzle!\n""")

    while len(attempted_questions) < 5:
        
        choice = int(input("Enter a number (1-5) to answer a question: "))
        if not choice:
            exit()
        if choice < 1 or choice > 5:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        if f'quest_{choice}' in attempted_questions:
            print("You are done to this question!!")
            continue
        attempted_questions.add(f'quest_{choice}')
        
        if choice == 1:
            quest_one()
        elif choice == 2:
            quest_two()
        elif choice == 3:
            quest_three()
        elif choice == 4:
            quest_four()
        elif choice == 5:
            quest_five()

    print("\nCongratulations! You have completed the quiz.")
    print(f"You have {correct_answers} correct answer!!")
    
    score = int(correct_answers / (5) * 100)
    print(f"Your score is: {score}%")

    if score >= 50:
        print("\nWe are moving to the next level!!")
        
        space = input("Enter if you want to exit and pres 'q' if you want to try next level! : ")        
        if space.lower() == 'q':
                next_level()
        else:
            print("THANK YOU FOR ANSWERING!!")
            exit()

def sign_in():
    print("Sign-In")
    print("Sign-In Account")

    
    while True:
        try:
            user = input("Enter username: ")
            if not user:
                main()
            password = input("Enter password: ")
            if user_account.get(user) and user_account[user]['password'] == password:
                print("Login Successful")
                questions()
            else:
                print("Invalid username or password")
        except ValueError as e:
            print(e)
            main()

def register():
    print("REGISTER!!")
    print("Input Information")
    while True:
        try:
            user = input(str("Enter username: "))
            if user in user_account:
                print("Username aldready existed!")
                continue
            user_balance = 0
            user_points = 0
            while True: 
                try:
                    password = input("Enter a password that is minimum of 8 characters! : ")
                    if len(password) >= 8:
                        user_account[user] = {"password" : password, "balance" : user_balance, "points" : user_points} 
                        print("Save password!")
                        print("Successfully Registered")
                        main()
                    else:
                        print("Password must be atleast minimum of 8 caharacters!")
                except ValueError as e:
                    print(e)
                    register()   
        except ValueError as e:
            print(e)
            register()  


def main():
    print("Welcome to Game Rental Store")
    print("1. Register")
    print("2. Sign In")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    while True:
        if choice == 1:
            register()
            break
        if choice == 2:
            sign_in()
        if choice == 3:
            print("Exit!")
            exit()
        else:
            print("Invalid Input")
            main()


main()