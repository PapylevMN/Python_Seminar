import interface
import search as s
import new_task_enter as nt
import convert

def run():
    run = True
    while run:
        option = interface.start()
        if option == '5':
            return
        elif option == '2':
            s.search()
        elif option == '3':
            s.print_all()
        elif option == '4':
            convert.to_csv()
        elif option == '1':
            nt.enter_task()
        
    