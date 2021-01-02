from dataclasses import dataclass
from typing import List


@dataclass
class Level:
    """ Contain data for level including duration """

    name: str
    frames: int
    difficulty: int
    enter: str
    exit: str
    notes: str = ""
    granted_item: str = ""


@dataclass
class Node:
    level: Level
    prerequisites: List
    required: bool = False


@dataclass
class Graph:
    nodes: List[Node]
