#coding: utf-8


#início do código
#operações matemáticas
print (1+2)
print (2-1)
print (2/2)
print (4%2)
print (8%3)
print (2**2)
#funções matemáticas
print (max(2,4,9))
print (min(1,5,8))
print (abs(-22))

#operações com string

#concatenar
print ("Curso" + "de" + "Python")


print ("Caixa d'agua") #correto

#print ('Caixa d'agua') #errado - cuidar as aspas simples
print ('Caixa d\'agua') #correto

#funções com strings
print (len ("Curso de Python"))

var = "CURSO DE PYTHON"
print (var.lower())

var = "curso de python"
print (var.upper())


print (2,5)

print (2)

#print ("Data: ", 02/04/2019) #errado
print ("Data: ", "02/04/2019") #certo

print ("Temperatura externa: "+ str(25))


var = "Curso de Python"
var.isalpha()


var = "Curso"
var.isalpha()