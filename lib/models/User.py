from db import CURSOR, CONN

class User:
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

    def save(self):
        """Insert a new user or update an existing one."""
        if self.id:
            CURSOR.execute("""
                UPDATE users
                SET name = ?, email = ?
                WHERE id = ?
            """, (self.name, self.email, self.id))
        else:
            CURSOR.execute("""
                INSERT INTO users (name, email)
                VALUES (?, ?)
            """, (self.name, self.email))
            self.id = CURSOR.lastrowid
        CONN.commit()

    def delete(self):
        """Delete the user from the database."""
        if self.id:
            CURSOR.execute("DELETE FROM users WHERE id = ?", (self.id,))
            CONN.commit()
            self.id = None

    
    def get_all(cls):
        """Return a list of all users."""
        CURSOR.execute("SELECT * FROM users")
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1], email=row[2]) for row in rows]

    
    def find_by_id(cls, user_id):
        """Find a user by ID."""
        CURSOR.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], name=row[1], email=row[2])
        return None

    
    def find_by_email(cls, email):
        """Find a user by email."""
        CURSOR.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], name=row[1], email=row[2])
        return None

    def __repr__(self):
        return f"<User id={self.id} name={self.name} email={self.email}>"
