import os

def RunExample():
    while True:
        run = input("Choose Example to run (1 > 4 or exit): ")
        
        if run == "1":
            os.system("cd src && py Example1.py")
        elif run == "2":
            os.system("cd src && py Example2.py")
        elif run == "3":
            os.system("cd src && py Example3.py")
        elif run == "4":
            os.system("cd src && py Example4.py")
        elif run == "exit":
            exit()
        else:
            print("Invalid input. Please choose a number between 1 and 4.")
            # return to input 

RunExample()
