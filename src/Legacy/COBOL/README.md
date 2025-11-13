# COBOL Examples

This directory contains COBOL programming examples demonstrating mainframe Language Environment callable services.

## Files

### CEEFunctions.cobol
A COBOL program demonstrating IBM Language Environment (LE) callable services.

**Features:**
- Language Environment callable service integration
- Date and time manipulation using LE services
- Message formatting and output
- Structured COBOL programming with divisions

**Key Concepts Demonstrated:**
- **Callable Services**: Using IBM LE services (CEEMOUT, CEELOCT, CEEDATE)
- **Date/Time Handling**: Working with Lilian date format and Gregorian dates
- **Data Structures**: Working-Storage declarations and COPY statements
- **Error Handling**: Feedback code processing
- **Pattern Formatting**: Custom date output formatting

**Language Environment Services Used:**
- `CEEMOUT` - Message output service
- `CEELOCT` - Local date/time retrieval
- `CEEDATE` - Date conversion service

**Data Structures:**
- `Feedback` - Standard LE feedback code structure (CEEIGZCT copybook)
- `Pattern` - Date formatting pattern string
- `Msg` - Variable-length message structure
- `Lildate` - Lilian date (integer day count)
- `Greg` - Gregorian date string

**Program Structure:**
- **Identification Division**: Program metadata (AWIXMP)
- **Data Division**: Variable declarations and working storage
- **Procedure Division**: Executable logic (000-Main-Logic)

## Purpose

This example demonstrates:
- Enterprise mainframe programming
- IBM Language Environment integration
- COBOL data handling and formatting
- Standard mainframe design patterns

## Compilation

On IBM mainframe systems (z/OS):

```jcl
// EXEC IGYWC,PARM='LIB'
//COBOL.SYSLIB DD DSN=CEE.SCEESAMP,DISP=SHR
```

Or using modern COBOL compilers:

```bash
cob -x CEEFunctions.cobol
```

## Usage

Execute on mainframe or compatible COBOL environment:

```
AWIXMP
```

Expected output shows current date formatted with the pattern:
```
Callable Service example starting.
Today is [Day of Week], [Month] [Day], [Year].
Callable Service example ending.
```

## Educational Value

This code is valuable for:
- Understanding mainframe programming
- Learning COBOL language syntax and structure
- Working with enterprise callable services
- Maintaining legacy business systems

## Context

COBOL remains critical in:
- Banking and financial systems
- Insurance processing
- Government applications
- Large-scale transaction processing

## Note

This code requires an IBM COBOL compiler with Language Environment support, typically found on z/OS mainframe systems or compatible environments.
