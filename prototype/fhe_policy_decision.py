#!/usr/bin/env python3
"""Toy separation of identity, policy and FHE result access."""

from dataclasses import dataclass

@dataclass
class Decision:
    subject: str
    operation: str
    allowed: bool
    reason: str

def decide(subject: str, operation: str, allowed_subjects: set[str]) -> Decision:
    allowed = subject in allowed_subjects
    return Decision(subject, operation, allowed, "policy match" if allowed else "not authorized")

if __name__ == "__main__":
    print(decide("service", "decrypt", {"service"}))
