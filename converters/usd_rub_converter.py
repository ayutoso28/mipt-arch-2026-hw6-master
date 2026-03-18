from converters.currency_converter import CurrencyConverter


class UsdRubConverter(CurrencyConverter):
    """Конвертер USD → RUB."""

    @property
    def target_currency(self) -> str:
        return "RUB"