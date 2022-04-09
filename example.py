import psutil
import colorama
from colorama import Fore, Back, Style
import os

def psutil_cpu_pcnt():
    return 'cpu_percent '+str(psutil.cpu_percent())

def psutil_cpu_cnt():
    return 'cpu_count '+str(psutil.cpu_count())

def psutil_cpu_frq():
    return 'cpu_frequency '+str(psutil.cpu_freq()[0])

def psutil_vmemory():
    return 'virtual memory: '+str(round(int(psutil.virtual_memory().used)/1024/1024/1024,1))+'G/'\
           + str(round(int(psutil.virtual_memory().total)/1024/1024/1024,0))+'G'

def psutil_swmemory():
        return 'SWAP memory: '+str(round(int(psutil.swap_memory().used)/1024/1024/1024,1))+'G/'\
               + str(round(int(psutil.swap_memory().total)/1024/1024/1024,0))+'G/'\
               + str(round(int(psutil.swap_memory().free)/1024/1024/1024,0))+'G'
def f_print(a):
    print(a)


def psutil_process():

    print(Back.BLUE + Fore.BLACK + "{:^5}".format('PID'),
      "{:^20}".format('USER'),
      "{:^5}".format('CPU%'),
      "{:^5}".format('MEM%'),
      "{:^20}".format('NAME'),
      "{:^10}".format('STATUS'),
      "{:<50}".format('COMMAND')
      )
    for proc in psutil.process_iter(['pid', 'name', 'username', 'exe','cpu_percent','memory_percent' , 'status']):
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

if __name__ == "__main__":
    colorama.init()
    f_print(psutil_cpu_pcnt())
    f_print(psutil_cpu_cnt())
    f_print(psutil_cpu_frq())
    f_print(psutil_vmemory())
    f_print(psutil_swmemory())
    psutil_process()
