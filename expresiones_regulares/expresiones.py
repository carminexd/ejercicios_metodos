import re



with open(r"C:\Users\ricar\Downloads\carta.txt", "r", encoding="utf-8") as file:
 contenido = file.read().strip()

contenido=contenido.strip()
correos = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" #sirve para sacar correos electronicos
nombres = r"\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+\b" #sirve basicamente para reconocer solo nombres
fechas  = r"\b\d{1,2}[-/]\d{1,2}\b|\b\d{1,2} de [A-Za-záéíóúÁÉÍÓÚñ]+\b" #sirve para sacar fechas
horas   = r"\d{1,2}+\:\d{2}+" #sirve para sacar horas
calles = r"(Calle [A-ZÁÉÍÓÚa-záéíóú\s]+[0-9]+, oficina \d+)"
links   =r"https?://[a-zA-Z._-]+\.[a-z]{2,3}"
dominios =r"[a-zA-ZÁÉÍÓÚÑ]+\.[a-z]{2,3}"

cadena_correos = re.findall(correos, contenido)
cadena_nombres = re.findall(nombres, contenido)
cadena_fechas  = re.findall(fechas, contenido)
cadena_horas   = re.findall(horas, contenido)
cadena_calles = re.findall(calles, contenido)
cadena_link    =re.findall(links,contenido) #http://reunion.curso-programacion.com
cadena_org     =re.findall(dominios,contenido)

# Verificar si se encontraron correos
if cadena_correos:
        print("Lista de correos electrónicos encontrados:")
        for i, correo in enumerate (cadena_correos, start=1):
            print(f"{i}: {correo}")
else:
        print("\n⚠ No se encontraron correos electrónicos en el archivo.")

# Busca los nombres
if cadena_nombres:
        print("\nLista de nombres doxeados:")
        for i, nombre in enumerate(cadena_nombres, start=1):
            print(f"{i}: {nombre}")
        print("")
else:
        print("no hay ni un nombre")

# Busca fechas 
if cadena_fechas:
      print("\nlista de fechas:" )
      for i, fecha in enumerate(cadena_fechas, start=1):
            print(f"{i}: {fecha}")
            print("")
else:
      print("no se hayaron fechas")

if cadena_horas:
      print("\nHoras encontradas: ",cadena_horas)
      print("")
else:
      print("no hay")

if cadena_calles:
      print("\nCalles encontradas:", cadena_calles)
      print("")
else:
      print("no hay")

if cadena_link:
      print("\nLinks: ",cadena_link)
      print("")
else:
      print("no hay")

print(cadena_org)