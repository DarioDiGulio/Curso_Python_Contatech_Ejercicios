class Strings:
    def __init__(self, io):
        self.io = io

    def exercise_one(self):
        """
        Escribir un programa que pregunte el nombre del usuario en la consola y
        un número entero e imprima por pantalla en líneas distintas el nombre
        del usuario tantas veces como el número introducido.
        """
        name = self.io.input("¿Cómo te llamas?")
        number = self.io.input("Introduce un número entero: ", int)
        self.io.output(f'{name}\n' * int(number))

    def exercise_two(self):
        """
        Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla
        el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las
        letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
        El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
        """
        full_name: str = self.io.input("Cuál es tu nombre completo?")
        self.io.output(full_name.lower())
        self.io.output(full_name.upper())
        self.io.output(full_name.title())

    def exercise_tree(self):
        """
        Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario
        lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario
        en mayúsculas y <n> es el número de letras que tienen el nombre.
        """
        full_name: str = self.io.input("Cuál es tu nombre completo?")
        self.io.output(f'{full_name.upper()} tiene {len(full_name)} letras.')

    def exercise_four(self):
        """
        Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo
        es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
        Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla
        el número de teléfono sin el prefijo y la extensión.
        """
        full_phone_number: str = self.io.input("Ingresá tu número de celular completo: ")
        self.io.output(full_phone_number.split("-")[1])

    def exercise_five(self):
        """
        Escribir un programa que pida al usuario que introduzca una frase
        en la consola y muestre por pantalla la frase invertida.
        """
        sentence: str = self.io.input("Ingresá la frase que más te guste por favor: ")
        self.io.output(sentence[::-1])

    def exercise_six(self):
        """
        Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal
        y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
        """
        sentence: str = self.io.input("Ingresá la frase que más te guste por favor: ")
        vocal: str = self.io.input("Ahora ingresá una vocal: ")
        self.io.output(sentence.replace(vocal, vocal.upper()))

    def exercise_seven(self):
        """
        Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla
        otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
        """
        email: str = self.io.input("Introduce tu correo electrónico: ")
        self.io.output(email[:email.find('@')] + '@ceu.es')

    def exercise_eight(self):
        """
        Escribir un programa que pregunte por consola el precio de un producto en pesos con dos decimales
        y muestre por pantalla el número de pesos y el número de centavos del precio introducido.
        """
        amount: str = self.io.input("Introduce el precio del producto con dos decimales:  ")
        self.io.output(f'{amount[:amount.find(".")]} pesos y, {amount[amount.find(".") + 1:]} centavos.')

    def exercise_nine(self):
        """
        Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa
        y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione
        cuando el día o el mes se introduzcan con un solo carácter.
        """
        date = self.io.input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
        day = date[:date.find('/')]
        year_month = date[date.find('/') + 1:]
        month = year_month[:year_month.find('/')]
        year = year_month[year_month.find('/') + 1:]
        self.io.output(f'Día {day}')
        self.io.output(f'Mes {month}')
        self.io.output(f'Año {year}')
