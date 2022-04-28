from pydantic import validator
from dataclasses import dataclass


@dataclass
class Vehicle:
    name: str
    age: int
    note: int

    @validator('note')
    def validate_note(cls, value, field):
        if value < 1 or value > 10:
            raise RuntimeError(f'{field.name} must be between 1 and 10')
        return value


if __name__ == '__main__':
    v1 = Vehicle(name='fiat', age=50, note=15)
