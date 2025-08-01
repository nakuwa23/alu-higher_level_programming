-- comment
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
REVOKE AUDIT_ABORT_EXEMPT, FIREWALL_EXEMPT, AUTHENTICATION_POLICY_ADMIN, GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN, SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN ON *.* FROM 'user_0d_1'@'localhost';
