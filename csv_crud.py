import csv
import configparser
import errno
import os
import re
import DB_connector


class csv_crud:
    config_obj = configparser.ConfigParser()
    config_obj.read("config.ini")
    path_config = config_obj["path"]
    db_connect = DB_connector.db()
    def __init__(self):
        print("init")


    def to_csv(self):
        connect = DB_connector.db()
        path = self.path_config["main_path"]+self.path_config["result"]
        try:
                os.makedirs(path)
        except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        fp = open(path+self.path_config["result_name"], 'w')
        File = csv.writer(fp)
        File.writerows(connect.Custom_sql(self.config_obj["sql"]["target"]))
        fp.close()


    def clear_header(self,header):
        header = header[2:-2]
        header = header.split(";")
        return header

    def clear_row(self, row):
        row = row[2:-2].replace("\"","").replace("<","").replace(">","").replace(",",".").replace(" '","").replace("'","")
        #print(row)
        row=row.split(";")
        #print(row)
        return row

    def count_lines(self,filename, chunk_size=1 << 13):
        with open(filename) as file:
            return sum(chunk.count('\n')
                       for chunk in iter(lambda: file.read(chunk_size), ''))
    def re_add_one_column(self,name):
        files = os.listdir(self.path_config["main_path"] + "/" + self.path_config["temp"])
        print("current files :", files)
        for i in range(0, len(files)):
            if re.match(name+".csv", files[i]):
                print("\n" + files[i])
                with open(self.path_config["temp"] + "/" + files[i], 'r', encoding='utf-8-sig') as file:
                    csvreader = csv.reader(file)
                    header = next(csvreader)
                    self.db_connect.Create_Table(files[i].replace(".csv", ""), self.clear_header(str(header)))
                    check = self.count_lines(self.path_config["temp"] + "/" + files[i]) / 100
                    iterator = check
                    print(check * 100, " lines")
                    progress = 0

                    for row in csvreader:
                        if csvreader.line_num > iterator:
                            iterator += check
                            progress += 1
                            print(progress, "%")
                        # break
                        self.db_connect.Insert(files[i].replace(".csv", ""), self.clear_header(str(header)),
                                               self.clear_row(str(row)))
#CRUD
    def add_to_sql(self):

        files = os.listdir(self.path_config["main_path"]+"/"+self.path_config["temp"])
        print("current files :",files)
        for i in range(0,len(files)):
            if re.match(".*\.csv", files[i]):
                print("\n"+files[i])
                with open(self.path_config["temp"]+"/"+files[i], 'r' , encoding='utf-8-sig') as file:
                    csvreader = csv.reader(file)
                    header = next(csvreader)
                    self.db_connect.Create_Table(files[i].replace(".csv",""),self.clear_header(str(header)))
                    check=self.count_lines(self.path_config["temp"]+"/"+files[i])/100
                    iterator=check
                    print(check*100," lines")
                    progress = 0

                    for row in csvreader:
                        if csvreader.line_num>iterator:
                            iterator+=check
                            progress+=1
                            print(progress,"%")
                           # break
                        self.db_connect.Insert(files[i].replace(".csv",""),self.clear_header(str(header)),
                                              self.clear_row(str(row)))
            else:
                print("\n" + files[i])
                with open(self.path_config["temp"] + "/" + files[i], 'r', encoding='utf-8-sig') as file:
                    header=file.readline().split()
                    self.db_connect.Create_Table(files[i].replace(".txt", ""), header)
                    print(header)
                    check = self.count_lines(self.path_config["temp"] + "/" + files[i]) / 100
                    chekpoint=check
                    iterator = 0
                    progress = 0
                    print(check * 100, " lines")
                    for line in file:
                        line = line.split()
                        if iterator>chekpoint:
                            chekpoint+=check
                            progress+=1
                            print(progress,"%")
                            #break
                        iterator += 1
                        self.db_connect.Insert(files[i].replace(".txt", ""), header,(line[0]+" "+line[1]+"," + ",".join(line[2:])).split(","))
        print("complete)")
        self.complete_sql_adding()

    def complete_sql_adding(self):
        self.db_connect.Custom_sql("ALTER TABLE quantity MODIFY quantity  INT(5);")
        self.db_connect.Custom_sql("ALTER TABLE deposit MODIFY deposit  INT(5) ;")
        self.db_connect.Custom_sql("ALTER TABLE price MODIFY price  INT(5) ;")