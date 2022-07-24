import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('data/database.db')
        self.cursor = self.connection.cursor()

        self.create_meals_table()
        self.create_barcodes_table()

    def create_meals_table(self):
        table_query = """
        CREATE TABLE IF NOT EXISTS meals
        (
            [meal_id] INTEGER PRIMARY KEY AUTOINCREMENT,
            [feed_time] TIME,
            [feed_date] DATE,
            [half_pouch] INTEGER,
            [product_id] INTEGER
        )
        """

        self.cursor.execute(table_query)
        self.connection.commit()

    def create_barcodes_table(self):
        table_query = """
        CREATE TABLE IF NOT EXISTS products
        (
            [product_id] INTEGER PRIMARY KEY AUTOINCREMENT,
            [barcode] VARCHAR(100),
            [product] VARCHAR(500),
            [calories] INTEGER,
            [protein] INTEGER,
            [fat] INTEGER,
            [fiber] INTEGER,
            [moisture] INTEGER
        )
        """

        self.cursor.execute(table_query)
        self.connection.commit()

    def update_meals(self, time, date, half, prod_id):
        table_query = f"""
        INSERT INTO meals 
        (feed_time, feed_date, half_pouch, product_id)
        VALUES 
        ({time}, {date}, {half}, {prod_id})
        """

        self.cursor.execute(table_query)
        self.connection.commit()


if __name__ == '__main__':
    db = Database()
