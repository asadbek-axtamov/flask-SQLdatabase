import sqlite3

class Smartphone:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()

    def sql_get_all_smartphones(self):
        self.cursor.execute("SELECT * FROM smartphone")
        data=self.cursor.fetchall()
        return data
    
    def sql_get_product_by_id(self, id):
        self.cursor.execute("SELECT * FROM smartphone WHERE id = ?", (id, ))
        data = self.cursor.fetchone()
        return data
    
    def sql_get_smartphone_by_name(self, name):
        self.cursor.execute("SELECT * FROM smartphone WHERE name = ?", (name, ))
        data = self.cursor.fetchone()
        return data
    
    def sql_get_smartphone_all_names(self):
        self.cursor.execute("SELECT name FROM smartphone")
        data = self.cursor.fetchall()
        return data
    
    def sql_get_smartphone_by_color(self, color):
        self.cursor.execute("SELECT * FROM smartphone WHERE color = ?", (color.title(), ))
        data = self.cursor.fetchall()
        return data
    
    def sql_get_smartphone_by_ram(self, ram):
        self.cursor.execute("SELECT * FROM smartphone WHERE ram = ?", (ram,))
        data = self.cursor.fetchall()
        return data
    
    def sql_get_smartphone_by_memory(self, memory):
        self.cursor.execute("SELECT * FROM smartphone WHERE memory = ?", (memory, ))
        data = self.cursor.fetchall()
        return data
    
    def sql_get_smartphone_by_price(self, price):
        self.cursor.excute("SELECT * FROM smartphone WHERE price = ?", (price,))
        data = self.cursor.fetchall()
        return data
    
    def sql_add_smartphone(self, phone):
        self.cursor.execute("INSERT INTO smartphone (id, name, color, ram, memory, price) VALUES(?,?,?,?,?,?)", (phone['id'], phone['name'], phone['color'], phone['ram'],phone['memory'], phone['price']))
        self.connect.commit()
        return {"statust": 200}
    
    def sql_delete_smartphone(self, id):

        return 
