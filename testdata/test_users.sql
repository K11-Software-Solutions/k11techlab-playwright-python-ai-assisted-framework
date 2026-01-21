-- Example SQLite test data for Playwright tests
-- Run this script in a SQLite client or use sqlite3 CLI to create the database

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users (email, password) VALUES
    ('testuser', 'testpass'),
    ('wronguser', 'wrongpass');
