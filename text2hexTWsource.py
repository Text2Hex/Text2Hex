#!/usr/bin/env python3
# hex_converter.py

def text_to_hex(text: str) -> str:
    return text.encode("utf-8").hex()

def hex_to_text(hex_str: str) -> str:
    return bytes.fromhex(hex_str).decode("utf-8")

def main():
    print("Text2Hex 2Way Console Edition by Epicinver")
    choice = input("Choose conversion (1) Text to Hex, (2) Hex to Text: ")
    if choice == "1":
        user_input = input("Enter text to convert: ")
        print("Hex result:", text_to_hex(user_input))
    elif choice == "2":
        user_input = input("Enter hex to convert: ")
        try:
            print("Text result:", hex_to_text(user_input))
        except Exception as e:
            print("Error decoding hex:", e)
    else:
        print("Invalid choice")

    input("Press Enter to exit...")  # Pause at the very end

if __name__ == "__main__":
    main()
