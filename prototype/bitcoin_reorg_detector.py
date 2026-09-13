#!/usr/bin/env python3
"""Toy detector for competing Bitcoin chain tips."""

def common_ancestor(chain_a: list[str], chain_b: list[str]) -> str | None:
    for block in reversed(chain_a):
        if block in chain_b:
            return block
    return None

if __name__ == "__main__":
    print(common_ancestor(["g", "a", "b"], ["g", "a", "c"]))
