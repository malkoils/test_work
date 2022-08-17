from datetime import datetime
import os
def log(error):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if os.path.isfile('log_test.log'):
        f = open("log_test.log", "a")
    else:
        f = open("log_test.log", "x")
    f.write("\n\n"+dt_string+"\t"+str(error))
    f.close()