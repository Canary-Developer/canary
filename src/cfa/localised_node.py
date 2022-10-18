from ts import Node
from .cfa_node import CFANode

class LocalisedNode(CFANode):
    def __init__(self, node: Node, location: str = None) -> None:
        self.location: str = location
        super().__init__(node)

    def __str__(self) -> str:
        # loc. X visitied Y times
        # Ln. 14-15, Col. 7-42
        # 1 candidate
        # 1 killed / 12 survived = #.##
        # "some code"
        
        text = f'BB loc. {self.location} '
        if hasattr(self, "amount_visited"):
            text += f'visited {self.amount_visited} times'
        text += '\n'

        start = self.node.start_point
        end = self.node.end_point
        text += f'Ln. {start.line}-{end.line}, Col. {start.char}-{end.char}\n'

        if hasattr(self, "amount_of_candidates"):
            text += f"{self.amount_of_candidates} candidates\n"

        if hasattr(self, "amount_killed") and hasattr(self, "amount_survived"):
            total_mutations = self.amount_survived + self.amount_killed
            if total_mutations > 0:
                mutation_score = self.amount_killed / total_mutations
                mutation_score_str = "{:.2f}".format(mutation_score)
                text += f"MS. {self.amount_killed} of {total_mutations} killed = {mutation_score_str}\n"

        return f'{text}'
