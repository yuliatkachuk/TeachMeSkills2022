import psutil
import colorama
from colorama import Fore, Back, Style
import os
import time

class Psutil_cls():

 psutil_name = None

 def __init__(self,name):
     self.psutil_name = name


 def get(self,psutil_name):
     psutil_values = []

     if psutil_name == 'CPU':
         psutil_values.append('CPU% ' + str(psutil.cpu_percent()))
         psutil_values.append('CPU count ' + str(psutil.cpu_count()))
         psutil_values.append('CPU frequency ' + str(psutil.cpu_freq()[0]))
     elif psutil_name == 'MEM':
         psutil_values.append('virtual memory: ' + str(round(int(psutil.virtual_memory().used) / 1024 / 1024 / 1024, 1)) + 'G/'
               + str(round(int(psutil.virtual_memory().total) / 1024 / 1024 / 1024, 0)) + 'G')
         psutil_values.append('SWAP memory: ' + str(round(int(psutil.swap_memory().used) / 1024 / 1024 / 1024, 1)) + 'G/'
               + str(round(int(psutil.swap_memory().total) / 1024 / 1024 / 1024, 0)) + 'G/'
               + str(round(int(psutil.swap_memory().free) / 1024 / 1024 / 1024, 0)) + 'G')
     elif psutil_name =='PROC':
         psutil_values.append((Back.BLUE + Fore.BLACK + "{:^7}".format('PID')+
               "{:^25}".format('USER')+
               "{:^7}".format('CPU%')+
               "{:<7}".format('MEM%')+
               "{:^25}".format('NAME')+
               "{:^10}".format('STATUS')+
               "{:<50}".format(' COMMAND'))
               )
         for proc in psutil.process_iter(['pid', 'name', 'username', 'exe', 'cpu_percent', 'memory_percent', 'status']):
             if proc.info['exe'] is None:
                 proc.info['exe'] = 'None'
             if len(proc.info['name'])>30:
                 s = proc.info['name']
                 s = s[s.rfind('.', 1, s.rfind('.'),)+1:]
                 proc.info['name'] = s
             if proc.info['username'] is None:
                 continue
             else:
                 psutil_values.append(Back.GREEN + Fore.BLACK + "{:>7}".format(proc.info['pid'])+
                                      "{:^25}".format(proc.info['username'])+
                                      "{:^5.2f}".format(proc.info['cpu_percent'])+
                                      "{:>5.2f}".format(proc.info['memory_percent'])+
                                      "{:>30}".format(proc.info['name'])+
                                      "{:^10}".format(proc.info['status'])+
                                      "{:<50}".format(proc.info['exe'])
                                      )
     return psutil_values


 def show(self,psutil_values):
     for i in psutil_values:
         print(i)


if __name__ == "__main__":

    colorama.init()

    Psutil_cls('CPU').show(Psutil_cls('CPU').get('CPU'))
    Psutil_cls('MEM').show(Psutil_cls('MEM').get('MEM'))
    Psutil_cls('PROC').show(Psutil_cls('PROC').get('PROC'))

    time.sleep(1)
    os.system('cls')



