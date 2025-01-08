class Book:
    def __init__(self, title, quantity,author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount=None

    def set_discount(self,discount):
        self.__discount=discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price
    
    def __repr__(self):
        return f"Titulo: {self.title}, Autor: {self.author}, Cantidad: {self.quantity}, Precio: {self.get_price(),3}"
    


class Novel(Book):
    def __init__(self, title, author, price,branch,quantity):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return f"Titulo: {self.title}, Autor: {self.author}, Cantidad: {self.quantity}, Precio: {self.get_price(),3}, Genero: {self.branch}"
    
class Academic(Book):
    def __init__(self, title, author, price,branch,quantity):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return f"Titulo: {self.title}, Autor: {self.author}, Cantidad: {self.quantity}, Precio: {self.get_price(),3}, Genero: {self.branch}"
    


Novela1=Novel(
    title="La Casa de los Espíritus",
    author="Isabel Allende",
    price=20,
    branch="Novela",
    quantity=10
)
Novela1.set_discount(0.20)

ensayo1=Academic(
    title="El Capital",
    author="Karl Marx",
    price=30,
    branch="Economía",
    quantity=5
)
print(Novela1)
print(ensayo1)  