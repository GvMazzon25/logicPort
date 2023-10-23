from porte_logiche import porta_not


def main():
    x = input('Inserisci un numero binario (0 o 1): ')
    result = porta_not(x)
    if result is not None:
        print(f"NOT di {x} è {result}")


if __name__ == "__main__":
    main()
