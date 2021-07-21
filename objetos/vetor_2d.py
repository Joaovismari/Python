class vetor:
    def __init__(self,x,y):#magic method init
        self.x = x
        self.y = y

    def norma(vet):
        return ((vet.x**2+vet.y**2)**(1/2))

    def __add__(vet1,vet2):
        return vetor(vet1.x+vet2.x,vet1.y+vet2.y)

v1 = vetor(3,3)
v2 = vetor(4,5)
v3 = v1 + v2 #magic method add
print(v1.norma())
print(v2.norma())
print(v3.norma())