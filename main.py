from converters import UsdRubConverter, UsdEurConverter, UsdGbpConverter, UsdCnyConverter


def main():
    amount = float(input('Введите значение в USD:\n'))

    converters = [
        UsdRubConverter(),
        UsdEurConverter(),
        UsdGbpConverter(),
        UsdCnyConverter(),
    ]

    for converter in converters:
        currency = converter.target_currency
        result = converter.convert(amount)
        print(f"{amount} USD to {currency}: {result}")


if __name__ == "__main__":
    main()