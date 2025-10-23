# Oracle Database Integration Examples

This directory contains examples demonstrating how to connect to and interact with Oracle Database using different programming languages.

## Overview

The examples cover basic CRUD (Create, Read, Update, Delete) operations and demonstrate proper connection handling, error management, and transaction control.

## C++ Examples (using Oracle OCCI)

### Prerequisites

- Oracle Instant Client
- Oracle C++ Call Interface (OCCI) library
- C++ compiler (g++, clang, or Visual Studio)

### Files

1. **ConnectOracleDB.cpp** - Basic connection to Oracle Database
   - Demonstrates establishing a connection
   - Shows proper resource cleanup
   - Includes error handling

2. **SelectDataOracle.cpp** - Querying data from Oracle Database
   - Executes SELECT queries
   - Retrieves and processes result sets
   - Displays query results

3. **InsertDataOracle.cpp** - Inserting data into Oracle Database
   - Executes INSERT statements
   - Handles transactions with commit
   - Includes rollback on error

4. **UpdateDataOracle.cpp** - Updating data in Oracle Database
   - Executes UPDATE statements
   - Transaction management
   - Row count reporting

5. **DeleteDataOracle.cpp** - Deleting data from Oracle Database
   - Executes DELETE statements
   - Transaction control
   - Proper cleanup and rollback

### Compilation

To compile the C++ examples, use the following command:

```bash
g++ -o connect_oracle ConnectOracleDB.cpp -I$ORACLE_HOME/rdbms/public -L$ORACLE_HOME/lib -locci -lclntsh
g++ -o select_oracle SelectDataOracle.cpp -I$ORACLE_HOME/rdbms/public -L$ORACLE_HOME/lib -locci -lclntsh
g++ -o insert_oracle InsertDataOracle.cpp -I$ORACLE_HOME/rdbms/public -L$ORACLE_HOME/lib -locci -lclntsh
g++ -o update_oracle UpdateDataOracle.cpp -I$ORACLE_HOME/rdbms/public -L$ORACLE_HOME/lib -locci -lclntsh
g++ -o delete_oracle DeleteDataOracle.cpp -I$ORACLE_HOME/rdbms/public -L$ORACLE_HOME/lib -locci -lclntsh
```

**Note:** Set the `ORACLE_HOME` environment variable to your Oracle installation directory.

## Python Example (using oracledb)

### Prerequisites

Install the Oracle database driver for Python:

```bash
pip install oracledb
```

### File

**oracle_operations.py** - Comprehensive Python example
- Connection management
- SELECT queries
- INSERT operations with parameterized queries
- UPDATE operations
- DELETE operations
- Stored procedure execution
- Proper exception handling

### Usage

```bash
python oracle_operations.py
```

Uncomment the desired operations in the `main()` function to execute them.

## Configuration

Before running any examples, update the connection parameters:

### C++ Examples
```cpp
string username = "your_username";
string password = "your_password";
string connectString = "//localhost:1521/ORCL";  // Format: //host:port/service_name
```

### Python Example
```python
username = "your_username"
password = "your_password"
dsn = "localhost:1521/ORCL"  # Format: host:port/service_name
```

## Database Schema

The examples assume a table named `employees` with the following structure:

```sql
CREATE TABLE employees (
    employee_id NUMBER PRIMARY KEY,
    first_name VARCHAR2(50),
    last_name VARCHAR2(50),
    email VARCHAR2(100),
    hire_date DATE
);
```

You can create this table using SQL*Plus or any Oracle database client.

## Common Connection String Formats

- **Easy Connect**: `//hostname:port/service_name`
- **TNS Name**: `TNS_ALIAS` (requires tnsnames.ora configuration)
- **Full TNS**: `(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=hostname)(PORT=port))(CONNECT_DATA=(SERVICE_NAME=service_name)))`

## Error Handling

All examples include comprehensive error handling:
- C++ examples use try-catch blocks for `SQLException`
- Python examples use try-except blocks for `oracledb.Error`
- Proper resource cleanup in all cases
- Transaction rollback on errors

## Security Best Practices

⚠️ **Important Security Notes:**

1. **Never hardcode credentials** in production code
2. Use environment variables or secure configuration files
3. Consider using Oracle Wallet for credential management
4. Use connection pooling for better performance and resource management
5. Always use parameterized queries to prevent SQL injection

## Additional Resources

- [Oracle C++ Call Interface Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/21/lncpp/)
- [Python oracledb Documentation](https://python-oracledb.readthedocs.io/)
- [Oracle Database Documentation](https://docs.oracle.com/en/database/)

## License

These examples are provided for educational purposes.
