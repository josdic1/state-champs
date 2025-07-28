from lib import CONN,CURSOR

class State:
    def __init__(self, name, region):
        self.name = name
        self.region = region
        self.id = None

    def __repr__(self):
        return f"State: {self.name} | {self.region}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance (value, str) and value.strip():
            self._name = value
    
    @property
    def region(self):
        return self._region
    
    @region.setter
    def region(self, value):
        if isinstance (value, str) and value.strip():
            self._region = value

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS states (
                id INTEGER PRIMARY KEY,
                name TEXT,
                region TEXT
            )
        """)

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM states")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows]

    @classmethod
    def _from_db_row(cls, row):
        state = cls(row[1], row[2])
        state.id = row[0]
        return state
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM states WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls._from_db_row(row)
        else:
            return None
    
    @classmethod
    def add_new(cls, name, region):
        state = cls(name, region)
        state.save()
        return state

    def update(self):
        CURSOR.execute("UPDATE states SET name = ?, region = ? WHERE id = ?", (self._name, self._region, self.id,))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM states WHERE id = ?", (self.id,))
        CONN.commit()
        self.id = None


    def save(self):
        CURSOR.execute("INSERT INTO states (name, region) VALUES (?,?)", (self._name, self._region))
        self.id = CURSOR.lastrowid
        CONN.commit()
        
    
