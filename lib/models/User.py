from db import CONN, CURSOR

class User:
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

    def save(self):
        if self.id:
            CURSOR.execute(
                "UPDATE users SET name = ?, email = ? WHERE id = ?",
                (self.name, self.email, self.id)
            )
        else:
            CURSOR.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (self.name, self.email)
            )
            self.id = CURSOR.lastrowid
        CONN.commit()

    @classmethod
    def get_by_id(cls, id):
        CURSOR.execute("SELECT * FROM users WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], name=row[1], email=row[2]) if row else None

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM users")
        return [cls(id=row[0], name=row[1], email=row[2]) for row in CURSOR.fetchall()]

    def delete(self):
        if self.id:
            CURSOR.execute("DELETE FROM users WHERE id = ?", (self.id,))
            CONN.commit()
