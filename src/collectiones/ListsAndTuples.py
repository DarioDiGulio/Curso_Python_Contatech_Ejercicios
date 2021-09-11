class ListsAndTuples:
    def __init__(self, io):
        self.io = io

    def exercise_one(self):
        # Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
        # Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
        subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
        self.io.output(subjects)

    def exercise_two(self):
        """
        Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química,
        Historia y Lengua) en una lista y la muestre por pantalla el mensaje
        Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
        """
        subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
        for subject in subjects:
            self.io.output(f"Yo estudio {subject}")

    def exercise_tree(self):
        """
        Escribir un programa que almacene las asignaturas de un curso (Matemáticas, Física,
        Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura,
        y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde
        <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
        notas introducidas por el usuario.
        :return En <asignatura> has sacado <nota>
        """
        subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
        scores = []
        for subject in subjects:
            score = self.io.input("¿Qué nota has sacado en " + subject + "?")
            scores.append(score)
        for i in range(len(subjects)):
            self.io.output("En " + subjects[i] + " has sacado " + scores[i])

    def exercise_four(self):
        # Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
        # los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
        awarded = []
        for i in range(6):
            winner_number = self.io.input("Introduce un número ganador: ")
            awarded.append(int(winner_number))
        awarded.sort()
        self.io.output("Los números ganadores son " + str(awarded))

    def exercise_five(self):
        # Escribir un programa que almacene en una lista los números del 1 al 10
        # y los muestre por pantalla en orden inverso separados por comas.
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(1, 11):
            self.io.output(f"{numbers[-i]},")

    def exercise_six(self):
        """
        Escribir un programa que almacene las asignaturas de un curso (Matemáticas, Física,
        Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y
        elimine de la lista las asignaturas aprobadas (6 o más).
        Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
        :return "Tienes que repetir <list>"
        """
        subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
        for i in range(len(subjects) - 1, -1, -1):
            score = float(self.io.input("¿Qué nota has sacado en " + subjects[i] + "?"))
            if score >= 6:
                subjects.pop(i)
        self.io.output("Tienes que repetir " + str(subjects))

    def exercise_seven(self):
        """
        Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que
        ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
        """
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in range(len(alphabet), 1, -1):
            if i % 3 == 0:
                alphabet.pop(i - 1)
        self.io.output(alphabet)

    def exercise_eight(self):
        """
        Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
        :return "No es un palíndromo" or "Es un palíndromo"
        """
        word = self.io.input("Introduce una palabra: ")
        reversed_word = word
        word = list(word)
        reversed_word = list(reversed_word)
        reversed_word.reverse()
        if word == reversed_word:
            self.io.output("Es un palíndromo")
        else:
            self.io.output("No es un palíndromo")

    def exercise_nine(self):
        """
        Escribir un programa que pida al usuario una palabra y muestre por
        pantalla el número de veces que contiene cada vocal.
        :return "La vocal <vocal> aparece <times> veces"
        """
        word = self.io.input("Introduce una palabra: ")
        vocals = ['a', 'e', 'i', 'o', 'u']
        for vocal in vocals:
            times = 0
            for letter in word:
                if letter == vocal:
                    times += 1
            self.io.output("La vocal " + vocal + " aparece " + str(times) + " veces")

    def exercise_ten(self):
        """
        Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
        y muestre por pantalla el menor y el mayor de los precios.
        :return "El mínimo es <min>" "El máximo es <max>"
        """
        prices = [50, 75, 46, 22, 80, 65, 8]
        min_import = max_import = prices[0]
        for price in prices:
            if price < min_import:
                min_import = price
            elif price > max_import:
                max_import = price
        self.io.output("El mínimo es " + str(min_import))
        self.io.output("El máximo es " + str(max_import))

    def exercise_eleven(self):
        """
        Escribir un programa que almacene los vectores (1,2,3) y
        (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
        """
        a = (1, 2, 3)
        b = (-1, 0, 2)
        product = 0
        for i in range(len(a)):
            product += a[i] * b[i]
        self.io.output("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product))

    def exercise_twelve(self):
        """
        Escribir un programa que pregunte por una muestra de números, separados por guión,
         los guarde en una lista y muestre por pantalla su media y desviación típica.
         :return "La media es <media> , y la desviación típica es <desviacion_tipica>"
        """
        sample = self.io.input("Introduce una muestra de números separados por comas: ")
        sample = sample.split('-')
        n = len(sample)
        for i in range(n):
            sample[i] = int(sample[i])
        sample = tuple(sample)
        sum = 0
        sumsq = 0
        for i in sample:
            sum += i
            sumsq += i ** 2
        mean = sum / n
        stdev = (sumsq / n - mean ** 2) ** (1 / 2)
        self.io.output(f'La media es {mean} y la desviación típica es {stdev}')
