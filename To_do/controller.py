import interface
import to_do_hw
import new_task_enter as nt

def run():
    run = True
    while run:
        option = interface.start()
        if option == '7':
            return
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            pass
        elif option == '6':
            pass
        elif option == '1':
            nt.enter_task()
        
    