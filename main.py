a = [5,1,4,9,0]
""" 
numeros = [5,1,4,9,0]
ordenados = sorted(numeros)
print(ordenados)
print(a[3:10])
print(a[3:10:2]) """

""" print(a[2]) """


""" b = range(3,10) + range(20, 23)  """
# da type error, los obejetos tipo range no soportan el operador de suma

""" for i in range(3,10):
    print(i)

for i in range(20,23):
    print(i) """
    
b = list(range(3, 10)) + list(range(20, 23))
# para que funcionara el código sin errores, se transformó a lista obteniendo como resultado 22
""" print(b[9]) """
""" print(complex(b[0], b[1])) """


c = [[1,2], [3,4,5], [6,7]]
""" print(c[1][2])
 """
""" print(len(c))
print(len(c[0])) """
""" print(c[-1]) """
""" print(c[-1][+1]) """




d = ["perro", "gato", "jirafa", "elefante"]
""" print(d.index("jirafa")) """
""" print(c[2:]+ d[2:]) """



 e = ["a", a, 2 * a] 
""" print(e[0]==e[1]) """
""" print(len(e)) """

#RESULTADOS
#4
#22
#5
#False
#3
#2
#3
#[6,7]
#7
#[6,7], ['jirafa','elefante']
#9,0
#9
#2
#4
#3+4j