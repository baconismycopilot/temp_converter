"""Convert temperatures between units."""


def celsius_to_fahrenheit(temperature: float) -> float:
    return (temperature * 9 / 5) + 32


def celsius_to_kelvin(temperature: float) -> float:
    return temperature + 273.15


def fahrenheit_to_celsius(temperature: float) -> float:
    return (temperature - 32) / 1.8


def fahrenheit_to_kelvin(temperature: float) -> float:
    return (temperature - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(temperature: float) -> float:
    return temperature - 273.15


def kelvin_to_fahrenheit(temperature: float) -> float:
    return (temperature - 273.15) * 9 / 5 + 32
