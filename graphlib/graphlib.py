from typing import *
from collections import deque
from functools import partial

T = TypeVar("T")


class TraceNode:
    def __init__(self, value: T, steps: int, parent: Optional["TraceNode"]):
        self.value = value
        self.steps = steps
        self.parent = parent

    def __eq__(self, other: "TraceNode"):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return (f"<{self.__class__.__qualname__} "
                f"value={self.value!r} "
                f"steps={self.steps!r} "
                f"parent={(self.parent.value if self.parent else None)!r}"
                ">")


def _traverse(pop_fn: Callable[[deque], T], start: Generic[T], successors: Callable[[T], Iterable[T]]) -> Iterable[T]:
    frontier = deque([start])
    seen = set()

    while frontier:
        node = pop_fn(frontier)
        if node in seen:
            continue
        yield node
        seen.add(node)
        for successor in successors(node):
            frontier.append(successor)


bft = partial(_traverse, pop_fn=lambda frontier: frontier.popleft())
dft = partial(_traverse, pop_fn=lambda frontier: frontier.pop())


def _traced_traverse(pop_fn: Callable[[deque], TraceNode], start: Generic[T],
                     successors: Callable[[T], Iterable[T]]) \
        -> Iterable[TraceNode]:
    frontier = deque([TraceNode(value=start, steps=0, parent=None)])
    seen: Set[TraceNode] = set()

    while frontier:
        node = pop_fn(frontier)
        if node in seen:
            continue
        yield node
        seen.add(node)
        for successor in successors(node.value):
            frontier.append(TraceNode(value=successor, steps=node.steps + 1, parent=node))


traced_bft = partial(_traced_traverse, pop_fn=lambda frontier: frontier.popleft())
traced_dft = partial(_traced_traverse, pop_fn=lambda frontier: frontier.pop())
