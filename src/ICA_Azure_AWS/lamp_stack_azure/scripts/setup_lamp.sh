#!/bin/bash

# Update package lists
sudo apt update
sudo apt upgrade -y

# Install LAMP stack components
sudo apt install -y apache2 mysql-client php php-mysql libapache2-mod-php

# Enable Apache modules
sudo a2enmod rewrite
sudo a2enmod ssl

# Restart Apache
sudo systemctl restart apache2

# Create info.php file for testing
cat <<EOF | sudo tee /var/www/html/info.php
<?php
phpinfo();
?>
EOF

# Create a sample application
cat <<EOF | sudo tee /var/www/html/index.php
<!DOCTYPE html>
<html>
<head>
    <title>LAMP Stack on Azure</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #f4f4f4;
            padding: 20px;
            border-radius: 5px;
        }
        h1 {
            color: #0078D4;
        }
        .info {
            background: #e9f7fe;
            padding: 15px;
            border-left: 4px solid #0078D4;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>LAMP Stack Successfully Deployed on Azure!</h1>
        
        <div class="info">
            <h2>Environment Information</h2>
            <p><strong>Server:</strong> <?php echo $_SERVER['SERVER_SOFTWARE']; ?></p>
            <p><strong>PHP Version:</strong> <?php echo phpversion(); ?></p>
            <p><strong>Document Root:</strong> <?php echo $_SERVER['DOCUMENT_ROOT']; ?></p>
            <p><strong>Server Name:</strong> <?php echo $_SERVER['SERVER_NAME']; ?></p>
            <p><strong>Server IP:</strong> <?php echo $_SERVER['SERVER_ADDR']; ?></p>
        </div>
        
        <h2>Database Connection Test</h2>
        <?php
        // These would normally come from environment variables or a config file
        $dbhost = getenv("MYSQL_HOST") ?: "localhost";
        $dbuser = getenv("MYSQL_USER") ?: "mysqladmin";
        $dbpass = getenv("MYSQL_PASSWORD") ?: "";
        $dbname = getenv("MYSQL_DATABASE") ?: "lampdb";
        
        try {
            $conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
            
            if ($conn->connect_error) {
                echo "<p style='color: red;'>Database connection failed: " . $conn->connect_error . "</p>";
            } else {
                echo "<p style='color: green;'>Successfully connected to the database!</p>";
                $conn->close();
            }
        } catch (Exception $e) {
            echo "<p style='color: orange;'>Database connection not configured or unavailable.</p>";
        }
        ?>
        
        <h2>Next Steps</h2>
        <ul>
            <li>Secure your MySQL server by restricting access</li>
            <li>Configure SSL certificates for your website</li>
            <li>Implement a backup strategy for your database</li>
            <li>Set up monitoring for your LAMP stack</li>
        </ul>
    </div>
</body>
</html>
EOF

# Secure Apache configuration
sudo sed -i 's/ServerTokens OS/ServerTokens Prod/' /etc/apache2/conf-enabled/security.conf 
sudo sed -i 's/ServerSignature On/ServerSignature Off/' /etc/apache2/conf-enabled/security.conf

# Set proper permissions
sudo chown -R www-data:www-data /var/www/html/
sudo chmod -R 755 /var/www/html/

# Restart Apache service
sudo systemctl restart apache2

echo "LAMP stack installation and configuration complete."
