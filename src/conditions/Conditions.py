class Conditions:
    def __init__(self, io):
        self.io = io

    def exercise_one(self):
        """
        Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
        :returns "Sos mayor de edad." / "No sos mayor de edad."
        """
        user_age = self.io.input("¿Cuál es tu edad?")
        user_age = int(user_age)
        if user_age >= 18:
            self.io.output("Sos mayor de edad.")
        else:
            self.io.output("No sos mayor de edad.")

    def exercise_two(self):
        """
        Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable,
        pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario
        coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
        :returns "No coincide." / "Coincide."
        """
        pass

    def exercise_tree(self):
        """
        Escribir un programa que pida al usuario dos números enteros y muestre por pantalla su división.
        Si el divisor es cero el programa debe mostrar un error.
        El resultado debe ser un número entero.
        :return error => "¡Error! No se puede dividir por 0."
        :return success => "El resultado de la división es {resultado}."
        """
        pass

    def exercise_four(self):
        """
        Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
        :return "El número {number} es par." / "El número {number} es impar."
        """
        pass

    def exercise_five(self):
        """
        Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales
        o superiores a $1000 mensuales. Escribir un programa que pregunte al usuario su edad y sus
        ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
        :return "Tenés que cotizar." / "No tenés que cotizar."
        """
        pass

    def exercise_six(self):
        """
        Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
        Primero pedirle al usuario el sexo y luego el nombre.
        El grupo A esta formado por las mujeres(F) con un nombre anterior a la M y los hombres(M)
        con un nombre posterior o igual a la M y el grupo B por el resto. Escribir un programa que pregunte al
        usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
        :return "Tu grupo es {group}."
        """
        pass
