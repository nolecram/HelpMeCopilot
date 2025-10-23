#include <iostream>
#include <occi.h>

using namespace oracle::occi;
using namespace std;

int main() {
    Environment *env = nullptr;
    Connection *conn = nullptr;
    Statement *stmt = nullptr;
    ResultSet *rs = nullptr;

    try {
        // Create environment and connection
        env = Environment::createEnvironment(Environment::DEFAULT);
        
        string username = "your_username";
        string password = "your_password";
        string connectString = "//localhost:1521/ORCL";
        
        conn = env->createConnection(username, password, connectString);
        
        // Create statement
        stmt = conn->createStatement("SELECT employee_id, first_name, last_name, email FROM employees");
        
        // Execute query
        rs = stmt->executeQuery();
        
        // Process results
        cout << "Employee Data:" << endl;
        cout << "ID\tFirst Name\tLast Name\tEmail" << endl;
        cout << "------------------------------------------------------------" << endl;
        
        while (rs->next()) {
            int empId = rs->getInt(1);
            string firstName = rs->getString(2);
            string lastName = rs->getString(3);
            string email = rs->getString(4);
            
            cout << empId << "\t" << firstName << "\t\t" << lastName << "\t" << email << endl;
        }
        
        // Clean up
        stmt->closeResultSet(rs);
        conn->terminateStatement(stmt);
        env->terminateConnection(conn);
        Environment::terminateEnvironment(env);
        
        return 0;
        
    } catch (SQLException &ex) {
        cerr << "SQL Error: " << ex.getMessage() << endl;
        
        if (rs != nullptr && stmt != nullptr) {
            stmt->closeResultSet(rs);
        }
        if (stmt != nullptr) {
            conn->terminateStatement(stmt);
        }
        if (conn != nullptr) {
            env->terminateConnection(conn);
        }
        if (env != nullptr) {
            Environment::terminateEnvironment(env);
        }
        
        return 1;
    }
}
