from typing import Protocol, runtime_checkable

# TODO: rewrite with abc?
@runtime_checkable
class Patternable(Protocol):
    def get_val(self, beat_count: int) -> None:
        """return value at beat_count beat"""
