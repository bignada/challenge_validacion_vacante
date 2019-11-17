from typing import List


class Disambiguation:
    subtype: List[str]

    def __init__(self, subtype: List[str]) -> None:
        self.subtype = subtype


class ModelFind:
    type: str
    text: str
    count: int
    confidence: float

    def __init__(self, type: str, text: str, count: int, confidence: float) -> None:
        self.type = type
        self.text = text
        self.count = count
        self.confidence = confidence
