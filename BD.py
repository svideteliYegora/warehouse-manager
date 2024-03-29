import sqlite3 as sl
import time
from datetime import datetime, timezone

con = sl.connect('warehouseDB.db', check_same_thread=False)
cur=con.cursor()

with con:

    con.execute("""
        CREATE TABLE IF NOT EXISTS staff (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            surname VARCHAR(20),
            full_name varchar(100) GENERATED ALWAYS AS (last_name || ' ' || first_name || ' ' || surname),
            login VARCHAR(20),
            password VARCHAR(20),
            access_level INTEGER
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            surname VARCHAR(20),
            full_name varchar(100) GENERATED ALWAYS AS (last_name || ' ' || first_name || ' ' || surname),
            birthday INTEGER,
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
            products_id INTEGER,
            FOREIGN KEY (order_number) REFERENCES orders (id),
            FOREIGN KEY (products_id) REFERENCES products (id)
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS warehouseProduct (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            warehouse_id INTEGER,
            products_id INTEGER,
            quantity INTEGER,
            delivery_date INTEGER,
            expiration_date INTEGER,
            FOREIGN KEY (warehouse_id) REFERENCES warehouse (id),
            FOREIGN KEY (products_id) REFERENCES products (id)
        );
    """)

    con.execute("""
            CREATE TABLE IF NOT EXISTS deliveries (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                warehouse_id INTEGER,
                delivery_date INTEGER,
                provider VARCHAR(30),
                FOREIGN KEY (warehouse_id) REFERENCES warehouse (id)
            );
        """)

    con.execute("""
            CREATE TABLE IF NOT EXISTS delivery_contents (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                deliveries_id INTEGER,
                products_id INTEGER,
                quantity INTEGER,
                expiration_date INTEGER,
                FOREIGN KEY (deliveries_id) REFERENCES deliveries (id),
                FOREIGN KEY (products_id) REFERENCES products (id)
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
        with con:
            con.execute(s)

    def add_record(self, table: str, **param: dict):
        """
        Добавляет запись в указанную таблицу по указанным значениям в словаре
        :param table: имя таблицы
        :param param: словарь значений для записи в таблицу
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
            SELECT access_level FROM staff 
            
        """
        with con:
            data = con.execute(s).fetchall()
            if data:
                return data[0][0]
            return 0

    def get_products_from_warehouse(self,warehouse_name:str):
        """
        Получение товаров по выбранному одному складу
        :param warehouse_name: название склада
        :return: список списков
        """
        s=f"""
            SELECT warehouse.warehouse_name, product_name, category, vendor_code, quantity, products.price, delivery_date,expiration_date FROM products
            INNER JOIN warehouseProduct ON products.id = warehouseProduct.products_id 
            INNER JOIN warehouse ON warehouse.id = warehouseProduct.warehouse_id 
            WHERE warehouse.warehouse_name='{warehouse_name}'
            """
        with con:
            data = con.execute(s).fetchall()

            for i in range(len(data)):
                data[i]=list(data[i])

                unix_delivery_date=float(data[i][6])
                unix_expiration_date=float(data[i][7])
                unix_delivery_date=time.gmtime(unix_delivery_date)
                unix_expiration_date=time.gmtime(unix_expiration_date)
                data[i][6]= time.strftime("%m.%d.%Y",unix_delivery_date)
                data[i][7] = time.strftime("%m.%d.%Y" , unix_expiration_date)


            return data

    def get_products_from_all_warehouse(self):
        """
        получение товаров со всех складов сразу
        :return: список списков
        """
        s=f"""
            SELECT warehouse.warehouse_name, product_name, category, vendor_code, quantity, products.price, delivery_date,expiration_date FROM products
            INNER JOIN warehouseProduct ON products.id = warehouseProduct.products_id 
            INNER JOIN warehouse ON warehouse.id = warehouseProduct.warehouse_id 
            """
        with con:
            data = con.execute(s).fetchall()

            for i in range(len(data)):
                data[i]=list(data[i])

                unix_delivery_date=float(data[i][6])
                unix_expiration_date=float(data[i][7])
                unix_delivery_date=time.gmtime(unix_delivery_date)
                unix_expiration_date=time.gmtime(unix_expiration_date)
                data[i][6]= time.strftime("%m.%d.%Y",unix_delivery_date)
                data[i][7] = time.strftime("%m.%d.%Y" , unix_expiration_date)

            return data

    def search_products_in_warehouse(self,warehouse_name:str,**param:dict):
        """
        Получение товаров на заданном складе с заданнами параметрами поиска товара
        :param warehouse_name: название склада
        :param param: словарь с параметрами поиска
        :return: список списков
        """

        s=f"""
            SELECT warehouse.warehouse_name, product_name, category, vendor_code, quantity, products.price, delivery_date,expiration_date FROM products
            INNER JOIN warehouseProduct ON products.id = warehouseProduct.products_id 
            INNER JOIN warehouse ON warehouse.id = warehouseProduct.warehouse_id 
            WHERE warehouse.warehouse_name='{warehouse_name}' AND  
            """

        key = list(param.keys())
        final_param={}

        for i in range(len(param)):
            if param[key[i]]!=None:
                if param[key[i]].text() != "":
                    if key[i] in ("delivery_date","expiration_date"):
                        final_param[key[i]]=int(datetime.strptime(param[key[i]].text(),"%d.%m.%Y").replace(tzinfo=timezone.utc).timestamp())
                    else:
                        final_param[key[i]] = param[key[i]].text()

        key = list(final_param.keys())
        for i in range(len(final_param)):
            if i == len(final_param) - 1:
                s += f"{key[i]}='{final_param[key[i]]}'"
            else:
                s += f"{key[i]}='{final_param[key[i]]}' AND "

        with con:
            data = con.execute(s).fetchall()

            for i in range(len(data)):
                data[i]=list(data[i])

                unix_delivery_date=float(data[i][6])
                unix_expiration_date=float(data[i][7])
                unix_delivery_date=time.gmtime(unix_delivery_date)
                unix_expiration_date=time.gmtime(unix_expiration_date)
                data[i][6]= time.strftime("%m.%d.%Y",unix_delivery_date)
                data[i][7] = time.strftime("%m.%d.%Y" , unix_expiration_date)


            return data

    def search_products_in_all_warehouse(self,**param:dict):
        """
        Получение товаров по заданным параметрам поиска на всех складах сразу
        :param param: словарь параметров
        :return: список списков
        """

        s=f"""
            SELECT warehouse.warehouse_name, product_name, category, vendor_code, quantity, products.price, delivery_date,expiration_date FROM products
            INNER JOIN warehouseProduct ON products.id = warehouseProduct.products_id 
            INNER JOIN warehouse ON warehouse.id = warehouseProduct.warehouse_id 
            WHERE   
            """

        key = list(param.keys())
        final_param={}

        for i in range(len(param)):
            if param[key[i]]!=None:
                if param[key[i]].text() != "":
                    if key[i] in ("delivery_date", "expiration_date"):
                        final_param[key[i]] = int(datetime.strptime(param[key[i]].text(), "%d.%m.%Y").replace(tzinfo=timezone.utc).timestamp())
                    else:
                        final_param[key[i]] = param[key[i]].text()

        key = list(final_param.keys())
        for i in range(len(final_param)):
            if i == len(final_param) - 1:
                s += f"{key[i]}='{final_param[key[i]]}'"
            else:
                s += f"{key[i]}='{final_param[key[i]]}' AND "

        with con:
            data = con.execute(s).fetchall()

            for i in range(len(data)):
                data[i]=list(data[i])

                unix_delivery_date=float(data[i][6])
                unix_expiration_date=float(data[i][7])
                unix_delivery_date=time.gmtime(unix_delivery_date)
                unix_expiration_date=time.gmtime(unix_expiration_date)
                data[i][6]= time.strftime("%m.%d.%Y",unix_delivery_date)
                data[i][7] = time.strftime("%m.%d.%Y" , unix_expiration_date)

            return data

    def get_info_deliveryes_on_warehoouse(self, warehouse_name):
        """
        Метод для получения информации о поставках на заданном складе

        :param warehouse_name: Название склада.
        :return: Список кортежей или пустой список.
        """

        inf = f"""
            SELECT deliveries.id,warehouse_name, provider, delivery_date FROM deliveries
            INNER JOIN warehouse ON deliveries.warehouse_id = warehouse.id
            WHERE warehouse.warehouse_name = '{warehouse_name}'
            """
        with con:
            data = con.execute(inf).fetchall()

            for i in range(len(data)):
                data[i]=list(data[i])

                data[i][0]=f"№{data[i][0]}"

                unix_delivery_date=float(data[i][3])
                unix_delivery_date=time.gmtime(unix_delivery_date)
                data[i][3]= time.strftime("%m.%d.%Y",unix_delivery_date)

            return data

    def get_info_deliveryes_all_warehouse(self):
        """
        Метод для получения информации о поставках на всех складах.

        :return: Список списоков.
        """

        inf = f"""
            SELECT deliveries.id,warehouse_name, provider, delivery_date FROM deliveries
            INNER JOIN warehouse ON deliveries.warehouse_id = warehouse.id
            """
        with con:
            data = con.execute(inf).fetchall()


            for i in range(len(data)):
                data[i]=list(data[i])

                data[i][0]=f"№{data[i][0]}"

                unix_delivery_date=float(data[i][3])
                unix_delivery_date=time.gmtime(unix_delivery_date)
                data[i][3]= time.strftime("%m.%d.%Y",unix_delivery_date)

            return data


    def search_deliveryes_on_warehouse(self,warehouse_n:str,**param:dict):
        """
        Получение поставок на заданном складе по заданным параметрам посиска
        :param warehouse_n: название склада
        :param param: словарь параметров поиска
        :return: список списков
        """

        s=f"""
            SELECT deliveries.id,warehouse_name, provider, delivery_date FROM deliveries
            INNER JOIN warehouse ON deliveries.warehouse_id = warehouse.id
            WHERE warehouse.warehouse_name = '{warehouse_n}' AND
            """

        key = list(param.keys())
        final_param={}

        for i in range(len(param)):
            if param[key[i]]!=None:
                if param[key[i]].text() != "":
                    if key[i] =="delivery_date":
                        print(param[key[i]].text())
                        final_param[key[i]] = int(datetime.strptime(param[key[i]].text(), "%d.%m.%Y").replace(tzinfo=timezone.utc).timestamp())
                    else:
                        final_param[key[i]] = param[key[i]].text()
        key = list(final_param.keys())
        for i in range(len(final_param)):
            if i == len(final_param) - 1:
                s += f"{key[i]}='{final_param[key[i]]}'"
            else:
                s += f"{key[i]}='{final_param[key[i]]}' AND "

        with con:
            data = con.execute(s).fetchall()

            for i in range(len(data)):
                data[i]=list(data[i])

                data[i][0]=f"№{data[i][0]}"

                unix_delivery_date=float(data[i][3])
                unix_delivery_date=time.gmtime(unix_delivery_date)
                data[i][3]= time.strftime("%m.%d.%Y",unix_delivery_date)

            return data


    def search_deliveryes_all_warehouse(self,**param:dict):
        """
        Получение поставок на всех складах по заданным параметрам поиска
        :param param: словарь параметров поиска
        :return: список списков
        """
        s=f"""
            SELECT deliveries.id,warehouse_name, provider, delivery_date FROM deliveries
            INNER JOIN warehouse ON deliveries.warehouse_id = warehouse.id 
            WHERE   
            """

        key = list(param.keys())
        final_param={}

        for i in range(len(param)):
            if param[key[i]]!=None:
                if param[key[i]].text() != "":
                    if key[i] =="delivery_date":
                        final_param[key[i]] = int(datetime.strptime(param[key[i]].text(), "%d.%m.%Y").replace(
                            tzinfo=timezone.utc).timestamp())
                    else:
                        final_param[key[i]] = param[key[i]].text()

        key = list(final_param.keys())
        for i in range(len(final_param)):
            if i == len(final_param) - 1:
                s += f"{key[i]}='{final_param[key[i]]}'"
            else:
                s += f"{key[i]}='{final_param[key[i]]}' AND "

        with con:
            data = con.execute(s).fetchall()

            for i in range(len(data)):
                data[i] = list(data[i])

                data[i][0] = f"№{data[i][0]}"

                unix_delivery_date = float(data[i][3])
                unix_delivery_date = time.gmtime(unix_delivery_date)
                data[i][3] = time.strftime("%m.%d.%Y", unix_delivery_date)

            return data

    def get_warehouses_info(self):
        """
        Получение информаци о складах
        :return: список списков
        """
        s="SELECT * FROM warehouse"
        with con:
            data=con.execute(s).fetchall()

            for i in range(len(data)):
                data[i]=list(data[i])

                data[i][0]=f"№{data[i][0]}"
            return data


    def search_warehouse(self,**param:dict):
        """
        Получение инфы о складах по заданным параметрам поиска
        :param param: словарь параметров поиска
        :return: список кортежей
        """
        s = f"""
             SELECT * FROM warehouse
             WHERE   
             """

        key = list(param.keys())
        final_param = {}

        for i in range(len(param)):

            if param[key[i]] != None:
                if param[key[i]].text()!="":
                    final_param[key[i]] = param[key[i]]

        key = list(final_param.keys())
        for i in range(len(final_param)):
            if i == len(final_param) - 1:
                s += f"{key[i]}='{final_param[key[i]].text()}'"
            else:
                s += f"{key[i]}='{final_param[key[i]].text()}' AND "

        with con:
            data = con.execute(s)
            return data.fetchall()


    def get_all_users(self):
        """
        Получение информации о всех клиентах для таблицы клиентов
        :return: список списков
        """
        s="SELECT id,last_name,first_name,  surname,birthday,address,email FROM users"
        with con:
            data=con.execute(s).fetchall()

            for i in range(len(data)):
                data[i]=list(data[i])

                unix_delivery_date=float(data[i][4])
                unix_delivery_date=time.gmtime(unix_delivery_date)
                data[i][4]= time.strftime("%m.%d.%Y",unix_delivery_date)

            return data


    def search_users(self,**param):
        """
        Получение информации о клиентах по заданным параметрам поиска
        :param param: словарь параметров поиска
        :return: список списков
        """
        s="SELECT id,last_name,first_name,surname,birthday,address,email FROM users WHERE "

        key = list(param.keys())
        final_param = {}

        for i in range(len(param)):

            if param[key[i]] != None:
                if param[key[i]].text() != "":
                    if key[i] == "birthday":
                        final_param[key[i]] = int(datetime.strptime(param[key[i]].text(), "%d.%m.%Y").replace(
                            tzinfo=timezone.utc).timestamp())
                    else:
                        final_param[key[i]] = param[key[i]].text()
        key = list(final_param.keys())

        for i in range(len(final_param)):
            if i == len(final_param) - 1:
                if key[i]=='full_name':

                    s+=f"{key[i]} LIKE '%{final_param[key[i]]}%'"
                else:
                    s += f"{key[i]}='{final_param[key[i]]}'"
            else:
                if key[i]=="fool_name":
                    s+=f"{key[i]} LIKE '%{final_param[key[i]]}%' AND "
                else:
                    s += f"{key[i]}='{final_param[key[i]]}' AND "
        with con:
            data = con.execute(s).fetchall()
            for i in range(len(data)):
                data[i] = list(data[i])

                unix_delivery_date = float(data[i][4])
                unix_delivery_date = time.gmtime(unix_delivery_date)
                data[i][4] = time.strftime("%m.%d.%Y", unix_delivery_date)

            return data

    def get_staff(self):
        """
        получение информации о персонале
        :return: список кортежей
        """
        s="SELECT id,last_name,first_name,surname,login,password,access_level FROM staff"
        with con:
            return con.execute(s).fetchall()

    def search_staff(self,**param):
        """
        получение информации о персонали по заданным параметрам поиска
        :param param: словарь параметров поиска
        :return: список кортежей
        """

        s="SELECT id,last_name,first_name,surname,login,password,access_level FROM staff WHERE "

        key = list(param.keys())
        final_param = {}

        for i in range(len(param)):

            if param[key[i]] != None:
                if param[key[i]].text() != "":
                    final_param[key[i]] = param[key[i]]

        key = list(final_param.keys())

        for i in range(len(final_param)):
            if i == len(final_param) - 1:
                if key[i] == 'full_name':

                    s += f"{key[i]} LIKE '%{final_param[key[i]].text()}%'"
                else:
                    s += f"{key[i]}='{final_param[key[i]].text()}'"
            else:
                if key[i] == "fool_name":
                    s += f"{key[i]} LIKE '%{final_param[key[i]].text()}%' AND "
                else:
                    s += f"{key[i]}='{final_param[key[i]].text()}' AND "

        with con:
            data = con.execute(s).fetchall()
            return data

    def get_product_names(self):
        """
        Метод получения названий товаров
        :return: списо названий
        """
        s="SELECT product_name FROM products ORDER BY product_name"
        with con:
            data = con.execute(s)
            data = data.fetchall()
            data1 = []
            for i in data:
                data1.append(i[0])
            return data1

    def get_delivery_contents(self,id):
        s=f"SELECT product_name,quantity,expiration_date FROM delivery_contents JOIN products ON delivery_contents.products_id=products.id WHERE delivery_contents.deliveries_id={id}"
        print(s)
        with con:
            data=con.execute(s).fetchall()

        for i in range(len(data)):
            data[i] = list(data[i])

            unix_delivery_date = float(data[i][2])
            unix_delivery_date = time.gmtime(unix_delivery_date)
            data[i][2] = time.strftime("%m.%d.%Y", unix_delivery_date)

        return data

    def get_orders_content(self, order_number):
        order_content_query = ("SELECT orderDetail.quantity, products.product_name, products.price FROM orderDetail "
                               "JOIN products ON orderDetail.products_id = products.id "
                               "WHERE orderDetail.order_number = ?")

        with con:
            cursor = con.cursor()
            cursor.execute(order_content_query, (order_number,))
            result = cursor.fetchall()
            cursor.close()

            return result
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



    def addupdate_query(self, field, value, table_name, id):
        query = f"UPDATE {table_name} SET {field} = {value} WHERE id = {id}"
        self.queries_list.append(query)


    def get_staff_for_cmb(self):
        first_name="SELECT DISTINCT first_name FROM staff"
        last_name="SELECT DISTINCT last_name FROM staff"
        surname="SELECT DISTINCT surname FROM staff"
        access_level="SELECT DISTINCT access_id FROM staff"

        with con:
            return [con.execute(first_name).fetchall(),con.execute(last_name).fetchall(),con.execute(surname).fetchall(),con.execute(access_level).fetchall()]

    def edit_product(self, warehouse_product_id):
        try:
            with con:
                data = con.execute("SELECT products.id "
                                   "FROM warehouseProduct "
                                   "JOIN products "
                                   "ON products.id = warehouseProduct.product_id "
                                   "WHERE warehouseProduct.id = ?",(warehouse_product_id,)).fetchone()
        except Exception as e:
            print(e)
            return None

    def get_staff_for_cmb(self):
        first_name = "SELECT DISTINCT first_name FROM staff"
        last_name = "SELECT DISTINCT last_name FROM staff"
        surname = "SELECT DISTINCT surname FROM staff"
        access_level = "SELECT DISTINCT access_level FROM staff"

        with con:
            return [con.execute(first_name).fetchall(), con.execute(last_name).fetchall(),
                    con.execute(surname).fetchall(), con.execute(access_level).fetchall()]




workBD=MethosdBD()