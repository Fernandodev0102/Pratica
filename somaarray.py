Array = ["a","d",2,"a","d",2,"a","d",2,"a","d",2,"a","d",2,"a","d",2]
Soma = 0
for i in range(0,len(Array),3):
    Valores= Array[i+2]
    Soma += Valores


print(Soma)


