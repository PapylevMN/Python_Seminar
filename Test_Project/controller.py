import interface
import rational_number
import complex_number

def run():
    input_data = interface.get_data()
    result = rational_number.start_modul(input_data)
    interface.show_result(result)