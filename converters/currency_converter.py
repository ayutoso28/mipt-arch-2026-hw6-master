from abc import ABC, abstractmethod
import requests
import logging
import time


class CurrencyConverter(ABC):
    """Базовый класс для конвертации из USD в целевую валюту."""

    API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

    def __init__(self, max_retries: int = 3, retry_delay: float = 2, timeout: int = 10):
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.timeout = timeout
        self.logger = logging.getLogger(self.__class__.__name__)
        self.rates = self._fetch_rates()

    def _fetch_rates(self) -> dict | None:
        """Загружает курсы валют с API с retry-логикой."""
        for attempt in range(self.max_retries):
            try:
                response = requests.get(self.API_URL, timeout=self.timeout)
                response.raise_for_status()
                return response.json()['rates']
            except requests.exceptions.RequestException as e:
                self.logger.error(
                    "Request failed (attempt %d/%d): %s",
                    attempt + 1, self.max_retries, e,
                )
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
            except (ValueError, KeyError) as e:
                self.logger.error("Error processing response: %s", e)
                return None
        self.logger.error("Max retries reached. Unable to fetch rates.")
        return None

    @property
    @abstractmethod
    def target_currency(self) -> str:
        """Код целевой валюты, например 'EUR'."""
        ...

    def convert(self, amount: float) -> float:
        """Конвертирует amount USD в целевую валюту."""
        if self.rates is None:
            raise RuntimeError("Exchange rates unavailable")
        return amount * self.rates[self.target_currency]