import os
import logging

#print(os.getcwd())
def logger():
    file_name = 'test123.csv'

    #print(os.path.dirname(os.getcwd()))
    #dir=os.path.join(os.path.dirname(os.getcwd()),'log')
    #print(dir)logs
    log_dir=os.path.join(os.getcwd(),'logs')
    print(log_dir)
    if os.path.exists(log_dir):
        pass
    else:
        os.mkdir(log_dir)
    log_file=os.path.join(log_dir,file_name)
    print(log_file)
    if os.path.exists(log_file):
        os.remove(log_file)
    else:
        pass
    log_format = '%(levelname)s %(asctime)s - %(message)s'
    logging.basicConfig(filename = log_file,level = logging.DEBUG,format = log_format,filemode = 'w')
    loger = logging.getLogger()
    #loger.debug("Maniya Lal")
    print(loger.level)
    return loger

#logger()