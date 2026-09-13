#!/usr/bin/env python3
"""Toy domain separation for ZK commitments."""

from hashlib import sha256

def domain_hash(domain: str, statement: str, payload: bytes) -> str:
    if not domain or not statement:
        raise ValueError("domain and statement are required")
    return sha256((domain + "|" + statement).encode() + payload).hexdigest()

if __name__ == "__main__":
    print(domain_hash("zk-demo/v1", "balance", b"proof"))
