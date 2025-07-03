#!/usr/bin/env python3
# hex_converter.py

def text_to_hex(text: str) -> str:
    """Convert a string to its UTF-8 hex representation."""
    return text.encode("utf-8").hex()

def main():
    print("Text2Hex Classic by Epicinver")
    user_input = input("Enter text to convert: ")
    hex_output = text_to_hex(user_input)
    print(f"Hex result: {hex_output}")
    input("Press Enter to exit...")  # Keep console open

if __name__ == "__main__":
    main()
