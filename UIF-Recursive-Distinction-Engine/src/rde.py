"""UIF Recursive Distinction Engine — minimal executable prototype.

This is a conceptual simulation. It is not a physical model of consciousness
or cosmology.
"""

from dataclasses import dataclass, field
import random
from typing import Callable, List, Tuple


@dataclass
class State:
    values: List[int]


Lens = Callable[[State, int], bool]


@dataclass
class Observer:
    position: int
    lens: Lens
    observations: int = 0

    def observe(self, state: State) -> bool:
        result = self.lens(state, self.position)
        self.observations += 1
        return result


def difference_lens(state: State, position: int) -> bool:
    """Detect a distinction between adjacent state values."""
    if position < 0 or position >= len(state.values) - 1:
        return False
    return state.values[position] != state.values[position + 1]


def distinguish(state: State) -> List[Tuple[int, int, int]]:
    """Return all adjacent distinctions currently present in the state."""
    return [
        (i, state.values[i], state.values[i + 1])
        for i in range(len(state.values) - 1)
        if state.values[i] != state.values[i + 1]
    ]


@dataclass
class Universe:
    state: State = field(default_factory=lambda: State([random.randint(0, 1) for _ in range(10)]))
    observers: List[Observer] = field(default_factory=list)
    step_count: int = 0

    def step(self) -> None:
        distinctions = distinguish(self.state)

        # Δ → Ω: each newly detected boundary can establish an observer.
        existing_positions = {o.position for o in self.observers}
        for position, _, _ in distinctions:
            if position not in existing_positions:
                self.observers.append(Observer(position, difference_lens))

        # Ω(Σ) → Δ': observation contributes a new state element.
        additions = sum(observer.observe(self.state) for observer in self.observers)
        self.state.values.extend(random.randint(0, 1) for _ in range(additions))
        self.step_count += 1

    def run(self, steps: int = 10) -> None:
        for _ in range(steps):
            self.step()
            print(
                f"step={self.step_count:02d} "
                f"state_size={len(self.state.values):03d} "
                f"observers={len(self.observers):03d}"
            )


if __name__ == "__main__":
    Universe().run(15)
