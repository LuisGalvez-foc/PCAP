class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,val):
        self.queue.append(val)
        return self.queue

    def dequeue(self):
        if len(self.queue)>0:
            numero=self.queue.pop(0)
            return numero
        else:
            return "no hay nada"
        
    def __str__(self):
        return str(self.queue)
        

pila=Queue()
print(pila.enqueue(1))
print(pila.enqueue(2))
print(pila.enqueue(3))

print(pila.__str__())

print(pila.dequeue())
print(pila.dequeue()) 
print(pila.dequeue()) 
print(pila.dequeue()) 

 


    
        