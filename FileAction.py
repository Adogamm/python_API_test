from Request import Request


class FileAction:

    def __init__(self):
        pass

    def load_file(self):
        try:
            rq = Request()
            file = open('Clientes.txt','r')
            content = file.readlines()
            for i in range(len(content)):
                var = content[i].split(",")
                diccionario = {    "firstname":str(var[0]),
                                    "surname":str(var[1]),
                                    "country":str(var[2]),
                                    "languaje":str(var[3]),
                                    "airport":str(var[4])
                                    }
                rq.insert_employee(diccionario)
        except Exception as e:
            print(e.args)

