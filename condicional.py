marks = []
cadena= ""

for i in range(5):        
    marks.append(int(input("Ingrese número: ")))
          
print(marks)

for i in marks:
    if i>=0 and i<50:
        cadena+= "F"
    elif i>=50 and i<60:
        cadena+= "E"
    elif i>=60 and i<70:
        cadena+= "D"
    elif i>=70 and i<80:
        cadena+= "C"
    elif i>=80 and i<90:
        cadena+= "B"
    elif i>=90 and i<101:
        cadena+= "A"
  
print(cadena)
        


        



