# Sybase Database Examples

This directory contains C++ examples demonstrating Sybase database operations using DB-Library.

## Files

### DeletingDataSyb.cpp
Demonstrates deleting data from a Sybase database.

**Operations:**
- Database connection initialization
- Login and authentication
- DELETE query execution
- Error handling
- Resource cleanup

### InsertDataSyb.cpp
Demonstrates inserting data into a Sybase database.

**Operations:**
- Record insertion
- Parameter binding
- INSERT query execution
- Transaction handling

### UpdateDataSyb.cpp
Demonstrates updating data in a Sybase database.

**Operations:**
- UPDATE query execution
- Row modification
- Conditional updates

### MultiStepSyb.cpp
Demonstrates complex multi-step database operations.

**Operations:**
- Multiple query execution
- Transaction management
- Result set processing
- Advanced DB-Library features

### RunSQLCommSyb.cpp
Generic SQL command execution utility.

**Operations:**
- Dynamic SQL execution
- Command processing
- Result handling

## Key Concepts

### DB-Library API
All examples use the Sybase DB-Library API:
- `dbinit()` - Initialize DB-Library
- `dblogin()` - Create login record
- `DBSETLUSER()` - Set username
- `DBSETLPWD()` - Set password
- `dbopen()` - Open database connection
- `dbcmd()` - Set SQL command
- `dbsqlexec()` - Execute SQL command
- `dbclose()` - Close connection
- `dbexit()` - Clean up DB-Library

### Error Handling
- Checking return values (FAIL vs. SUCCESS)
- Proper resource cleanup
- Error message reporting

## Prerequisites

### Required Libraries
- Sybase DB-Library headers (`sybfront.h`, `sybdb.h`)
- Sybase client libraries

### Installation
On Linux:
```bash
# Install Sybase Open Client
# Specific installation depends on your distribution
```

## Compilation

Basic compilation:
```bash
g++ -o delete_data DeletingDataSyb.cpp -lsybdb
g++ -o insert_data InsertDataSyb.cpp -lsybdb
g++ -o update_data UpdateDataSyb.cpp -lsybdb
g++ -o multi_step MultiStepSyb.cpp -lsybdb
g++ -o run_sql RunSQLCommSyb.cpp -lsybdb
```

## Usage

### Configuration
Before running, update the connection parameters in each file:
- `username` - Your Sybase username
- `password` - Your Sybase password
- `server` - Sybase server name/address

### Execution
```bash
./delete_data
./insert_data
./update_data
./multi_step
./run_sql
```

## Database Setup

These examples assume a Sybase database with appropriate tables. Example table schema:

```sql
CREATE TABLE my_table (
    column1 VARCHAR(50),
    column2 INT,
    column3 DATETIME
)
```

## Security Considerations

- **Never hardcode credentials** in production code
- Use environment variables or configuration files
- Implement proper connection pooling
- Use prepared statements when available
- Apply least privilege principle for database users

## Educational Value

These examples are valuable for:
- Learning Sybase database programming
- Understanding DB-Library API
- Working with legacy database systems
- Database connectivity in C++

## Context

Sybase (now SAP ASE - Adaptive Server Enterprise) is widely used in:
- Financial services
- Telecommunications
- Enterprise applications
- Legacy system maintenance

## Troubleshooting

### Common Issues

**Connection failures:**
- Verify server name and network connectivity
- Check firewall settings
- Confirm credentials are correct

**Compilation errors:**
- Ensure Sybase client libraries are installed
- Check include paths: `-I/opt/sybase/include`
- Check library paths: `-L/opt/sybase/lib`

**Runtime errors:**
- Verify database and table exist
- Check user permissions
- Review SQL syntax

## Modern Alternatives

While these examples use DB-Library, modern Sybase applications often use:
- ODBC (Open Database Connectivity)
- JDBC (for Java applications)
- Native client libraries with C++ wrappers

## Note

These examples are intended for educational purposes and compatibility testing. For production use, implement proper error handling, connection pooling, and security measures.
