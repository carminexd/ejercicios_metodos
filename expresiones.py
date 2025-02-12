import re



with open(r"C:\Users\ricar\Downloads\carta.txt", "r", encoding="utf-8") as file:
 contenido = file.read().strip()

contenido=contenido.strip()
correos = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" #sirve para sacar correos electronicos
nombres = r"\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+\b" #sirve basicamente para reconocer solo nombres
fechas  = r"\b\d{1,2}[-/]\d{1,2}\b|\b\d{1,2} de [A-Za-záéíóúÁÉÍÓÚñ]+\b" #sirve para sacar fechas
horas   = r"\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9] (AM|PM)\b|\b(?:[01]?[0-9]|2[0-3]) (AM|PM)\b" #sirve para sacar horas
cadena_correos = re.findall(correos, contenido)
cadena_nombres = re.findall(nombres, contenido)
cadena_fechas  = re.findall(fechas, contenido)
cadena_horas   = re.findall(horas, contenido)

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
      print("\n lista de fechas:" )
      for i, fecha in enumerate(cadena_fechas, start=1):
            print(f"{i}: {fecha}")
            print("")
else:
      print("no se hayaron fechas")

if cadena_horas:
      print("\nHoras encontradas:")
      for hora in cadena_horas:
            if len (hora)==2:
                print(f"{hora[0]} {hora[1]}")
            else:
                print(hora[0])
else:
      print("no hay")