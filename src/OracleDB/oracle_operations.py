"""
Oracle Database Connection Example using cx_Oracle

This example demonstrates how to connect to an Oracle database and perform
basic CRUD operations using Python and cx_Oracle (oracledb) library.

Prerequisites:
    pip install oracledb
"""

import oracledb


def connect_to_oracle():
    """
    Establish a connection to Oracle Database
    
    Returns:
        connection: Oracle database connection object
    """
    try:
        # Connection parameters
        username = "your_username"
        password = "your_password"
        dsn = "localhost:1521/ORCL"  # Format: host:port/service_name
        
        # Establish connection
        connection = oracledb.connect(
            user=username,
            password=password,
            dsn=dsn
        )
        
        print("Successfully connected to Oracle Database!")
        print(f"Oracle version: {connection.version}")
        
        return connection
        
    except oracledb.Error as error:
        print(f"Error connecting to Oracle Database: {error}")
        return None


def select_data(connection):
    """
    Retrieve data from Oracle Database
    
    Args:
        connection: Oracle database connection object
    """
    try:
        cursor = connection.cursor()
        
        # Execute SELECT query
        query = "SELECT employee_id, first_name, last_name, email FROM employees"
        cursor.execute(query)
        
        # Fetch all results
        rows = cursor.fetchall()
        
        print("\nEmployee Data:")
        print("ID\tFirst Name\tLast Name\tEmail")
        print("-" * 60)
        
        for row in rows:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}")
        
        cursor.close()
        
    except oracledb.Error as error:
        print(f"Error executing SELECT query: {error}")


def insert_data(connection):
    """
    Insert data into Oracle Database
    
    Args:
        connection: Oracle database connection object
    """
    try:
        cursor = connection.cursor()
        
        # Prepare INSERT statement
        query = """
            INSERT INTO employees (employee_id, first_name, last_name, email, hire_date)
            VALUES (:emp_id, :first_name, :last_name, :email, SYSDATE)
        """
        
        # Execute INSERT with parameters
        cursor.execute(query, {
            'emp_id': 1001,
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com'
        })
        
        # Commit transaction
        connection.commit()
        
        print(f"\nSuccessfully inserted {cursor.rowcount} row(s) into employees table")
        
        cursor.close()
        
    except oracledb.Error as error:
        connection.rollback()
        print(f"Error executing INSERT query: {error}")


def update_data(connection):
    """
    Update data in Oracle Database
    
    Args:
        connection: Oracle database connection object
    """
    try:
        cursor = connection.cursor()
        
        # Prepare UPDATE statement
        query = """
            UPDATE employees 
            SET email = :new_email 
            WHERE employee_id = :emp_id
        """
        
        # Execute UPDATE with parameters
        cursor.execute(query, {
            'new_email': 'jane.updated@example.com',
            'emp_id': 1001
        })
        
        # Commit transaction
        connection.commit()
        
        print(f"\nSuccessfully updated {cursor.rowcount} row(s) in employees table")
        
        cursor.close()
        
    except oracledb.Error as error:
        connection.rollback()
        print(f"Error executing UPDATE query: {error}")


def delete_data(connection):
    """
    Delete data from Oracle Database
    
    Args:
        connection: Oracle database connection object
    """
    try:
        cursor = connection.cursor()
        
        # Prepare DELETE statement
        query = "DELETE FROM employees WHERE employee_id = :emp_id"
        
        # Execute DELETE with parameter
        cursor.execute(query, {'emp_id': 1001})
        
        # Commit transaction
        connection.commit()
        
        print(f"\nSuccessfully deleted {cursor.rowcount} row(s) from employees table")
        
        cursor.close()
        
    except oracledb.Error as error:
        connection.rollback()
        print(f"Error executing DELETE query: {error}")


def execute_stored_procedure(connection):
    """
    Execute a stored procedure in Oracle Database
    
    Args:
        connection: Oracle database connection object
    """
    try:
        cursor = connection.cursor()
        
        # Call stored procedure
        # Example: CALL get_employee_count(:dept_id, :emp_count)
        dept_id = 10
        emp_count = cursor.var(int)
        
        cursor.callproc("get_employee_count", [dept_id, emp_count])
        
        print(f"\nEmployee count for department {dept_id}: {emp_count.getvalue()}")
        
        cursor.close()
        
    except oracledb.Error as error:
        print(f"Error executing stored procedure: {error}")


def main():
    """
    Main function to demonstrate Oracle database operations
    """
    # Connect to database
    connection = connect_to_oracle()
    
    if connection:
        try:
            # Uncomment the operations you want to perform
            
            # select_data(connection)
            # insert_data(connection)
            # update_data(connection)
            # delete_data(connection)
            # execute_stored_procedure(connection)
            
            pass
            
        finally:
            # Close connection
            connection.close()
            print("\nConnection closed.")


if __name__ == "__main__":
    main()
