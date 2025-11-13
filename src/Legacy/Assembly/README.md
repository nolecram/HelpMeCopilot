# Assembly Language Examples

This directory contains x86 Assembly language examples demonstrating low-level programming concepts.

## Files

### 1-x86.asm
A DOS COM file that calculates Fibonacci numbers using assembly language.

**Features:**
- Calculates up to 15,000 terms of the Fibonacci sequence
- Uses ASCII BCD (Binary Coded Decimal) arithmetic
- Demonstrates low-level memory manipulation
- Direct DOS interrupt calls (INT 21h)
- String and numeric output routines

**Key Concepts Demonstrated:**
- **BCD Arithmetic**: Addition using ASCII BCD representation
- **Memory Management**: Direct memory access and manipulation
- **String Operations**: Custom string and number printing routines
- **DOS System Calls**: File handle operations via interrupts
- **Loop Optimization**: Efficient counting and iteration
- **Register Usage**: x86 register operations (AX, DI, SI, CX, BP, etc.)

**Functions:**
- `AddNumbers` - BCD addition with carry handling
- `PrintLine` - Formatted output with counter
- `PrintNumericString` - Number to string conversion and output
- `PrintString` - Raw string output to stdout
- `IncrementCount` - Counter increment in BCD
- `CRLF` - Carriage return/line feed output

## Purpose

This example demonstrates:
- Low-level programming without standard libraries
- Direct hardware/OS interaction
- Efficient algorithms in constrained environments
- Classic DOS programming techniques

## Usage

This is a DOS COM file designed to run in a DOS or DOS-compatible environment:

```
1-x86.com
```

To assemble (using NASM or similar):
```bash
nasm -f bin 1-x86.asm -o 1-x86.com
```

## Educational Value

This code is valuable for:
- Understanding computer architecture fundamentals
- Learning how high-level operations map to assembly
- Appreciating modern programming conveniences
- Studying optimization techniques

## Note

This code targets 16-bit x86 DOS systems and won't run directly on modern 64-bit operating systems without an emulator like DOSBox.
