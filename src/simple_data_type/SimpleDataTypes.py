class SimpleDataTypes:
    def __init__(self, io):
        self.io = io

    def exercise_one(self):
        # Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
        self.io.output("¡Hola Mundo!")

    def exercise_two(self):
        # Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y
        # luego muestre por pantalla el contenido de la variable.
        message = '¡Hola Mundo!'
        self.io.output(message)

    def exercise_tree(self):
        # Escribir un programa que pregunte el nombre del usuario en la consola
        # y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola < nombre >!,
        # donde < nombre > es el nombre que el usuario haya introducido.
        user_name = self.io.input('Por favor, ingresá tu nombre:', str)
        self.io.output(f'¡Hola {user_name}!')

    def exercise_four(self):
        # Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+2/2*5)2
        self.io.output(((3 + 2) / (2 * 5)) ** 2)

    def exercise_five(self):
        # Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
        # Después debe mostrar por pantalla la paga que le corresponde
        hours_worked = self.io.input("¿Cuántas horas trabajaste?", int)
        hourly_rate = self.io.input("¿Cuánto te pagan por hora?", int)
        self.io.output(f'Te corresponden como paga: {hours_worked * hourly_rate}')

    def exercise_six(self):
        """
        Escribir un programa que lea un entero positivo n, introducido por el usuario y después muestre en pantalla
        la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada
        de la siguiente forma: suma = (n (n + 1)) / 2
        """
        n = self.io.input("Introduce un número entero:", int)
        add = n * (n + 1) / 2
        self.io.output(f'La suma de los primeros números enteros desde 1 hasta {n} es {add}')

    def exercise_seven(self):
        """
        Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa
        corporal y lo almacene en una variable, y muestre por pantalla la frase "Tu índice de masa corporal es <imv>"
        donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
        """
        weight = self.io.input("¿Cuál es tu peso en kg?", float)
        height = self.io.input("¿Cuál es tu estatura en metros?", float)
        imc = round(weight / (height ** 2), 2)
        self.io.output(f'Tu índice de masa corporal es {imc}')

    def exercise_eight(self):
        """
        Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un
        cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
         y <c> y <r> son el cociente y el resto de la división entera respectivamente.
        """
        n = self.io.input("Introduce el dividendo (entero):", int)
        m = self.io.input("Introduce el divisor (entero):", int)
        self.io.output(f'La {n} entre {m} da un cociente {n // m} y un resto {n % m}')

    def exercise_nine(self):
        """
        Escribir un programa que pregunte al usuario una cantidad a invertir,
        el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
        """
        capital = self.io.input("¿Cantidad a invertir?", float)
        interest = self.io.input("¿Interés porcentual anual?", float)
        years = self.io.input("¿Años?", int)
        self.io.output(f'Capital final: {(round(capital * (interest / 100 + 1) ** years, 2))}')

    def exercise_ten(self):
        """
        Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
        Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular
        el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
        cada muñeca 75g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido
        y calcule el peso total del paquete que será enviado.
        """
        clown_weight = 112
        dolls_weight = 75
        clowns = self.io.input("Introduce el número de payasos a enviar:", int)
        dolls = self.io.input("Introduce el número de muñecas a enviar:", int)
        total_weight = (clown_weight * clowns) + (dolls_weight * dolls)
        self.io.output(f'El peso total del paquete es {total_weight}')

    def exercise_eleven(self):
        """
        Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
        Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance
        final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada
        en la cuenta de ahorros, introducida por el usuario.
        Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras
        el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
        """
        investment = self.io.input("Introduce la inversión inicial:", float)
        interest = 0.04
        balance_first_year = investment * (1 + interest)
        self.io.output(f'Balance tras el primer año: {(round(balance_first_year, 2))}')
        balance_second_year = balance_first_year * (1 + interest)
        self.io.output(f'Balance tras el segundo año: {(round(balance_second_year, 2))}')
        balance_third_year = balance_second_year * (1 + interest)
        self.io.output(f'Balance tras el tercer año: {(round(balance_third_year, 2))}')

    def exercise_twelve(self):
        """
        Una panadería vende barras de pan a $3,49 cada una. El pan que no es del día tiene un descuento del %60.
        Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa
        debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y
        el coste final total.
        """
        barras = self.io.input("Introduce el número de barras vendidas que no son frescas:", int)
        amount = 3.49
        discount = 0.6
        coast = barras * amount * (1 - discount)
        self.io.output(f'El coste de una barra fresca es ${amount}')
        self.io.output(f'El descuento sobre una barra no fresca es {discount * 100} %')
        self.io.output(f'El coste final a pagar es ${round(coast, 2)}')
