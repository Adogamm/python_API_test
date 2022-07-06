import requests

class Request:
    
    def __init__(self):
        pass

    def insert_employee(self,employee_data):
        response = requests.post('http://127.0.0.1:8081/employees/create_employee',json=employee_data)
        return print("Datos guardados exitosamente "+response.text)
