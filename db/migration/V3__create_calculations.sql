CREATE TABLE calculations (
    id         SERIAL PRIMARY KEY,
    user_id    INTEGER REFERENCES users(id),
    operation  VARCHAR(10) NOT NULL,
    a          INTEGER NOT NULL,
    b          INTEGER NOT NULL,
    result     NUMERIC,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
