from typing import TypedDict


class ModelData(TypedDict):
    company: str
    architecture: str
    modality: list[str]
    tasks: list[str]
    parameters: str
    release_year: int
