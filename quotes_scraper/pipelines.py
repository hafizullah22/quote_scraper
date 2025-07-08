import mysql.connector

class MySQLPipeline:

    def open_spider(self, spider):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='scrapydb'
        )
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS quotes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                text TEXT,
                author VARCHAR(255)
            )
        """)

    def close_spider(self, spider):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute("""
            INSERT INTO quotes (text, author)
            VALUES (%s, %s)
        """, (item['text'], item['author']))
        self.connection.commit()
        return item
