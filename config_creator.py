import configparser
import os
config = configparser.ConfigParser()
config.add_section('path')
config.set('path', 'temp', 'temp_from_ftp')
config.set('path', 'result', 'temp_result')
config.add_section('ftp')
config.set('ftp', 'server', '138.201.56.185')
config.set('ftp', 'user', 'rekrut')
config.set('ftp', 'password', 'zI4wG9yM5krQ3d')
config.set('ftp', 'target', 'task.rar')
config.set('ftp', 'target_server', '138.201.56.185')
config.set('ftp', 'target_user', 'rekrut')
config.set('ftp', 'target_password', 'zI4wG9yM5krQ3d')
config.add_section('sql')
config.set('sql', 'admin', 'no')
config.add_section('depend')
config.set('depend', '0', 'python3-pip')
if os.path.isfile('config.ini'):
    configfile = open("config.ini", "w")
else:
    configfile = open("config.ini", "x")
config.write(configfile)
configfile.close()