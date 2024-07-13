import random
from random import randint

trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez'
                ,'Isabel Gómez','Francisco Díaz','Elena Fernández']
sueldo=[]
menor_800k=[]
entre_800k_2000k=[]
sobre_2000k=[]


def sueldos_alea():
    
    for trabajador in trabajadores:
        print(f"{trabajador.ljust(20)} {str(randint(300000, 2500000)).ljust(10)}")
        sueldo.append({"nombre":trabajador, "sueldo":randint(300000,2500000)})
    print(sueldo)
    
    
    

           

       
        
    


def menu():
    while True:
        print("1)Asignar sueldos aleatorios. ")
        print("2)Clasificar sueldos. ")
        print("3)Ver Estadisticas. ")
        print("4)Reporte de sueldos. ")
        print("5)Salir del programa.")
        
        opc = int(input("Ingrese opcion. "))
        
        opc == 1
        sueldos_alea()
        
        
        
       
        
        opc == 5
        print("Saliendo del programa. ")
        print("Desarrollado por Moises Salinas")
        print("Rut 20.060.701-5")
        

        
menu()
    