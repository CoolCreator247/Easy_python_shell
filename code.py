def setup():
    import time
#import things
def intro():
    print("what is your name")
    time.sleep(2)
    name = input("name>")
    print(f"Hi",name) 
    print("Welcome to easy shell")
    print("If you need help type help in the shell")
    #inform
def start_shell():
    shell = input(">")
    #get input 
def run_shell():
    exec(shell)
        

