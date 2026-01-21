-- SQL test data for login
INSERT INTO logindata (testName, email, password, expected) VALUES
('Valid login', 'testuser', 'testpass', 'success'),
('Invalid login', 'wronguser', 'wrongpass', 'failure');
