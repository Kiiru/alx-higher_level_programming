-- a script that creates the table unique_id
CREATE TABLE IF NOT EXISTS unique_id(
	id INTEGER UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
