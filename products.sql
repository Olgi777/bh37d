CREATE TABLE IF NOT EXISTS products(
    id INTEGER SERIAL PRIMARY KEY,
    title VARCHAR(36),
    description VARCHAR(140),
    category_id INTEGER FOREIGN KEY
);