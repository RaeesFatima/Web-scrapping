import mysql.connector
class ZameenLahorePipeline:
    def __init__(self):
        self.create_connection()
    def create_connection(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="home",
            database="zameendb"
        )
        self.mycursor = self.mydb.cursor()

        # self.mycursor.execute("CREATE DATABASE zameendb")
        # self.mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        sql=""" INSERT into zameen_houses
        (added, home_url, is_trusted, deal_type, is_titanium, 
                  house_type, area, currency, price, purpose, 
                  location, bath, bedroom, description, amenities) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        values=(
            ", ".join(item['added']) if item['added'] else None,
            item['home_url'],
            item['is_trusted'],
            item['deal_type'],
            item['is_titanium'],
            item['house_type'],
            item['area'],
            item['currency'],
            item['price'],
            item['purpose'],
            item['location'],
            item['bath'],
            item['bedroom'],
            " ".join(item['description']) if item['description'] else None,
            ", ".join(item['amenities']) if item['amenities'] else None
        )

        self.mycursor.execute(sql, values)
        self.mydb.commit()