# -*- coding: utf-8 -*-

''''''

from __future__ import annotations

import typing

from dataclasses import dataclass

from enum import Enum

from .base.option_base import OptionBase

from .base.input_data_filter_method_interface import InputDataFilterMethodInterface

from .base.input_data_type import InputDataType

class TrainMode(Enum):
    ''''''
 
    TRAIN = 0

    CROSS_VALIDATION = 1

class 

@dataclass
class TrainOption(OptionBase):
    ''''''


    @staticmethod
    def load(yaml_path: str) -> TrainOption:
        ''''''

    train_mode: TrainMode = TrainMode.CROSS_VALIDATION

    input_data_path: str = ''

    input_data_filter: InputDataType = InputDataType.NII_GZ

    input_data_filter_method: typing.Optional[InputDataFilterMethodInterface] = None

    # input_data_filter_method_py_path: str = ''

    input_data_ratio_for_train: float = 0.8

    input_data_selection_mode_for_train: str = ''

