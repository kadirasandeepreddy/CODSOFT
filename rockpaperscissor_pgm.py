import random
user_choice=int(input("enter the choice:type 0 for rock,1 for paper,2 for scissor"))
if user_choice>=3:
    print("user choice is invalid")
else:
    computer_choice=random.randint(0,2)
    print("computer_choice:")
    print(computer_choice)
    if computer_choice==user_choice:
        print("it is draw")
    elif computer_choice==0 and user_choice==2:
        print("your lose")
    elif user_choice_0 and computer_choice==2:
        print("you win")
    elif computer_choice>user_choice:
        print("you lose")
    elif user_choice>computer_choice:
        print("you win")

#logic in book
