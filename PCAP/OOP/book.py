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
    



book1=Book(title="Harry Potter",quantity=10,author="J.K. Rowling",price=20.0)
book2=Book(title="El Señor de los Anillos",quantity=5,author="J.R.R. Tolkien",price=30.0)
book3=Book(title="El Círculo Mágico",quantity=7,author="J.K. Rowling",price=25.0)


print(book1)
print(book2)
print(book3)

print(book1.title)
print(book1.quantity)
print(book1.author)
print(book1.get_price())
