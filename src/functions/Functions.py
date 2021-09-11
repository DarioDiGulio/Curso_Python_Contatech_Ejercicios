def exercise_one() -> str:
    print("¡Hola mundo!")
    return "¡Hola mundo!"


def saludar_por_nombre(name: str = "") -> str:
    name = input("ingresá tu nombre:")
    print(f"Hola {name}")
    return f"Hola {name}"
