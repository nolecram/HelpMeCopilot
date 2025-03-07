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

    const char *query = "DELETE FROM my_table WHERE column1 = 'value1'";
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

    std::cout << "Data deleted successfully" << std::endl;

    dbclose(dbproc);
    dbexit();

    return 0;
}