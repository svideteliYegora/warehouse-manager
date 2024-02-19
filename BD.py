import sqlite3 as sl

con = sl.connect('warehouseBD.db', check_same_thread=False)

with con:
    con.execute("""
            CREATE TABLE IF NOT EXISTS access (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                access_level INTEGER
            );
        """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS staff (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            surname VARCHAR(20),
            login VARCHAR(20),
            password VARCHAR(20),
            access_id INTEGER,
            FOREIGN KEY (access_id) REFERENCES access (id)
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            surname VARCHAR(20),
            age INTEGER,
            address VARCHAR(30),
            email VARCHAR(30)
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            total_price INTEGER,
            order_date INTEGER,
            delivery_date INTEGER,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)                  
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS warehouse (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            address VARCHAR(30),
            text_location VARCHAR(50),
            latitude DECIMAL,
            longitude DECIMAL                 
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR(30),
            category VARCHAR(30),
            characteristic TEXT,
            vendor_code VARCHAR(30),
            price BIGINT,
            image_path VARCHAR(50),
            quantity_type INTEGER   
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS orderDetail (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            order_number INTEGER,
            quantity INTEGER,
            product_id INTEGER,                  
            FOREIGN KEY (order_number) REFERENCES orders (id),
            FOREIGN KEY (product_id) REFERENCES product (id)                  
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS warehouseProduct (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            warehouse_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            delivery_date INTEGER,
            expiration_date INTEGER,                 
            FOREIGN KEY (warehouse_id) REFERENCES orders (id),
            FOREIGN KEY (product_id) REFERENCES product (id),
            FOREIGN KEY (quantity) REFERENCES product (quantity_type)                  
        );
    """)

class MethosdBD:
    def get_table(self,table:str):
        """
        Получение всех записей из указанной таблицы
        :param table: название таблицы
        :return: список кортежей с записями таблицы, если в таблице нет записей —вернет пустой список
        """
        s=f"SELECT * FROM {table}"
        try:
            with con:
                data=con.execute(s)
                return data.fetchall()
        except:
            raise ValueError("Заданной таблицы не существует")

    def get_record(self,table:str,**param:dict):
        """
        Получение 1 записи из указанной таблицы с указанным условием
        :param table: имя таблицы
        :param param: словарь условий
        :return: возвращает 1 запись в кортеже
        """
        s=f"SELECT * from {table} WHERE "
        key=list(param.keys())
        for i in range(len(param)):
            if i==len(param)-1:
                s+=f"{key[i]}={param[key[i]]}"
            else:
                s += f"{key[i]}={param[key[i]]} AND "
        with con:
            data = con.execute(s)
            return data.fetchall()[0]

    def del_record(self,table:str, **param:dict):
        """
        Удаляет запись из таблицы с указанным условием
        :param table: имя таблицы
        :param param: словарь условий
        :return: ничего не возвращает
        """
        s = f"DELETE FROM {table} WHERE "
        key = list(param.keys())
        for i in range(len(param)):
            if i == len(param) - 1:
                s += f"{key[i]}={param[key[i]]}"
            else:
                s += f"{key[i]}={param[key[i]]} AND "
        with con:
            con.execute(s)

    def add_record(self,table:str,**param:dict):
        """
        Добавляет запись в указанную таблицу по указанным значениям в словаре
        :param table: имя таблицы
        :param param: словарь значений для записи в  таблицу
        :return: ничего не возвращает
        """
        s=f"INSERT INTO {table} ("
        s1=f"SELECT "
        key = list(param.keys())
        for i in range(len(param)):
            if i == len(param) - 1:
                s += f"{key[i]}) "
                s1+=f"{param[key[i]]}"
            else:
                s += f"{key[i]},"
                s1+= f"{param[key[i]]},"

        s=s+s1
        with con:
            con.execute(s)


workBD=MethosdBD()