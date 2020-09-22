import os
from os import path
from typing import Dict, Generator


class GenericInputData:
    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path

    def read(self) -> str:
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config: dict) -> Generator:
        raise NotImplementedError


class PathInputData(GenericInputData):
    @classmethod
    def generate_inputs(cls, config: dict) -> Generator:
        data_dir = config["data_dir"]
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker:
    def __init__(self, input_data) -> None:
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_cls: GenericInputData, config: dict):
        workers = []
        for input_data in input_cls.generate_inputs(config):
            workers.append(cls(input_data))
        return workers
