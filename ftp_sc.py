import ftplib
import sys
import re
import configparser
import patoolib
import os
import errno

from log import log

#create config to file
#create depend file
class ftp_sc:
    config_obj = configparser.ConfigParser()
    config_obj.read("config.ini")
    ftp_config = config_obj["ftp"]
    path_config = config_obj["path"]
    ftp = ftplib.FTP
    filename = ftp_config["target"]


    def __init__(self):
        config_obj = configparser.ConfigParser()
        config_obj.read("config.ini")
        ftp_config = config_obj["ftp"]

        self.connect()
        self.download()

        self.unzip(filename=self.filename)

    def connect(self):
        try:
            self.ftp = ftplib.FTP(self.ftp_config["server"])
            self.ftp.login(self.ftp_config["user"], self.ftp_config["password"])
        except:
            log(sys.exc_info())

    def download(self):
        try:
            self.filename = self.find_file()
            self.ftp.cwd(self.filename)
            self.ftp.retrbinary('RETR %s' % self.filename, open(self.filename, 'wb').write)
            self.ftp.quit()
        except:
            log(sys.exc_info())

    def unzip(self,filename):
        path = os.path.realpath(__file__).replace(os.path.basename(__file__),"")+self.path_config["temp"]
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        try:
            patoolib.extract_archive(filename or self.filename, outdir=path)
            print('unzip')
        except:
            log(sys.exc_info())



    def find_file(self):
        Files = []
        try:
            for filename in self.ftp.nlst():
                if re.match(".*"+self.filename, filename):
                    Files.append(filename)
            print(Files)
        except:
            log(sys.exc_info())
        return Files[0] or "no matches"