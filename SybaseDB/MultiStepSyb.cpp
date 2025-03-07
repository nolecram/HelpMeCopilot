#include <iostream>
#include <sybfront.h>
#include <sybdb.h>

void handle_error(DBPROCESS *dbproc) {
    std::cerr << "Database error: " << dbproc->dbsqlexec << std::endl;
    dbclose(dbproc);
    dbexit();
    exit(1);
}

void execute_query(DBPROCESS *dbproc, const char *query) {
    if (dbcmd(dbproc, query) == FAIL) {
        std::cerr << "Failed to set query: " << query << std::endl;
        handle_error(dbproc);
    }

    if (dbsqlexec(dbproc) == FAIL) {
        std::cerr << "Failed to execute query: " << query << std::endl;
        handle_error(dbproc);
    }
}

void process_results(DBPROCESS *dbproc) {
    while (dbresults(dbproc) != NO_MORE_RESULTS) {
        int col_count = dbnumcols(dbproc);

        while (dbnextrow(dbproc) != NO_MORE_ROWS) {
            for (int i = 1; i <= col_count; ++i) {
                std::cout << dbdata(dbproc, i) << " ";
            }
            std::cout << std::endl;
        }
    }
}

int main() {
    if (dbinit() == FAIL) {
        std::cerr << "Failed to initialize DB-Library" << std::endl;
        return 1;
    }

    LOGINREC *login = dblogin();
    DBPROCESS *dbproc;

    DBSETLUSER(login, "username");
    DBSETLPWD(login, "password");

    dbproc = dbopen(login, "server");

    if (dbproc == NULL) {
        std::cerr << "Failed to connect to the database" << std::endl;
        return 1;
    }

    // Example of creating a table
    const char *create_table_query = "CREATE TABLE example_table (id INT PRIMARY KEY, name VARCHAR(50), age INT)";
    execute_query(dbproc, create_table_query);

    // Example of inserting data
    const char *insert_query = "INSERT INTO example_table (id, name, age) VALUES (1, 'John Doe', 30)";
    execute_query(dbproc, insert_query);

    // Example of calling a stored procedure
    const char *proc_query = "CREATE PROCEDURE get_user @id INT AS SELECT * FROM example_table WHERE id = @id";
    execute_query(dbproc, proc_query);

    const char *call_proc_query = "EXEC get_user @id = 1";
    execute_query(dbproc, call_proc_query);

    // Process results of stored procedure
    process_results(dbproc);

    // Example of updating data
    const char *update_query = "UPDATE example_table SET age = 31 WHERE id = 1";
    execute_query(dbproc, update_query);

    // Example of deleting data
    const char *delete_query = "DELETE FROM example_table WHERE id = 1";
    execute_query(dbproc, delete_query);

    // Example of dropping the table
    const char *drop_table_query = "DROP TABLE example_table";
    execute_query(dbproc, drop_table_query);

    dbclose(dbproc);
    dbexit();

    return 0;
}