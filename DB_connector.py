import mysql.connector
import configparser

from mysql.connector import errorcode

from log import log


class db:
    cnx = mysql.connector
    config_obj = configparser.ConfigParser()
    config_obj.read("config.ini")
    sql_config = config_obj["sql"]
    cursor = cnx

    # sql_query = ""

    def __init__(self):
        self.cnx = mysql.connector.connect(user=self.sql_config['user'], password=self.sql_config['pass'],
                                           host=self.sql_config['ip'],
                                           )
        self.cursor = self.cnx.cursor()
        try:
            self.cursor.execute("USE %s" % self.sql_config["datebase"])
        except mysql.connector.Error as err:
            log(err)
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.Create_Database()
                self.cnx.database = self.sql_config["datebase"]
            else:
                log(err)

    def Create_Database(self):
        try:
            self.cursor.execute(
                "CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8'" % self.sql_config["datebase"])
        except mysql.connector.Error as err:
            log(err)

    def Update(self):
        print("Todo")

    def Delete(self):
        print("Todo")

    def Add(self):
        print("Todo")

    def clear_tables(self):
        SQL = "DROP TABLE price;DROP TABLE data;DROP TABLE deposit;DROP TABLE quantity;DROP TABLE weight;"
        try:
            print("Cleaning tables")
            self.cursor.execute(SQL)
        except mysql.connector.Error as err:
            log(err)

    # fast test mode
    # def Query_start(self,name,columns,value):
    #     self.sql_query+= "INSERT INTO " + name + " (" + ",".join(str(e) for e in columns) + ") VALUES ("+ ",".join(str(e) for e in value) + ");"

    #  def Query_end(self):
    #     try:
    #         self.cursor.execute(self.sql_query)
    #          self.sql_query=""
    # 3#     except mysql.connector.Error as err:
    #         log(err)

    #   CREATE TABLE new_table_name AS
    #    SELECT column1, column2,...
    #    FROM existing_table_name
    #    WHERE ....;

    def Create_Table(self, name, columns):
        SQL = "CREATE TABLE %s (" % name + " char(255),".join(str(e) for e in columns) + " char(255));"
        print(SQL)

        try:
            print("Creating table %s: " % name)
            self.cursor.execute(SQL)
        except mysql.connector.Error as err:
            log(err)
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    # INSERT
    #  INTO
    #   table_name(column1, column2, column3, ...)
    #  VALUES(value1, value2, value3, ...);

    ## slow but safety
    def Insert(self, name=" ", columns=" ", value=" "):
        SQL = "INSERT INTO " + name + " (" + ",".join(str(e) for e in columns) + ") VALUES (%s" + ",%s" * (
                len(columns) - 1) + ");"
        # print(SQL, value)
        try:
            self.cursor.execute(SQL, value)
            self.cnx.commit()  # slow but work when fast dont work
        except mysql.connector.Error as err:
            log(err)

    def Custom_sql(self, SQL):

        try:
            self.cursor.execute(SQL)
            rows = self.cursor.fetchall()
            return rows
        except mysql.connector.Error as err:
            log(err)

    def dissconnect(self):
        self.cnx.close()
