#!/usr/bin/env python3
"""Small Bitcoin Script opcode trace for educational inspection."""

OPCODES = {0x00: "OP_0", 0x51: "OP_1", 0x76: "OP_DUP", 0x87: "OP_EQUAL", 0x88: "OP_EQUALVERIFY"}

def trace(script: bytes) -> list[str]:
    return [OPCODES.get(byte, f"PUSH_OR_UNKNOWN(0x{byte:02x})") for byte in script]

if __name__ == "__main__":
    print(trace(bytes([0x76, 0x51, 0x88])))
