#include <iostream>
#include <occi.h>

using namespace oracle::occi;
using namespace std;

int main() {
    Environment *env = nullptr;
    Connection *conn = nullptr;
    Statement *stmt = nullptr;

    try {
        // Create environment and connection
        env = Environment::createEnvironment(Environment::DEFAULT);
        
        string username = "your_username";
        string password = "your_password";
        string connectString = "//localhost:1521/ORCL";
        
        conn = env->createConnection(username, password, connectString);
        
        // Prepare UPDATE statement
        string sql = "UPDATE employees SET email = 'john.updated@example.com' "
                     "WHERE employee_id = 1001";
        
        stmt = conn->createStatement(sql);
        
        // Execute UPDATE
        int rowsAffected = stmt->executeUpdate();
        
        cout << "Successfully updated " << rowsAffected << " row(s) in employees table" << endl;
        
        // Commit transaction
        conn->commit();
        
        // Clean up
        conn->terminateStatement(stmt);
        env->terminateConnection(conn);
        Environment::terminateEnvironment(env);
        
        return 0;
        
    } catch (SQLException &ex) {
        cerr << "SQL Error: " << ex.getMessage() << endl;
        
        if (stmt != nullptr) {
            conn->terminateStatement(stmt);
        }
        if (conn != nullptr) {
            conn->rollback();
            env->terminateConnection(conn);
        }
        if (env != nullptr) {
            Environment::terminateEnvironment(env);
        }
        
        return 1;
    }
}
