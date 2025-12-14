"""Simple electrical circuit solver (nodal analysis) without external dependencies.

Supports resistors and ideal DC voltage sources tied to ground (fixed node voltages).
This is intentionally minimal for unit testing and demonstrations.
"""
from typing import Dict, List, Tuple


class Circuit:
    def __init__(self, ground: str = "0") -> None:
        self.ground = ground
        self.nodes = {ground}
        self.resistors: List[Tuple[str, str, float]] = []
        self.fixed: Dict[str, float] = {ground: 0.0}

    def add_resistor(self, n1: str, n2: str, resistance_ohm: float) -> None:
        if resistance_ohm <= 0:
            raise ValueError("Resistance must be positive")
        self.nodes.add(n1)
        self.nodes.add(n2)
        self.resistors.append((n1, n2, float(resistance_ohm)))

    def add_voltage_source(self, node: str, voltage: float) -> None:
        self.nodes.add(node)
        self.fixed[node] = float(voltage)

    def solve(self) -> Dict[str, float]:
        # Unknown nodes are nodes without fixed voltages
        unknowns = [n for n in sorted(self.nodes) if n not in self.fixed]
        n = len(unknowns)
        if n == 0:
            return dict(self.fixed)

        # Map node to index
        idx = {node: i for i, node in enumerate(unknowns)}
        # Initialize conductance matrix G and current vector I (Ax = b where A=G)
        G = [[0.0 for _ in range(n)] for _ in range(n)]
        I = [0.0 for _ in range(n)]

        # For each resistor, stamp into G and I
        for a, b, R in self.resistors:
            g = 1.0 / R
            a_fixed = a in self.fixed
            b_fixed = b in self.fixed
            if not a_fixed and not b_fixed:
                ia = idx[a]
                ib = idx[b]
                G[ia][ia] += g
                G[ib][ib] += g
                G[ia][ib] -= g
                G[ib][ia] -= g
            else:
                # If one side is fixed, move contribution to I
                if not a_fixed and b_fixed:
                    ia = idx[a]
                    G[ia][ia] += g
                    I[ia] += g * self.fixed[b]
                elif a_fixed and not b_fixed:
                    ib = idx[b]
                    G[ib][ib] += g
                    I[ib] += g * self.fixed[a]
                else:
                    # both fixed: nothing to solve (could be used for consistency check)
                    pass

        # Solve linear system G x = I for x (unknown node voltages)
        x = _solve_linear_system(G, I)

        # Build result combining fixed and solved unknowns
        res = dict(self.fixed)
        for node, i in idx.items():
            res[node] = x[i]
        return res


def _solve_linear_system(A: List[List[float]], b: List[float]) -> List[float]:
    # Simple Gaussian elimination with partial pivoting
    n = len(b)
    # Convert to augmented matrix
    M = [row[:] + [b_i] for row, b_i in zip(A, b)]

    for k in range(n):
        # Find pivot
        piv = max(range(k, n), key=lambda i: abs(M[i][k]))
        if abs(M[piv][k]) < 1e-12:
            raise ValueError("Singular matrix or ill-conditioned circuit")
        # Swap
        if piv != k:
            M[k], M[piv] = M[piv], M[k]
        # Normalize and eliminate
        pivot_val = M[k][k]
        for j in range(k, n + 1):
            M[k][j] /= pivot_val
        for i in range(n):
            if i == k:
                continue
            factor = M[i][k]
            if factor == 0.0:
                continue
            for j in range(k, n + 1):
                M[i][j] -= factor * M[k][j]

    # Extract solution
    return [M[i][n] for i in range(n)]
