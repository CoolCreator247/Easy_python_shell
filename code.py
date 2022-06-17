
def intro():
    print("what is your name")
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
    exec_code()
    #run code from the shell var
  
def run_all():
    intro()
    start_shell()
    run_shell()
run_all()            

   
        

