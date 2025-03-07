#include <iostream>
#include <sybfront.h>
#include <sybdb.h>

int main() {
    // Initialize DB-Library
    if (dbinit() == FAIL) {
        std::cerr << "Failed to initialize DB-Library" << std::endl;
        return 1;
    }

    // Allocate login structure
    LOGINREC *login = dblogin();
    DBPROCESS *dbproc;

    // Set login credentials
    DBSETLUSER(login, "username");
    DBSETLPWD(login, "password");

    // Connect to the database
    dbproc = dbopen(login, "server");

    if (dbproc == NULL) {
        std::cerr << "Failed to connect to the database" << std::endl;
        return 1;
    }

    // Execute a query
    if (dbcmd(dbproc, "SELECT * FROM my_table") == FAIL) {
        std::cerr << "Failed to execute query" << std::endl;
        dbclose(dbproc);
        return 1;
    }

    // Send the query to the server
    if (dbsqlexec(dbproc) == FAIL) {
        std::cerr << "Failed to send query to the server" << std::endl;
        dbclose(dbproc);
        return 1;
    }

    // Process the results
    while (dbresults(dbproc) != NO_MORE_RESULTS) {
        DBINT col_count = dbnumcols(dbproc);
        while (dbnextrow(dbproc) != NO_MORE_ROWS) {
            for (DBINT i = 1; i <= col_count; ++i) {
                std::cout << dbdata(dbproc, i) << " ";
            }
            std::cout << std::endl;
        }
    }

    // Clean up
    dbclose(dbproc);
    dbexit();

    return 0;
}