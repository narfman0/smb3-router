from dataclasses import dataclass, field
from enum import Enum
from typing import List


class Item(Enum):
    BOX = 1
    CLOUD = 2
    PWING = 3
    STAR = 4
    WHISTLE = 5
    FIRE = 6
    LEAF = 7
    MUSHROOM = 8

    @staticmethod
    def value_of(value) -> Enum:
        for m, mm in Item.__members__.items():
            if m == value.upper():
                return mm


@dataclass
class Level:
    """ Contain data for level including duration """

    name: str
    frames: int
    difficulty: int
    enter: str
    star: bool
    exit: str
    notes: str = ""
    granted_item: Item = None


@dataclass
class GraphNode:
    level: Level
    previous_nodes: List = field(repr=False)
    next_nodes: List = field(repr=False)
    required: bool = False


@dataclass
class PathNode:
    level: Level
    enter: str
    item_used: Item = None


@dataclass
class Graph:
    nodes: List[GraphNode]
    start_node_name: str = "1-1"
    end_node_name: str = "BC"

    def find_start_node(self):
        for node in self.nodes:
            if node.level.name == self.start_node_name:
                return node

    def find_end_node(self):
        for node in self.nodes:
            if node.level.name == self.end_node_name:
                return node