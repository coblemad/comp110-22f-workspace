"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730544275"


class Simpy:
    """A simpler, single dimension implementation of many of the same capacities of NumPy."""
    values: list[float]

    def __init__(self, num_list: list[float]):
        """Simpy Constructor to initialize values of newly constructed Simply object to argument passed in."""
        self.values = num_list
    
    def __repr__(self) -> str:
        """Automatically called when a Simpy object is converted into a str."""
        return f"Simpy({self.values})"
    
    def fill(self, float_value: float, int_value: int) -> None:
        """Mutates the object the method is called on."""
        i: int = 0
        self.values = []
        while len(self.values) < int_value:
            self.values.append(float_value)
            i += 1
    
    def arrange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in values attribute with a range of values."""
        assert step != 0.0
        result_list: Simpy = self
        up_step: float = ((start) + (step))
        result_list.values.append(start)
        while up_step != stop:
            result_list.values.append(up_step)
            up_step = ((up_step) + (step))
        return result_list

    def sum(self)-> float: 
        """Sum the values in the Simpy class."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Add rhs using the addition operator."""
        result_val: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            i: int = 0
            for item in rhs.values:
                result_val.values.append(item + (self.values[i]))
                i += 1
        else:
            for item in self.valuesresult.values.append(item + rhs)
        return result_val

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Power operator for Simpy."""
        result_val: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            i: int = 0
            for item in rhs.values:
                result_val.values.append((self.values[i]) ** item)
                i += 1
        else:
            for item in self.values:
                result_val.values.append(item ** rhs)
        return result_val

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Eq operator overload for ==."""
        result_val: list[bool] = []
        if isinstance(rhs, Simpy):
            i: int = 0
            for item in self.values:
                if item == rhs.values[i]:
                    result_val.append(True)
                    i += 1
                else:
                    result_val.append(False)
                    i += 1
        else:
            for item in self.values:
                if item == rhs:
                    result_val.append(True)
                else:
                    result_val.append(False)
        return result_val
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """gt operator overload for >."""
        result_val: list[bool] = []
        if isinstance(rhs, Simpy):
            i: int = 0
            for item in self.values:
                if item > rhs.values[i]:
                    result_val.append(True)
                    i += 1
                else:
                    result_val.append(False)
                    i += 1
        else:
            for item in self.values:
                if item > rhs:
                    result_val.append(True)
                else:
                    result_val.append(False)
        return result_val
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription notation with the getitem operator overload."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            if isinstance(rhs, list):
                new_list: Simpy = Simpy([])
                for item in range(len(rhs)):
                    if rhs[item]:
                        new_list.values.append(self.values[item])
                return new_list