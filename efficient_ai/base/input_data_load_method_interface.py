# -*- coding: utf-8 -*-

''''''

import abc

import typing

class InputDataLoadMethodInterface(abc.ABC):
    ''''''

    @abc.abstractmethod
    def __call__(self) -> typing.Any:
        ''''''

