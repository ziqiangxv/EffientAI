# -*- coding: utf-8 -*-

''''''

import abc

class ImageSampleInterface(abc.ABC):
    ''''''

    @abc.abstractmethod
    def __call__(self) -> bool:
        ''''''

