
import sys

class Stack:
    def __init__(self):
        self.__stack_list = []
    

    def push(self,val):
     self.__stack_list.append(val)

    def pop(self):
        val=self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
    def imprimir(self):
       print(f"pila= {self.__stack_list}")


stack_obeject=Stack()
stack_obeject.push(3)
stack_obeject.push(2)
stack_obeject.push(1)

stack_obeject.imprimir()

