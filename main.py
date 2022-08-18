import ftp_sc
from csv_crud import csv_crud

test = ftp_sc.ftp_sc()
print(test.find_file())
test2 = csv_crud()
test2.add_to_sql()
test2.to_csv()
test.send_file()
