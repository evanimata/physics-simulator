"""Fundamental physics equations with classes."""

class System:
    def __init__(self, allowed_values: list, **kwargs) -> None:
        """Define an initial system."""
        for key, value in kwargs.items():
            if key not in allowed_values:
                raise(ValueError, f"Value {key} not allowed.")
            setattr(self, key, value)


class Gravitational(System):
    allowed_values = ["mass", "acceleration", ]

    def __init__(self, **kwargs) -> None:
        """Define a system with gravitational properties."""
        super().__init__(self.allowed_values, **kwargs)
