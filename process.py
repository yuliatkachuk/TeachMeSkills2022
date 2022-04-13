import psutil
from colorama import Fore, Back, Style

class Psutil_proc():
    psutil_values = []

    def get(self):

        self.psutil_values.append((Back.BLUE + Fore.BLACK + "{:^7}".format('PID') +
                              "{:^25}".format('USER') +
                              "{:^7}".format('CPU%') +
                              "{:<7}".format('MEM%') +
                              "{:^25}".format('NAME') +
                              "{:^10}".format('STATUS') +
                              "{:<50}".format(' COMMAND'))
                             )
        for proc in psutil.process_iter(['pid', 'name', 'username', 'exe', 'cpu_percent', 'memory_percent', 'status']):
            if proc.info['exe'] is None:
                proc.info['exe'] = 'None'
            if len(proc.info['name']) > 30:
                s = proc.info['name']
                s = s[s.rfind('.', 1, s.rfind('.'), ) + 1:]
                proc.info['name'] = s
            if proc.info['username'] is None:
                continue
            else:
                self.psutil_values.append(Back.GREEN + Fore.BLACK + "{:>7}".format(proc.info['pid']) +
                                     "{:^25}".format(proc.info['username']) +
                                     "{:^5.2f}".format(proc.info['cpu_percent']) +
                                     "{:>5.2f}".format(proc.info['memory_percent']) +
                                     "{:>30}".format(proc.info['name']) +
                                     "{:^10}".format(proc.info['status']) +
                                     "{:<50}".format(proc.info['exe'])
                                     )

        return self.psutil_values

    def show(self):
        for i in self.psutil_values:
            print(i)