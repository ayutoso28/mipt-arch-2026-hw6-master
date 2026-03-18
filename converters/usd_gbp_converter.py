from converters.currency_converter import CurrencyConverter


class UsdGbpConverter(CurrencyConverter):
    """Конвертер USD → GBP."""

    @property
    def target_currency(self) -> str:
        return "GBP"