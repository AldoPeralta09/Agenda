import csv

class agenda:
    def __init__(self):
        print "Menu\n"
        print "1. Ver agenda\n"
        print "2. Agregar Contacto\n"
        print "3. Salir de la aplicacion"
        
        self.option = int(raw_input("Eliga una opcion "))
        
        if self.option == 1:
            self.verAgenda()
        elif self.option == 2:
            self.agregarContacto()
        elif self.option == 3:
            exit()
        else:
            print "Opcion no valida..."
            exit()
            
    def verAgenda(self):
        with open("agenda.csv","r") as file:
            data = csv.reader(file, delimiter = "$")
            for line in data:
                print line
                
    def agregarContacto(self):
        self.name = str(raw_input("Ingresa el nombre: "))
        self.email = str(raw_input("Ingresa el email: "))
        self.phone = str(raw_input("Ingresa el telefono: "))
        self.age = str(raw_input("Ingresa la edad: "))
        
        with open("agenda.csv","a") as file:
            data = csv.writer(file, delimiter = "$")
            data.writerow([self.name, self.email, self.phone, self.age])
            
agendaAldo = agenda()
