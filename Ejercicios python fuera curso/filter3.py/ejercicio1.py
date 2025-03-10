class Empleado:
    def __init__(self, nombre, apellidos, cargo, salario):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.__salario = salario

    def get_salario(self):
        return self.__salario
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.cargo}) - Salario: {self.__salario}"


listaEmpleados = [
    Empleado("Antonio", "García", "CEO", 75000),
    Empleado("Luis", "Gálvez Sánchez", "informatico", 80000),
    Empleado("Ana", "Rodríguez", "Administrativo", 25000),
    Empleado("Mario", "Pérez", "Conserje", 20000)
]

filtro_salario = filter(lambda x: x.get_salario() > 50000, listaEmpleados)

print("Empleados con salario > 50k:")
for empleado in filtro_salario:
    print(empleado)

print("\nEmpleados con salario <= 50k:")
for empleado in listaEmpleados:
    if empleado.get_salario() <= 50000:
        print(empleado)

print("\nLuis Gálvez Sánchez, 75578608x")