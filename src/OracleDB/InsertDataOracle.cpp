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
        
        // Prepare INSERT statement
        string sql = "INSERT INTO employees (employee_id, first_name, last_name, email, hire_date) "
                     "VALUES (1001, 'John', 'Doe', 'john.doe@example.com', SYSDATE)";
        
        stmt = conn->createStatement(sql);
        
        // Execute INSERT
        int rowsAffected = stmt->executeUpdate();
        
        cout << "Successfully inserted " << rowsAffected << " row(s) into employees table" << endl;
        
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
