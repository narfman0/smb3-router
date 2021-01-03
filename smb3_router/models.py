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
    previous_nodes: List
    next_nodes: List
    required: bool = False


@dataclass
class Graph:
    nodes: List[Node]
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