import ftplib
import sys
import re
import configparser
import patoolib
import os
import errno

from log import log


# create config to file
# create depend file
# create deleting temp files
# clean code
class ftp_sc:
    config_obj = configparser.ConfigParser()
    config_obj.read("config.ini")
    ftp_config = config_obj["ftp"]
    path_config = config_obj["path"]
    ftp = ftplib.FTP

    def __init__(self):
        print('todo')
        self.connect()
        self.download()
        self.unzip(filename=self.ftp_config["target"])

    def connect(self):
        try:
            self.ftp = ftplib.FTP(self.ftp_config["server"])
            self.ftp.login(self.ftp_config["user"], self.ftp_config["password"])
        except:
            log(sys.exc_info())

    def download(self):
        try:
            path = self.path_config["main_path"] + self.path_config["download"]
            try:
                os.makedirs(path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            self.ftp.retrbinary('RETR %s' % self.ftp_config["target"], open(self.path_config["download"]+"/"+self.ftp_config["target"], 'wb').write)
            self.ftp.quit()
        except:
            log(sys.exc_info())

    def unzip(self, filename):
        path = self.path_config["main_path"] + self.path_config["temp"]
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        try:
            patoolib.extract_archive(self.path_config["download"]+"/"+self.ftp_config["target"], outdir=path)
            print('unzip')
        except:
            log(sys.exc_info())

    def find_file(self):
        Files = []
        try:
            for filename in self.ftp.nlst():
                if re.match(".*" + self.ftp_config["target"], filename):
                    Files.append(filename)
            print(Files[0])
            return Files[0] or "no matches"
        except:
            log(sys.exc_info())

    def send_file(self):
        print("sending to ftp")
        self.ftp = ftplib.FTP(self.ftp_config["target_server"])
        self.ftp.login(self.ftp_config["target_user"], self.ftp_config["target_password"])
        file = open(self.path_config["main_path"]+self.path_config["result"]+self.path_config["result_name"], 'rb')  # file to send
        self.ftp.storbinary('STOR /complete/'+self.path_config["result_name"], file)  # send the file
        file.close()  # close file and FTP
        self.ftp.quit()
        print("complete")