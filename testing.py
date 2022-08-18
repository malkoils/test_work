import unittest

import DB_connector
from csv_crud import csv_crud
from ftp_sc import ftp_sc


class MyTestCase(unittest.TestCase):
    # def test_sql(self):
    #     test = DB_connector.db()
    # test.clear_tables()
    #     while(True):
    #        test.Custom_sql(input("SQL> "))
    #

    # def test_csv_crud_test(self):
    # test2 = DB_connector.db()
    # test2.clear_tables()
    # test = csv_crud()
    # test.to_csv()
    # test.add_to_sql()
    # test.re_add_one_column("deposit")

    def test_tcp(self):
        test = ftp_sc()
        # print(test.find_file())
        test.send_file()


if __name__ == '__main__':
    unittest.main()
