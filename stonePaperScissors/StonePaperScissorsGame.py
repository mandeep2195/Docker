import random
import os
import time
# from flask import Flask, request, jsonify
# app = Flask(__name__)
# if __name__ == "__main__":
#     app.run(debug=True)
# app.route("/")
def call():
        print('''Rules =>  
        1 is stone
        2 is paper
        3 is scissors''')
        dict1 = {"1": "stone", "2": "paper", "3": "scissors"}
        playerwin = 0
        computerwin = 0
        i = 1
        while i <= 3:
            print("We'll play 3 times. This is time ", i)

            computer = str(random.randint(1,3))

            computerchoose = dict1[computer]
            player = input("enter a number to choose\n ==>")
            b = dict1[player]
            # print(type(b))
            print("you choose ",b, "Computer choose ", computerchoose)
            if (player==computer):
                print("its a tie")
            elif ((computer=="2" and player=="1")or(computer=="3" and player=="2")or(computer=="1" and player=="3")):
                print("computer wins, it choose: ", computerchoose)
                computerwin +=1
            elif ((computer=="1" and player=="2")or(computer=="2" and player=="3")or(computer=="3" and player=="1")):
                print("you won, computer choose: " , computerchoose)
                playerwin += 1
            i+=1
        print("Result =>")
        if(playerwin>computerwin):
            print("you won by " , playerwin -computerwin, " point.")
        elif(playerwin<computerwin):
            print("computer won by ", computerwin - playerwin , " point.")
        elif(playerwin==computerwin):
            print("It was a tie.")
        time.sleep(3)
        os.system('cls')

call()
while True:
    choice = int(input('''Enter 0 to play again
Enter 9 to Exit\n==>'''))
    match choice:
        case 0:
            call()
        case 9:
            exit()