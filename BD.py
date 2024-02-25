import sqlite3 as sl

con = sl.connect('warehouseBD.db', check_same_thread=False)
cur=con.cursor()

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
            warehouse_name VARCHAR(30),
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
            price DECIMAL,
            image_path VARCHAR(50)
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS orderDetail (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            order_number INTEGER,
            quantity INTEGER,
            product_id INTEGER,
            FOREIGN KEY (order_number) REFERENCES orders (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
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
            FOREIGN KEY (warehouse_id) REFERENCES warehouse (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
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
                s += f"{key[i]} = '{param[key[i]]}'"
            else:
                s += f"{key[i]} = '{param[key[i]]}' AND "
            print(s)
        with con:
            con.execute(s)

    def add_record(self, table: str, **param: dict):
        """
        Добавляет запись в указанную таблицу по указанным значениям в словаре
        :param table: имя таблицы
        :param param: словарь значений для записи в  таблицу
        :return: ничего не возвращает
        """
        fields = str(tuple(param.keys())).replace("'", "")
        values = str(tuple(param.values()))
        query = f"INSERT INTO {table} {fields} VALUES {values}"
        with con:
            con.execute(query)

    def get_warehouse_name(self):
        """
        Получение всех названий складов
        :return: список названий складов
        """
        s="SELECT warehouse_name FROM warehouse"
        with con:
            data = con.execute(s)
            data=data.fetchall()
            data1=[]
            for i in data:
                data1.append(i[0])
            return data1

    def get_access_level(self,login:str,password:str):
        """
        Получения уровня доступа сотрудника по логину и паролю
        :param login: логин
        :param password: пароль
        :return: возвращает число 1-3
        """
        s=f"""
            SELECT access_level FROM access 
            INNER JOIN staff ON access.id=staff.access_id 
            WHERE staff.password='{password}' AND staff.login='{login}'
        """
        with con:
            data = con.execute(s)
            return data.fetchall()[0][0]

    def get_products_from_warehouse(self,warehouse_name:str):
        """
        Получение данных продуктов на складе для таблицы продуктов (id, product_name, category, vendor_code, quantity, price, delivery_date,expiration_date)
        :param warehouse_name: название склада
        :return: возвращает список кортежей
        """
        s=f"""
            SELECT products.id, product_name, category, vendor_code, quantity, products.price, delivery_date,expiration_date FROM products
            INNER JOIN warehouseProduct ON products.id = warehouseProduct.product_id 
            INNER JOIN warehouse ON warehouse.id = warehouseProduct.warehouse_id 
            WHERE warehouse.warehouse_name='{warehouse_name}'
            """
        with con:
            data = con.execute(s)
            return data.fetchall()

    def get_product_cart(self,product_id:int):
        """
        Получение данных товара для карты товара
        :param product_id: id товара
        :return: возвращает кортеж с данными товара из таблицы products
        """
        s=f"SELECT * FROM products WHERE id={product_id}"
        with con:
            data=con.execute(s)
            return data.fetchall()[0]

    def get_all_users(self):
        """
        Получение информации о всех клиентах для таблицы клиентов
        :return: список кортежей
        """
        s="SELECT id, first_name, last_name, surname, address FROM users"
        with con:
            data=con.execute(s)
            return data.fetchall()

    def get_user_cart(self,user_id:int):
        """
        Получение всех всех данных клиента для карты клиента
        :param user_id: id пользователя
        :return: кортеж с данными
        """
        s=f"SELECT * FROM users WHERE id={user_id}"
        with con:
            data=con.execute(s)
            return data.fetchall()[0]

    def get_user_orders(self, user_id: int):
        query_orders = "SELECT id, total_price, order_date FROM orders " \
                       "WHERE user_id = ?"

        query_products = "SELECT products.product_name, orderDetail.quantity FROM orderDetail " \
                         "JOIN products ON orderDetail.product_id = products.id " \
                         "WHERE orderDetail.order_number = ?"

        with con:
            orders = con.execute(query_orders, (user_id,)).fetchall()

        orders = [list(i) for i in orders]

        for i in range(len(orders)):
            order_number = orders[i][0]
            with con:
                products = con.execute(query_products, (order_number,)).fetchall()
                dt = []
                for item in products:
                    if item:
                        name, quantity = item
                        dt.append(f"{name} - {quantity}шт")
                orders[i].append(", ".join(dt))

        return orders


    def get_warehouses_info(self):
        """
        Получение информаци о складах
        :return: список кортежей
        """
        s="SELECT id, warehouse_name, address, text_location, latitude,longitude FROM warehouse"
        with con:
            data=con.execute(s)
            return data.fetchall()

    def search_by_param(self,warehouse_name, **param) -> list:
        """
        Метод для поиска товаров по заданному параметру.

        :param warehouse_name: Название склада.
        :param param: Словарь с параметром, где ключ - название поля, значение - значение этого поля.
        :return: Список кортежей или пустой список.
        """
        p = ""
        for key, value in param.items():
            p += f"{key} LIKE '%{value}%'"
        p = "products." + p

        query = f"""
                SELECT products.id, product_name, category, vendor_code, quantity, products.price, delivery_date,expiration_date FROM products
                INNER JOIN warehouseProduct ON products.id = warehouseProduct.product_id 
                INNER JOIN warehouse ON warehouse.id = warehouseProduct.warehouse_id 
                WHERE warehouse.warehouse_name='{warehouse_name}' AND {p}
                """
        with con:
            return con.execute(query).fetchall()

    def addupdate_query(self, field, value, table_name, id):
        query = f"UPDATE {table_name} SET {field} = {value} WHERE id = {id}"
        self.queries_list.append(query)

workBD=MethosdBD()