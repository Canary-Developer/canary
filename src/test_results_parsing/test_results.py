from typing import Dict
from .test_summary import TestSummary
from instrumentation_trace import Trace

class TestResults():
    def __init__(
        self,
        summary: TestSummary,
        trace: Trace = None
    ) -> None:
        self._summary = summary
        self._trace = trace

    @property
    def summary(self) -> TestSummary:
        return self._summary

    @property
    def trace(self) -> Trace:
        return self._trace
    
    @property
    def visitations(self) -> Dict[str, int]:
        visitations: Dict[str, int] = dict()
        for location in self.trace.sequence:
            if location.id not in visitations:
                visitations[location.id] = 1
            else: visitations[location.id] += 1
        return visitations