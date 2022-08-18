import configparser
import os

config = configparser.ConfigParser()
config.add_section('path')
config.set('path', 'temp', 'temp_from_ftp')
config.set('path', 'result', 'temp_result/')
config.set('path', 'result_name', 'Okolita_result.csv')
config.set('path', 'download', 'temp_download')
config.set('path', 'main_path', os.path.realpath(__file__).replace(os.path.basename(__file__), ""))
config.add_section('ftp')
config.set('ftp', 'server', '138.201.56.185')
config.set('ftp', 'user', 'rekrut')
config.set('ftp', 'password', 'zI4wG9yM5krQ3d')
config.set('ftp', 'target', 'task.rar')
config.set('ftp', 'target_server', '138.201.56.185')
config.set('ftp', 'target_user', 'rekrut')
config.set('ftp', 'target_password', 'zI4wG9yM5krQ3d')
config.add_section('sql')
config.set('sql', 'user', 'test')
config.set('sql', 'pass', 'pass_test')
config.set('sql', 'ip', '127.0.0.1')
config.set('sql', 'datebase', 'TEST')
config.set('sql', 'target',
           "SELECT data.main_part_number,data.manufacturer,data.category,data.origin,price.price,IFNULL(deposit.deposit,0) as deposit,(price.price + deposit.deposit) as final_price ,quantity.quantity,quantity.warehouse FROM data INNER JOIN price ON data.part_number=price.part_number INNER JOIN deposit ON data.part_number=deposit.part_number INNER JOIN quantity ON data.part_number=quantity.part_number WHERE (price.price + deposit.deposit)>2.00 and quantity.quantity > 0 AND quantity.warehouse LIKE 'A' OR quantity.warehouse LIKE 'h' OR quantity.warehouse LIKE 'j' OR quantity.warehouse LIKE '3' OR quantity.warehouse LIKE '9';")
config.add_section('depend')
config.set('depend', '0', 'python3-pip')
if os.path.isfile('config.ini'):
    configfile = open("config.ini", "w")
else:
    configfile = open("config.ini", "x")
config.write(configfile)
configfile.close()
