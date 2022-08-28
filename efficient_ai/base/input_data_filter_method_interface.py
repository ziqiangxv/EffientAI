# -*- coding: utf-8 -*-

''''''

import abc

class InputDataFilterMethodInterface(abc.ABC):
    ''''''

    @abc.abstractmethod
    def __call__(self) -> bool:
        ''''''

