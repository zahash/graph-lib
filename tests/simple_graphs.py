from typing import *


class SimpleBinaryGridGraph:
    Position = Tuple[int, int]
    BinaryMatrix = List[List[bool]]
    Matrix = List[List[int]]

    def __init__(self, grid: BinaryMatrix):
        self._grid = grid

    @classmethod
    def from_default_grid(cls):
        return cls(cls._to_binary([
            [1, 0, 0],
            [1, 1, 1],
            [0, 1, 1]
        ]))

    @classmethod
    def from_integer_grid(cls, grid: Matrix):
        return cls(cls._to_binary(grid))

    @staticmethod
    def _to_binary(grid: Matrix):
        binary_grid = [[False for _ in range(len(grid[r]))] for r in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                binary_grid[r][c] = bool(grid[r][c])
        return binary_grid

    def _valid_pos(self, position: Position):
        r, c = position
        return 0 <= r < len(self._grid) and 0 <= c < len(self._grid[r]) and self._grid[r][c]

    @staticmethod
    def always_empty_successor(_: Position) -> Iterable[Position]:
        return iter(())

    def grid_successor(self, position: Position) -> Iterable[Position]:
        r, c = position
        for r, c in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if self._valid_pos((r, c)):
                yield r, c


class SimpleDictGraph:
    def __init__(self, graph: dict):
        self._graph = graph

    def successors(self, node: str) -> List[str]:
        return self._graph.get(node, [])
