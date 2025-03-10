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
    
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False




Empleado1=Empleado("Juan", "Perez", "Gerente", 60000)
Empleado2=Empleado("Maria", "Gzalez", "Secretaria", 20000)
Empleado3=Empleado("Pedro", "Lopez", "Desarrollador", 600)

for h in Empleado.plantilla:
    print(h)

print(Empleado.__dict__)
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")

num1=7
num2=7.0
num3=7.5

if Empleado.is_integer(num1):
    print(num1,"Es un entero")
else:
    print("No es un entero")

if Empleado.is_integer(num2):
    print(num2,"Es un entero")
else:
    print("No es un entero")

if Empleado.is_integer(num3):
    print(num3,"Es un entero")
else:
    print(num3,"No es un entero")  
