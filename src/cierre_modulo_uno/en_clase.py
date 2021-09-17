"""
Un depósito de gaseosas nos pide que le desarrollemos un sistema de gestión para sus traslados.
La idea es que el programa pueda recibir tres comandos:
"ingreso": recibirá una lista de gaseosas (hasta recibir "fin" como gaseosa).
Por cada una recibirá una cantidad y su nombre y deberá agregarlas al stock.

"egreso": recibirá una lista de gaseosas,
hasta recibir "fin" como gaseosa, con cantidades y nombre y deberá descontarlas del stock.

"cierre mensual": deberá calcular y mostrar el stock resultante del mes por cada gaseosa,
la cantidad de viajes realizados discriminados por egresos e ingresos y un balance general de viajes
(resta entre cantidad de egresos e ingresos). También el balance de dinero adquirido,
teniendo en cuenta que los ingresos son compras y los egresos son ventas.

Teniendo en cuenta la siguiente tabla de productos:
Gaseosa ---------------- Stock ---------------- Precio de lista
Lima        ----------------   50    ----------------         $78
Cola        -----------------   70    ----------------         $90
Naranja   ----------------   50    ----------------         $52
Manzana ---------------    90    ----------------         $44
"""

db = [
    {
        "nombre": "lima",
        "stock": 50,
        "precio": 78,
        "balance": 0
    },
    {
        "nombre": "cola",
        "stock": 70,
        "precio": 90,
        "balance": 0
    },
    {
        "nombre": "naranja",
        "stock": 50,
        "precio": 52,
        "balance": 0
    },
    {
        "nombre": "manzana",
        "stock": 90,
        "precio": 44,
        "balance": 0
    }
]
cantidad_ingresos = 0
cantidad_egresos = 0


def es_comando_disponible(user_command: str, commands: list) -> bool:
    return user_command in commands


def pedir_cantidad(gaseosa: str) -> int:
    try:
        cantidad = int(input(f"Ingrese la cantidad de gaseosas de {gaseosa}: "))
        return cantidad
    except ValueError:
        print("La cantidad ingresada no es válida.")
        return 0


def aumentar_stock(nombre_gaseosa: str, cantidad: int) -> None:
    for gaseosa in db:
        if gaseosa["nombre"] == nombre_gaseosa:
            gaseosa['stock'] += cantidad


def modificar_balance(nombre_gaseosa: str, cantidad: int) -> None:
    for gaseosa in db:
        if gaseosa["nombre"] == nombre_gaseosa:
            precio_lista = gaseosa["precio"]
            importe = precio_lista * cantidad
            gaseosa["balance"] += importe


def procesar_ingreso(gaseosa_ingresada: str) -> bool:
    if gaseosa_ingresada == "fin":
        continuar = False
    else:
        cantidad = pedir_cantidad(gaseosa_ingresada)
        aumentar_stock(gaseosa_ingresada, cantidad)
        modificar_balance(gaseosa_ingresada, -cantidad)
        continuar = True
    return continuar


# noinspection PyPep8Naming
def ingreso() -> None:
    continuar = True
    global cantidad_ingresos
    cantidad_ingresos += + 1
    while continuar:
        gaseosa_ingresada = input("Ingresá una gaseosa: ['Lima', 'Cola', 'Naranja', 'Manzana', 'Fin']").lower()
        if es_comando_disponible(gaseosa_ingresada, ['lima', 'cola', 'naranja', 'manzana', 'fin']):
            continuar = procesar_ingreso(gaseosa_ingresada)
        else:
            print("ERROR: ¡No ingresaste una gaseosa válida!")


def restar_stock(nombre_gaseosa: str, cantidad: int) -> None:
    for gaseosa in db:
        if gaseosa["nombre"] == nombre_gaseosa:
            gaseosa['stock'] -= cantidad


# noinspection PyPep8Naming
def procesar_egreso(gaseosa_ingresada):
    if gaseosa_ingresada == "fin":
        continuar = False
    else:
        cantidad = pedir_cantidad(gaseosa_ingresada)
        restar_stock(gaseosa_ingresada, cantidad)
        modificar_balance(gaseosa_ingresada, cantidad)
        continuar = True
    return continuar


def actualizar_ingresos_totales():
    global cantidad_egresos
    cantidad_egresos += 1


def egreso() -> None:
    continuar = True
    actualizar_ingresos_totales()
    while continuar:
        gaseosa_ingresada = input("Ingresá una gaseosa: ['Lima', 'Cola', 'Naranja', 'Manzana', 'Fin']").lower()
        if es_comando_disponible(gaseosa_ingresada, ['lima', 'cola', 'naranja', 'manzana', 'fin']):
            continuar = procesar_egreso(gaseosa_ingresada)
        else:
            print("ERROR: ¡No ingresaste una gaseosa válida!")


def mostrar_stock_final() -> None:
    print("---- Stock final del mes ----")
    for gaseosa in db:
        print(f'{gaseosa["nombre"]}: {gaseosa["stock"]}')


def mostrar_balance_movimientos():
    print("---- Balance de ingresos y egresos ----")
    print(f"Ingresos totales: {cantidad_ingresos}")
    print(f"Egresos totales: {cantidad_egresos}")
    print(f"Balance general: {cantidad_egresos - cantidad_ingresos}")


def mostrar_balance_economico() -> None:
    print("---- Balance económico ----")
    balance_total = 0
    for gaseosa in db:
        balance_total += gaseosa["balance"]
    print(f"Balance total: ${balance_total}")


def cierre_mensual() -> None:
    mostrar_stock_final()
    mostrar_balance_movimientos()
    mostrar_balance_economico()


# noinspection PyPep8Naming
def procesar_comandos() -> None:
    continuar = True
    while continuar:
        user_input = input("Ingresá un comando: ['egreso', 'ingreso', 'cierre mensual', 'fin']").lower()
        INGRESO = "ingreso"
        EGRESO = "egreso"
        CIERRE_MENSUAL = "cierre mensual"
        FIN = "fin"
        if user_input == INGRESO:
            ingreso()
        elif user_input == EGRESO:
            egreso()
        elif user_input == CIERRE_MENSUAL:
            cierre_mensual()
        elif user_input == FIN:
            continuar = False
        else:
            print("ERROR: ¡No ingresaste un comando válido!")


def main() -> None:
    procesar_comandos()


if __name__ == '__main__':
    main()
