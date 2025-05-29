from lib.db import CURSOR, CONN
from lib.models.User import User
from lib.models.Pizza import Pizza

def create_tables():
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS pizzas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            size TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS pizza_toppings (
            pizza_id INTEGER,
            topping TEXT,
            FOREIGN KEY (pizza_id) REFERENCES pizzas(id) ON DELETE CASCADE
        )
    """)
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            pizza_id INTEGER,
            quantity INTEGER NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (pizza_id) REFERENCES pizzas(id)
        )
    """)
    CONN.commit()
    print("Tables created (if they did not exist).")

def seed_data():
    if not User.find_by_email("abby@example.com"):
        users = [
            User("Abby", "abby@example.com"),
            User("Trevis", "trevis@example.com"),
        ]
        for user in users:
            try:
                user.save()
                print(f"User {user.name} saved.")
            except Exception as e:
                print(f"Failed to save user {user.name}: {e}")
    else:
        print("Users already exist — skipping user seeding.")

    
    pizzas = [
        Pizza("Pepperoni", "Large", 12.5, ["Pepperoni", "Cheese"]),
        Pizza("Veggie", "Medium", 10.0, ["Tomato", "Onion", "Bell Pepper"]),
    ]
    for pizza in pizzas:
        try:
            pizza.save()
            print(f"Pizza {pizza.name} saved.")
        except Exception as e:
            print(f"Failed to save pizza {pizza.name}: {e}")

def main():
    create_tables()
    seed_data()
    CONN.close()
    print("Database seeded successfully.")

if __name__ == "__main__":
    main()
