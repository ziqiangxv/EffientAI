# -*- coding: utf-8 -*-

''''''

from __future__ import annotations

import abc

from dataclasses import dataclass

@dataclass
class OptionBase(abc.ABC):
    ''''''

    @abc.abstractstaticmethod
    def load(yaml_path: str) -> OptionBase:
        ''''''

        raise NotImplementedError('')

    def save(self, output_dir: str) -> None:
        ''''''

        try:
            pass

        except Exception as e:
            pass


