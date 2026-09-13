#!/usr/bin/env python3
"""Toy Bitcoin fee estimator based on virtual weight."""

from dataclasses import dataclass

@dataclass
class FeeQuote:
    vbytes: int
    sat_per_vbyte: int

    @property
    def total_sats(self) -> int:
        return self.vbytes * self.sat_per_vbyte

def quote(vbytes: int, sat_per_vbyte: int) -> FeeQuote:
    if vbytes <= 0 or sat_per_vbyte < 0:
        raise ValueError("vbytes must be positive and fee rate non-negative")
    return FeeQuote(vbytes, sat_per_vbyte)

if __name__ == "__main__":
    print(quote(140, 12).total_sats)
