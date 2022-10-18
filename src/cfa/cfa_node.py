from random import random
from ts import Node

class CFANode:
    def __init__(self, node: Node) -> None:
        self.node = node

    def __str__(self) -> str:
        # Ln. 14-15, Col. 7-42
        if self.node is None: return f'None {random()}'
        start = self.node.start_point
        end = self.node.end_point
        text = f'Ln. {start.line}-{end.line}, Col. {start.char}-{end.char}\n'
        return text