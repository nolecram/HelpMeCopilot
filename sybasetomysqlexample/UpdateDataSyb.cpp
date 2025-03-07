#include <iostream>
#include <sybfront.h>
#include <sybdb.h>

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

    const char *query = "UPDATE my_table SET column1 = 'new_value' WHERE column2 = 'value2'";
    if (dbcmd(dbproc, query) == FAIL) {
        std::cerr << "Failed to execute query" << std::endl;
        dbclose(dbproc);
        return 1;
    }

    if (dbsqlexec(dbproc) == FAIL) {
        std::cerr << "Failed to send query to the server" << std::endl;
        dbclose(dbproc);
        return 1;
    }

    std::cout << "Data updated successfully" << std::endl;

    dbclose(dbproc);
    dbexit();

    return 0;
}