# Title: Tarea 3
# Estidiante: Juan Fernando Aviles Guillen
# Curso: C1-Nocturno


#1. Crea un archivo llamado "archivo.txt" y escribe en él "Hola, mundo!"
def crearArchivo():
    archivo = open("archivo.txt", "w")
    archivo.write("Hola, mundo!")
    archivo.close()

crearArchivo()


#2. Lee el contenido del archivo "archivo.txt" y muéstralo por pantalla.
def leerArchivo():
    archivo = open("archivo.txt", "r")
    print(archivo.read())
    archivo.close()

leerArchivo()


#3. Añade "¡Python es increíble!" al final del archivo "archivo.txt".
def anadirArchivo():
    archivo = open("archivo.txt", "a")
    archivo.write("\n¡Python es increíble!")
    archivo.close()
anadirArchivo()


#4. Cuenta cuántas líneas tiene el archivo "archivo.txt".
def contarLineas():
    archivo = open("archivo.txt", "r")
    print(len(archivo.readlines()))
    archivo.close()
contarLineas()


#5. Lee la segunda línea del archivo "archivo.txt".
def leerSegundaLinea():
    archivo = open("archivo.txt", "r")
    print(archivo.readlines()[1])
    archivo.close()
leerSegundaLinea()

#6. Crea una copia del archivo "archivo.txt" llamada "copia_archivo.txt".
def copiarArchivo():
    archivo = open("archivo.txt", "r")
    archivo2 = open("copia_archivo.txt", "w")
    archivo2.write(archivo.read())
    archivo.close()
    archivo2.close()
copiarArchivo()

#7. Crea una función que reciba un nombre de archivo como parámetro y muestre su contenido por pantalla.

def mostrarContenido(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    print(archivo.read())
    archivo.close()
mostrarContenido("archivo.txt")
print("\n------------------------------------------------------------")

#8. Crea una función que reciba un nombre de archivo como parámetro y devuelva la cantidad de caracteres que contiene.
def contarCaracteres(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    print(len(archivo.read()))
    archivo.close()
contarCaracteres("archivo.txt")

#9. Escribe una lista de números en un archivo llamado "numeros.txt", uno por línea.
def escribirNumeros():
    archivo = open("numeros.txt", "w")
    for i in range(15):
        archivo.write(str(i)+"\n")
    archivo.close()
escribirNumeros()

#10. Lee el archivo "numeros.txt" y suma todos los números presentes en él.
def sumarNumeros():
    archivo = open("numeros.txt", "r")
    suma = 0
    for linea in archivo.readlines():
        suma += int(linea)
    print(suma)
    archivo.close()
sumarNumeros()

#11. Escribe un programa que pida al usuario ingresar una línea de texto y la guarde en un archivo llamado "entrada_usuario.txt".
def entradaUsuario():
    archivo = open("entrada_usuario.txt", "w")
    archivo.write(input("Ingrese una linea de texto: "))
    archivo.close()
#entradaUsuario()

#12. Crea una función que tome un archivo HTML como entrada y cuente cuántas etiquetas <p> contiene.
def contarEtiquetas():
    archivo = open("exercises.html", "r")
    contador = 0
    for linea in archivo.readlines():
        if "<p>" in linea:
            contador += 1
    print(contador)
    archivo.close()
contarEtiquetas()

#13. Escribe un programa que reemplace todas las ocurrencias de una palabra específica en un archivo de texto.
def reemplazarPalabra():
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    archivo.close()
    archivo = open("archivo.txt", "w")
    archivo.write(contenido.replace("mundo", "python"))
    archivo.close()
reemplazarPalabra()

#14. Crea un programa que lea un archivo JSON y muestre solo los elementos que cumplen cierta condición.
import json
def mostrarElementos():
    archivo = open("data.json", "r")
    contenido = json.load(archivo)
    archivo.close()
    for elemento in contenido:
        if elemento["edad"] > 18:
            print(elemento)
mostrarElementos()

#15. Crea un programa que concatene dos archivos de texto en uno nuevo.
def concatenarArchivos():
    archivo1 = open("archivo.txt", "r")
    archivo2 = open("numeros.txt", "r")
    archivo3 = open("concatenado.txt", "w")
    archivo3.write(archivo1.read() + archivo2.read())
    archivo1.close()
    archivo2.close()
    archivo3.close()
concatenarArchivos()

#16. Escribe una función que tome una lista de nombres y los escriba en un archivo de texto, uno por línea.
def escribirNombres(lista_nombres):
    archivo = open("nombres.txt", "w")
    for nombre in lista_nombres:
        archivo.write(nombre + "\n")
    archivo.close()
escribirNombres(["Juan", "Pedro", "Luis", "Maria","Juan", "Ana"])

#17. Crea un programa que ordene alfabéticamente las líneas de un archivo de texto.
def ordenarAlfabeticamente():
    archivo = open("nombres.txt", "r")
    lista_nombres = archivo.readlines()
    archivo.close()
    lista_nombres.sort()
    archivo = open("nombres.txt", "w")
    for nombre in lista_nombres:
        archivo.write(nombre)
    archivo.close()
ordenarAlfabeticamente()

#18. Crea un programa que lea un archivo de texto y muestre las n primeras líneas.
def mostrarNLineas(n):
    archivo = open("nombres.txt", "r")
    for i in range(n):
        print(archivo.readline())
    archivo.close()
mostrarNLineas(2)

#18. Escribe una función que lea un archivo de texto y elimine las líneas duplicadas.
def eliminarLineasDuplicadas():
    archivo = open("nombres.txt", "r")
    lista_nombres = archivo.readlines()
    archivo.close()
    lista_nombres = list(set(lista_nombres))
    archivo = open("nombres.txt", "w")
    for nombre in lista_nombres:
        archivo.write(nombre)
    archivo.close()
eliminarLineasDuplicadas()

#19. Crea un programa que recorra todos los archivos de un directorio y muestre sus nombres.
import os
def mostrarArchivosDirectorio():
    for archivo in os.listdir("."):
        print(archivo)
mostrarArchivosDirectorio()

#20. Crea un programa que lea un archivo de texto y reemplace las vocales con acento por vocales sin acento.
def reemplazarVocales():
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    archivo.close()
    archivo = open("archivo.txt", "w")
    archivo.write(contenido.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u"))
    archivo.close()
reemplazarVocales()

#21. Escribe una función que lea un archivo de texto y cuente la cantidad de veces que aparece una palabra específica.
def contarPalabra(palabra):
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    archivo.close()
    print(contenido.count(palabra))
contarPalabra("Python")

#22. Escribe una función que reciba el nombre de un archivo y devuelva la longitud del contenido más largo de una línea.
def longitudLineaMasLarga(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    longitud = 0
    for linea in lineas:
        if len(linea) > longitud:
            longitud = len(linea)
    print(longitud)
longitudLineaMasLarga("archivo.txt")

#23. Implementa un programa que encuentre la palabra más larga en un archivo de texto.
import re
def palabraMasLarga():
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    archivo.close()
    palabras = re.findall(r'\b\w+\b', contenido)
    longitud = 0
    for palabra in palabras:
        if len(palabra) > longitud:
            longitud = len(palabra)
            palabra_mas_larga = palabra
    print(palabra_mas_larga)
palabraMasLarga()

#24. Crea un programa que lea un archivo de texto y elimine todas las líneas en blanco.
def eliminarLineasBlanco():
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    archivo.close()
    archivo = open("archivo.txt", "w")
    archivo.write(contenido.replace("\n\n", "\n"))
    archivo.close()
eliminarLineasBlanco()

#25. Escribe una función que lea un archivo de texto y cuente cuántas vocales hay en él.
def contarVocales():
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    archivo.close()
    print(contenido.count("a") + contenido.count("e") + contenido.count("i") + contenido.count("o") + contenido.count("u"))
contarVocales()

#26. Crea una función que lea dos archivos de texto, los compare y muestre las líneas que son iguales en ambos.
def compararArchivos():
    archivo1 = open("archivo.txt", "r")
    archivo2 = open("copia_archivo.txt", "r")
    contenido1 = [linea.strip() for linea in archivo1.readlines()]
    contenido2 = [linea.strip() for linea in archivo2.readlines()]
    archivo1.close()
    archivo2.close()
    for linea in contenido1:
        if linea in contenido2:
            print(linea)
compararArchivos()

#27. Escribe un programa que recorra todos los archivos de un directorio y muestre sus nombres junto con la cantidad de líneas que contienen.
import os
def mostrarArchivosDirectorio():
    for archivo in os.listdir("."):
        if os.path.isfile(archivo):
            archivo2 = open(archivo, "r")
            print(archivo + " " + str(len(archivo2.readlines())))
            archivo2.close()
mostrarArchivosDirectorio()

print("\n-------------------------------------------------------------")

print("\nTarea por: Juan Fernando Aviles Guillen")

print("\n----------------------Fin de la Tarea------------------------")