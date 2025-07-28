
CREATE TABLE IF NOT EXISTS states (
    id INTEGER PRIMARY KEY,
    name TEXT,
    region TEXT
);

CREATE TABLE IF NOT EXISTS capitals (
    id INTEGER PRIMARY KEY,
    name TEXT,
    state_id INTEGER,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

CREATE TABLE IF NOT EXISTS local_teams (
    id INTEGER PRIMARY KEY,
    name TEXT,
    sport TEXT,
    state_id INTEGER,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

