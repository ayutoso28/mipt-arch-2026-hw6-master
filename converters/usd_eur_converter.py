from converters.currency_converter import CurrencyConverter


class UsdEurConverter(CurrencyConverter):
    """Конвертер USD → EUR."""

    @property
    def target_currency(self) -> str:
        return "EUR"