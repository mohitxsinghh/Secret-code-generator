# Secret code generator

# Secret Code Generator

## Overview

The **Secret Code Generator** is a Python-based program that allows users to encode and decode messages using a simple Caesar cipher. The Caesar cipher shifts each letter in a message by a specified number of positions in the alphabet. This program provides an interactive menu where users can choose to encode or decode messages with a customizable shift value.

## Features

- **Encoding**: Encrypt a message by shifting its letters forward in the alphabet.
- **Decoding**: Decrypt a message by shifting its letters backward using the same shift value.
- Handles both uppercase and lowercase letters.
- Non-alphabet characters (e.g., numbers, punctuation) remain unchanged.
- Simple and intuitive menu interface for user interaction.

## How It Works

### 1. **Encoding a Message**

The `encode_message()` function takes two inputs:
- `message`: The string to be encoded.
- `shift`: The number of positions to shift each letter in the message.

The function shifts each letter by the specified amount, wrapping around the alphabet if necessary (e.g., shifting 'Z' by 1 results in 'A').

### 2. **Decoding a Message**

The `decode_message()` function uses the same logic as encoding but shifts the characters in the opposite direction by applying the negative of the given shift value.

### 3. **Menu Interface**

The program provides a simple menu that allows users to:
- Encode a message.
- Decode a message.
- Exit the program.

### Example Usage

```bash
Secret Code Generator
1. Encode a message
2. Decode a message
3. Exit

