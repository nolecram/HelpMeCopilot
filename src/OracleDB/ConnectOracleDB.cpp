#include <iostream>
#include <occi.h>

using namespace oracle::occi;
using namespace std;

int main() {
    Environment *env = nullptr;
    Connection *conn = nullptr;

    try {
        // Create environment
        env = Environment::createEnvironment(Environment::DEFAULT);
        
        // Connection parameters
        string username = "your_username";
        string password = "your_password";
        string connectString = "//localhost:1521/ORCL";  // Format: //host:port/service_name
        
        // Establish connection
        conn = env->createConnection(username, password, connectString);
        
        cout << "Successfully connected to Oracle Database!" << endl;
        
        // Clean up
        env->terminateConnection(conn);
        Environment::terminateEnvironment(env);
        
        return 0;
        
    } catch (SQLException &ex) {
        cerr << "Error connecting to database: " << ex.getMessage() << endl;
        
        if (conn != nullptr) {
            env->terminateConnection(conn);
        }
        if (env != nullptr) {
            Environment::terminateEnvironment(env);
        }
        
        return 1;
    }
}
