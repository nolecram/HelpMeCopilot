# C Language Examples

This directory contains C programming examples demonstrating POSIX threading and system programming.

## Files

### Posix.c
A C program demonstrating POSIX thread (pthread) usage and testing.

**Features:**
- Multi-threaded programming with pthreads
- Thread creation and synchronization
- Thread status verification with assertions
- Function pointer passing to threads

**Key Concepts Demonstrated:**
- **POSIX Threads**: Creating and managing multiple threads
- **Thread Joining**: Waiting for thread completion with `pthread_join()`
- **Thread Arguments**: Passing data to thread functions
- **Return Values**: Capturing thread return status
- **Assertions**: Testing thread behavior with `assert()`

**Functions:**
- `CEPSXT1(void *)` - Thread worker function (implementation not shown)
- `test_CEPSXT1()` - Test harness for multi-threaded execution
- `main()` - Entry point that runs the tests

**Dependencies:**
- `pthread.h` - POSIX thread library
- `assert.h` - Assertion testing
- `stdio.h`, `stdlib.h`, `string.h`, `unistd.h`, `errno.h` - Standard C libraries

## Purpose

This example demonstrates:
- Concurrent programming in C
- Thread-safe code design
- Testing multi-threaded applications
- POSIX API usage

## Compilation

To compile this program:

```bash
gcc -pthread -o posix_test Posix.c
```

The `-pthread` flag is required to link the POSIX thread library.

## Usage

Run the compiled program:

```bash
./posix_test
```

Expected output:
```
All tests passed.
```

## Educational Value

This code is valuable for:
- Learning concurrent programming concepts
- Understanding thread creation and management
- Practicing multi-threaded testing techniques
- Exploring POSIX standard APIs

## Note

This code requires a POSIX-compliant system (Linux, macOS, Unix) and will not compile on Windows without additional libraries like Cygwin or MinGW with pthread support.
