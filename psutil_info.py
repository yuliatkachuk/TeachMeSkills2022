import psutil
import colorama
from colorama import Fore, Back, Style
import os

colorama.init()
t = []
print('CPU%',psutil.cpu_percent())
print('CPU count', psutil.cpu_count())
print('CPU frequency', psutil.cpu_freq()[0])

print('virtual memory:'+str(round(int(psutil.virtual_memory().used)/1024/1024/1024,1))+'G/'
      + str(round(int(psutil.virtual_memory().total)/1024/1024/1024,0))+'G')

print('SWAP memory:'+str(round(int(psutil.swap_memory().used)/1024/1024/1024,1))+'G/'
      + str(round(int(psutil.swap_memory().total)/1024/1024/1024,0))+'G/' 
      + str(round(int(psutil.swap_memory().free)/1024/1024/1024,0))+'G')

print(Back.BLUE + Fore.BLACK + "{:^5}".format('PID'),
      "{:^20}".format('USER'),
      "{:^5}".format('CPU%'),
      "{:^5}".format('MEM%'),
      "{:^20}".format('NAME'),
      "{:^10}".format('STATUS'),
      "{:<50}".format('COMMAND')
      )

for proc in psutil.process_iter(['pid', 'name', 'username', 'exe','cpu_percent','memory_percent' , 'status']):
    table_of_process = proc.info
    if proc.info['username'] is None:
        proc.info['username'] = 'None'
    if proc.info['exe'] is None:
        proc.info['exe'] = 'None'
    print(Back.GREEN + Fore.BLACK + "{:>5}".format(proc.info['pid']),
          "{:>20}".format(proc.info['username']),
          "{:>2.2f}".format(proc.info['cpu_percent']),
          "{:>2.2f}".format(proc.info['memory_percent']),
          "{:>20}".format(proc.info['name']),
          "{:>10}".format(proc.info['status']),
           "{:<50}".format(proc.info['exe'])
          )