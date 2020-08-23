print(f"Ingrese",end=" ")
print(f"5",end=" ")
print(f"notas:")
while True:
    while True:
        try:
            a = int(input("nota-1: "))
            break
        except ValueError:
            print("vuelva a ingresar: ")
        
        
    while True:
        try:    
            b = int(input("nota-2: "))
            break
        except ValueError:
            print("vuelva_a_ingresar")
            
            
    while True:
        try:    
            c = int(input("nota-3: "))
            break
        except ValueError:
            print("vuelva_a_ingresar")
     
        
    while True:
        try:    
            d = int(input("nota-4: "))
            break
        except ValueError:
            print("vuelva_a_ingresar")
       
            
    
    while True:     
        try:        
            e = int(input("nota-5: "))
            break
        except ValueError:
            print("vuelva_a_ingresar")
    break
            
        


x = (a,b,c,d,e)
print(x)
g = (a+b+c+d+e)
n = int(len(x))
P = (g/n)

print(f"su",end=" ")
print(f"promedio",end=" ")
print(f"es:",end=" ")
print(f"{P}")