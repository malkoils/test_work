import ftplib
import re
import traceback
import patoolib
import os
class ftp_sc:
    ftp_server = "138.201.56.185"
    ftp_user = "rekrut"
    ftp_pass = "zI4wG9yM5krQ3d"
    name_file = "task.rar"
    ftp = ftplib.FTP
    def __init__(self):
        self.connect()
        self.download()
       # ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
       # ftp.quit()

    def connect(self):
        try:
            self.ftp = ftplib.FTP(self.ftp_server)
            self.ftp.login(self.ftp_user, self.ftp_pass)
        except Exception:
            traceback.print_exc()
    def download(self):
        try:
            filename = self.find_file()
            #self.ftp.cwd(filename)
            self.ftp.retrbinary(filename, open(filename, 'wb').write)
            self.ftp.quit()
            if re.match(".*rar", filename):
               # os.mkdir("unzip")
                patoolib.extract_archive(filename, outdir="/unzip")
                print('unraring')
        except Exception:
            traceback.print_exc()

    def find_file(self):
        Files = []
        for filename in self.ftp.nlst():
            if re.match(".*"+self.name_file, filename):
                Files.append(filename)
        print(Files)
        return Files[0] or "no matches"