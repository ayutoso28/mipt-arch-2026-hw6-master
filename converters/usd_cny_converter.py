from converters.currency_converter import CurrencyConverter


class UsdCnyConverter(CurrencyConverter):
    """Конвертер USD → CNY."""

    @property
    def target_currency(self) -> str:
        return "CNY"