class Dictionaries:
    def __init__(self, io):
        self.io = io

    def exercise_one(self):
        # Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
        # pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa
        # no está en el diccionario.
        # :returns "La divisa no está en el diccionario."
        amounts = {'Euro': '€', 'Dólar': '$', 'Yen': '¥'}
        amount = self.io.input("Introduce una divisa: ")
        if amount.title() in amounts:
            self.io.output(amounts[amount.title()])
        else:
            self.io.output("La divisa no está en el diccionario.")

    def exercise_two(self):
        """
        Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un
        diccionario. Después debe mostrar por pantalla el mensaje: "<nombre> tiene <edad> años, vive en <dirección>
        y su número de teléfono es <teléfono>".
        """
        name = self.io.input('¿Cómo te llamas? ')
        age = self.io.input('¿Cuántos años tienes? ')
        address = self.io.input('¿Cuál es tu dirección? ')
        phone = self.io.input('¿Cuál es tu número de teléfono? ')
        user = {'name': name, 'age': age, 'address': address, 'phone': phone}
        self.io.output(
            f'{user["name"]} tiene {user["age"]} años, vive en {user["address"]} y su número de teléfono es {user["phone"]}'
        )

    def exercise_tree(self):
        """
        Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al
        usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
        Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
        Fruta	Precio
        Plátano	1.35
        Manzana	0.80
        Pera	0.85
        Naranja	0.70
        :returns '{kg} kilos de {fruta} valen ${frutas[fruta] * kg}' / "Lo siento, la fruta {fruta} no está disponible."
        """
        frutas = {'Plátano': 1.35, 'Manzana': 0.8, 'Pera': 0.85, 'Naranja': 0.7}
        fruta = self.io.input('¿Qué fruta quieres? ').title()
        kg = float(self.io.input('¿Cuántos kilos? '))
        if fruta in frutas:
            self.io.output(f'{kg} kilos de {fruta} valen ${frutas[fruta] * kg}')
        else:
            self.io.output(f"Lo siento, la fruta {fruta} no está disponible.")

    def exercise_four(self):
        # Escribir un programa que pregunte una fecha en formato dd/mm/aaaa
        # y muestre por pantalla la misma fecha en formato "dd de <mes> de aaaa" donde <mes> es el nombre del mes.
        meses = {1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
                 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'}
        fecha = self.io.input('Introduce una fecha en formato dd/mm/aaaa: ')
        fecha = fecha.split('/')
        self.io.output(f'{fecha[0]} de {meses[int(fecha[1])]} de {fecha[2]}')

    def exercise_five(self):
        """
        Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
        {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura
         en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del
         curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
        """
        curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
        total_creditos = 0
        for asignatura, creditos in curso.items():
            self.io.output(f'{asignatura} tiene {creditos} créditos')
            total_creditos += creditos
        self.io.output(f'Número total de créditos del curso: {total_creditos}')

    def exercise_six(self):
        # Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una
        # persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario.
        # Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
        persona = {}
        continuar = True
        while continuar:
            clave = self.io.input('¿Qué dato quieres introducir? ')
            valor = self.io.input(clave + ': ')
            persona[clave] = valor
            self.io.output(persona)
            continuar = self.io.input('¿Quieres añadir más información (Si/No)? ') == "Si"

    def exercise_seven(self):
        """
        Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar
        el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.
        Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
        Lista de la compra
        Artículo 1	Precio
        Artículo 2	Precio
        Artículo 3	Precio
            …	        …
        Total	    Coste
        """
        pass

    def exercise_eight(self):
        """
        Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá
        las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción>
        separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones.
        Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
        Si una palabra no está en el diccionario debe dejarla sin traducir.
        """
        pass

    def exercise_nine(self):
        """
        Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
        Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura
        y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura,
        pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura
        y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura
        y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad
        cobrada hasta el momento y la cantidad pendiente de cobro.
        """
        pass

    def exercise_ten(self):
        """
        Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
        Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
        y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
        donde preferente tendrá el valor True si se trata de un cliente preferente.
        El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente,
        (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6)
        Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
        Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
        Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
        Preguntar por el NIF del cliente y mostrar sus datos.
        Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
        Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
        Terminar el programa.
        """
        pass

    def exercise_eleven(self):
        """
        El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo,
        donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica.
        Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de
        los campos con la información contenida en el directorio.
        "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
        Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento
        corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la
        información del cliente. Los diccionarios con la información de cada cliente tendrán como claves los
        nombres de los campos y como valores la información de cada cliente correspondientes a los campos.
        Es decir, un diccionario como el siguiente
        {'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576',
        'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com',
        'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez',
        'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2},
        '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com',
        'teléfono': '667677855', 'descuento': 15.7}}
        """
        pass
