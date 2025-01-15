class Empleado:
    def __init__(self, nombre, apellidos,cargo, salario):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.__salario = salario

    def get_salario(self):
        return self.__salario
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.cargo} - {self.get_salario()}"


lista_empleados=[
    Empleado("Juan", "Perez", "Gerente", 60000),
    Empleado("Maria", "Gonzalez", "Secretaria", 20000),
    Empleado("Pedro", "Lopez", "Desarrollador", 60000)
]

empleados_vip=[empleado for empleado in lista_empleados if empleado.get_salario()>50000]

for e in empleados_vip:
    print(e)  