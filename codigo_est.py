marks = []
cadena = ""

for i in range(5):
    while True:
        number = int(input("Ingrese un número: "))
        if 0 <= number <= 100:
            marks.append(number)

            if number >= 0 and number < 50:
                cadena += "F"
            elif number >= 50 and number < 60:
                cadena += "E"
            elif number >= 60 and number < 70:
                cadena += "D"
            elif number >= 70 and number < 80:
                cadena += "C"
            elif number >= 80 and number < 90:
                cadena += "B"
            elif number >= 90 and number <= 100:
                cadena += "A"

            break 
        else:
            print("Ingrese un número válido dentro del rango de 0 a 100.")

print("Calificaciones:", cadena)