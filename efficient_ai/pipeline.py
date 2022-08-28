# -*- coding: utf-8 -*-

''''''

import abc

import typing

import os

from pathlib import Path

from overrides import EnforceOverrides

import monai.transforms

import monai.utils

import monai.data

import glob

import torch

class PipelineBase(EnforceOverrides):
    ''''''

    def __init__(
        self,
        data_dir: str,
        label_dir: str,
        out_dir: str,
        net_name: typing.Optional[str] = None,
        loss_name: typing.Optional[str] = None,
        data_suffix: str = '*',
        label_suffix: str = '*',
        random_seed = 0
    ) -> None:
        ''''''

        if not Path(data_dir).exists():
            raise FileNotFoundError(f'{data_dir} not exists')

        if not Path(data_dir).is_dir():
            raise NotADirectoryError(f'{data_dir} is not directory')

        if not Path(label_dir).exists():
            raise FileNotFoundError(f'{label_dir} not exists')

        if not Path(out_dir).is_dir():
            raise NotADirectoryError(f'{label_dir} is not directory')

        if not Path(out_dir).is_dir():
            raise NotADirectoryError(f'{out_dir} is not directory')

        if not Path(out_dir).exists():
            Path(out_dir).mkdir(parents=True)

        if data_dir == label_dir:
            if data_suffix is None or label_suffix is None:
                raise ValueError('data_suffix and label_suffix cannot be None while data_dir is same as label_dir')

        self._data_dir = data_dir
        self._label_dir = label_dir
        self._out_dir = out_dir
        self._data_suffix = data_suffix
        self._label_suffix = label_suffix
        self._net_name = net_name
        self._loss_name = loss_name
        self._random_seed = random_seed

        # assert net.lower() == 'unet'
        # assert optimizer.lower() == 'adam'

        image_paths = sorted(glob.glob(os.path.join(data_dir, self._data_suffix)))
        label_paths = sorted(glob.glob(os.path.join(data_dir, self._label_suffix)))

        if not image_paths or not label_paths:
            raise ValueError(f'there is no images or labels in data_dir({data_dir}) and label_dir({label_dir}) ' + \
                            'with given data_suffix({data_suffix}) and label_suffix({label_suffix})')

        monai.utils.set_determinism(self._random_seed)

        self._image_data_key = 'image'
        self._label_data_key = 'label'

        self._data_dicts = [
                        {self._image_data_key: image_name, self._label_data_key: label_name}
                        for image_name, label_name in zip(image_paths, label_paths)
                    ]

    def data_filter(self, data_path: str, label_path: str) -> bool:
        ''''''

        return True

    def train_transforms(self) -> monai.transforms.Compose:
        ''''''

        return monai.transforms.Compose(
                [
                    monai.transforms.LoadImaged(keys=[self._image_data_key, self._label_data_key]),
                    monai.transforms.EnsureChannelFirstd(keys=[self._image_data_key, self._label_data_key]),
                    monai.transforms.Orientationd(keys=[self._image_data_key, self._label_data_key], axcodes="RAS"),
                    monai.transforms.Spacingd(
                        keys=[self._image_data_key, self._label_data_key], 
                        pixdim=(1.5, 1.5, 2.0), 
                        mode=("bilinear", "nearest")
                    ),
                    monai.transforms.ScaleIntensityRanged(
                        keys=[self._image_data_key], a_min=-57, a_max=164,
                        b_min=0.0, b_max=1.0, clip=True,
                    ),
                ]
            )

    def validate_transform(self) -> monai.transforms.Compose:
        ''''''

        return monai.transforms.Compose(
                [
                    monai.transforms.LoadImaged(keys=[self._image_data_key, self._label_data_key]),
                    monai.transforms.EnsureChannelFirstd(keys=[self._image_data_key, self._label_data_key]),
                    monai.transforms.Orientationd(keys=[self._image_data_key, self._label_data_key], axcodes="RAS"),
                    monai.transforms.Spacingd(
                        keys=[self._image_data_key, self._label_data_key], 
                        pixdim=(1.5, 1.5, 2.0), 
                        mode=("bilinear", "nearest")
                    ),
                    monai.transforms.ScaleIntensityRanged(
                        keys=[self._image_data_key], a_min=-57, a_max=164,
                        b_min=0.0, b_max=1.0, clip=True,
                    ),
                ]
            )

    def add_tranform(self, callable: typing.Callable) -> None:
        ''''''

    def set_net(self) -> None:
        ''''''

    def update_net(self, net) -> None:
        ''''''

    def update_optimizer(self, optimizer) -> None:
        ''''''

    def update_loss(self, loss) -> None:
        ''''''

    def train(
        self,
        train_mode: str,
        optimizer: str,
        data_ratio_for_train: float,
        batch_size: int,
        max_epoch: int,
        num_workers: int = 4,
        shuffle: bool = True,
        device: str = 'cuda:0'
    ) -> None:
        ''''''

        data_dicts = [
                        dc for dc in self._data_dicts \
                        if self.data_filter(dc[self._image_data_key], dc[self._label_data_key])
                    ]

        train_sample_num = int(len(data_dicts) * data_ratio_for_train)
        train_files, val_files = data_dicts[:train_sample_num], data_dicts[train_sample_num:]

        train_dataset = monai.data.CacheDataset(
                            data=train_files,
                            transform=self.train_transforms(),
                            cache_rate=1.0,
                            num_workers=4
                        )

        validate_dataset = monai.data.CacheDataset(
                            data=val_files,
                            transform=self.validate_transform(),
                            cache_rate=1.0,
                            num_workers=4
                        )

        train_loader = monai.data.DataLoader(
                            train_dataset,
                            batch_size=batch_size,
                            shuffle=shuffle,
                            num_workers=num_workers
                        )

        val_loader = monai.data.DataLoader(validate_dataset, batch_size=1, num_workers=4)

        device = torch.device("cuda:0")




    def test(self) -> None:
        ''''''

    def infer(self) -> None:
        ''''''
    










