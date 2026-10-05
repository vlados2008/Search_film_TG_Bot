import sqlite3

class DataBase:
    def __init__(self):
        self.__connect = sqlite3.connect("./db/database.db")
        self.__connect.row_factory = sqlite3.Row
        self.__cursor = self.__connect.cursor()
        self.__create_table()

    def __create_table (self):
        self.__cursor.execute("PRAGMA foreign_keys = ON")
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                full_name TEXT,
                name TEXT,
                username TEXT,
                language TEXT
            )
            """)
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """)

    def add_user(self, user_obj):
        self.__cursor.execute(
            "INSERT INTO users (user_id, full_name, name, username, language) VALUES (?, ?, ?, ?, ?)",
            (user_obj.id, user_obj.full_name, user_obj.name, user_obj.username, user_obj.language)
        )
        self.__connect.commit()

    def get_user(self, id):
        self.__cursor.execute(
            f"SELECT * FROM users WHERE user_id = {id}"
        )
        user = self.__cursor.fetchone()
        return user
    
    def change_lang(self, id, lang):
        self.__cursor.execute(
            f"UPDATE users SET language = ? WHERE user_id = ?",
            (lang, id)
        )
        self.__connect.commit()

    def change_full_name(self, id, full_name):
        self.__cursor.execute(
            f"UPDATE users SET full_name = ? WHERE user_id = ?",
            (full_name, id)
        )
        self.__connect.commit()

    def change_username(self, id, username):
        self.__cursor.execute(
            f"UPDATE users SET username = ? WHERE user_id = ?",
            (username, id)
        )
        self.__connect.commit()
    
    def delete_user(self, id):
        self.__cursor.execute(
            f"DELETE FROM users WHERE user_id = {id}"
        )
        self.__connect.commit()

    def add_history(self, search, user_id):
        self.__cursor.execute(
            f"INSERT INTO history (name, user_id) VALUES (?, ?)",
            (search, user_id)
        )
        self.__connect.commit()

    def get_history(self, user_id):
        user = self.get_user(user_id)
        id = user['id']
        self.__cursor.execute(
            f"SELECT name FROM history WHERE user_id = {id} ORDER BY id DESC LIMIT 20"
        )
        history = self.__cursor.fetchall()
        return history