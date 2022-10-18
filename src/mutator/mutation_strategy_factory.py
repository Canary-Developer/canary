from ts import Parser
from .mutation_strategy import *
from .composite_strategy import *
from .obom_strategy import *
from .abs_stategy import *
from .aor_strategy import *
from .lcr_strategy import *
from .ror_strategy import *
from .uoi_strategy import *

class MutationStrategyFactory():
    def __init__(self) -> None:
        pass

    def create(
        self,
        name: str,
        parser: Parser,
    ) -> MutationStrategy:
        composition: List[MutationStrategy] = list()
        for n in name.split():
            if n == "obom": composition.append(ObomStrategy(parser))
            elif n == "abs": composition.append(AbsStrategy(parser))
            elif n == "aor": composition.append(AorStrategy(parser))
            elif n == "lcr": composition.append(LcrStrategy(parser))
            elif n == "ror": composition.append(RorStrategy(parser))
            elif n == "uoi": composition.append(UoiStrategy(parser))
        if len(composition) == 1: return composition[0]
        return CompositeStrategy(composition)