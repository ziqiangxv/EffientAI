# -*- coding: utf-8 -*-

''''''

from dataclasses import dataclass

@dataclass
class IdBase:
    ''''''

    name: str

    version: str

    def __str__(self) -> str:
        ''''''

        return f'{self.name}##{self.version}'

# @dataclass
# class StudyId(IdBase):
#     ''''''

#     path: str

# @dataclass
# class PassId(IdBase):
#     ''''''

# @dataclass
# class TrainId(IdBase):
#     ''''''

# @dataclass
# class TestId(IdBase):
#     ''''''

# @dataclass
# class InferId(IdBase):
#     ''''''

