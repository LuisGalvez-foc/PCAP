class Empleado:
    plantilla=[]
    num_empleados=0


    def __init__(self, nombre:str, apellidos,cargo: str, salario):

        if salario <= 0:
            raise ValueError("El salario debe ser positivo")
        
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.__salario = salario
        Empleado.plantilla.append(self)
        Empleado.num_empleados += 1

    


    def get_salario(self):
        return self.__salario
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.cargo} - {self.get_salario()}"




Empleado1=Empleado("Juan", "Perez", "Gerente", 60000)
Empleado2=Empleado("Maria", "Gzalez", "Secretaria", 20000)
Empleado3=Empleado("Pedro", "Lopez", "Desarrollador", 600)

for h in Empleado.plantilla:
    print(h)

print(Empleado.__dict__)