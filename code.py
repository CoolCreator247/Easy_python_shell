
import time
def intro():
    print("what is your name")
    name = input("name>")
    time.sleep(2)
    print(f"Hi",name) 
    print("Welcome to easy shell")
    print("If you need help type help in the shell")
    #inform
        
while True:   
    def run_shell():
        shell = input(">")
        if shell == help:

                print("check https://www.w3schools.com/python/ for a good learning path")
        else:    
            exec(shell)
            #run code from the shell var
    
    def run_all():
        intro()
        run_shell()
    run_all()            

   
        

