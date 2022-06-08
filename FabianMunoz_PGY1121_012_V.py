datoscliente = {'patente': "",
            'marca' : "",
            'modelo' : "",
            "añofab" : 0,
            "tipovehiculo":"",
            "registros" : "",
}
registrosguardados = []
datosclientes = []

print("bienvenido a ServiExpress")


validadorpatente = False


while True:
    try:
        while True:
            opc = int(input(''' 
[1] Registrar automóvil
[2] Registro Mantenimiento
[3] Consultar datos de automovil
[4] Salir
'''))
            if opc ==1:
                print("Registrar automóvil")
                while True:
                    patente = input("Ingrese patente:")
                    if patente[0:2].isalpha() and patente[2:4].isdigit() or patente[2:4].isalpha() and patente[4:6].isdigit():
                        break
                    else:
                        print("La patente ingresada no es válida, ingresela nuevamente: \n")
                while True:
                    marca = input("Ingrese marca de su automóvil: \n")
                    if len(marca) !=None:
                        break               
                    else:
                        print("Debe ingresar una marca")
                while True:        
                    modelo = input("Ingrese modelo de su automóvil: \n")
                    if len(modelo) !=None: 
                        break             
                    else:
                        print("Debe ingresar un modelo")
                while True:          
                    añofab = int(input("Ingresa el año de fabricación de tu vehículo: \n"))  
                    if añofab >=1900 and añofab <=2021:
                        break
                    else:
                        print("Ingrese un año de fabricación válido (entre 1900 y 2021)\n")    
                while True:
                    tipovehiculo = input('''Ingresa letra correspondiente al tipo de vehículo: 
[B] encina
[D] iesel
[E] léctrico
[H] íbrido
''')
                    if tipovehiculo == "d" or "D" or "b" or "B" or "e" or "E" or "h" or "H":
                        break
                    else:
                        print("Ingresa una letra válida.")
                registros = input("Ingresa registros del vehículo en el siguiente formato:\n DD/MM/YYY - Registro: \n")
                registrosguardados.append(registros)
                datosclientes.append({'patente':patente, 'marca': marca, 'modelo': modelo, 'añofab': añofab, 'tipovehiculo': tipovehiculo, 'registros':registros})
            elif opc ==2:
                print("Registro mantenimiento")
                patente = input("Ingrese patente de vehículo para registrar mantenimiento:\n")
                for regmantenimiento in datosclientes:
                    if patente == regmantenimiento['patente']:
                        validadorpatente = True
                if validadorpatente:
                    ingresofecha = input("ingresa fecha de mantenimiento en formato DD/MM/AAAA:  ")
                    ingresoobservacion = input("Ingrese observaciones para revisión mecánico: ")
                    registrosguardados.append(regmantenimiento)
            elif opc == 3:
                print("Consulta datos de automóvil:\n")
                patente = input("Ingresa la patente del automóvil que busca:\n")
                for patenteconsulta in datosclientes:
                    if patente == patenteconsulta['patente']:
                        validadorRut = True
                if validadorpatente:
                    patente = patenteconsulta['patente']
                    marca = patenteconsulta['marca'].capitalize()
                    modelo = patenteconsulta['modelo'].capitalize()
                    añofab = patenteconsulta['añofab']
                    tipovehiculo = patenteconsulta['tipovehiculo'].capitalize()
                    registros = patenteconsulta['registros'].capitalize()
                    print("-----------Datos del automóvil -------")
                    print(f"patente: {patente}\n marca: {marca}\n modelo: {modelo}\n añofab: {añofab}\n tipovehiculo: {tipovehiculo}\n registros: {registros}\n")
                elif validadorpatente == False:
                    print("Patente ingresada no existe en ekl sistema")
            elif opc ==4:
                print("=======================================")
                print("Saliendo")
                print("=======================================")
                print("Gracias por suscribirse a la app de juan maestro")
                break
        break
    except ValueError:
        print("Error, ingreso un dato mal.")
        