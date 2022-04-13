from abc  import ABC, abstractmethod
import psutil
import colorama
from colorama import Fore, Back, Style
from process import Psutil_proc

class Utilabc(ABC):

    psutil_values = {}
    template = ''

    @abstractmethod
    def get():
        pass

    @abstractmethod
    def _prepare(self):
        pass

    def show(self):
        self._prepare()
        print(self.template.format(**self.psutil_values))


class Psutil_cpu(Utilabc):
    #psutil_values = {}
    #template = '\n'

    def get(self):
        self.psutil_values.update(count=['CPU count '+str(psutil.cpu_count())])
        self.psutil_values.update(frequency =['CPU frequency '+ str(s.current) for s in psutil.cpu_freq(percpu=True)])
        self.psutil_values.update(percent=['CPU percent '+str(psutil.cpu_percent(interval=1))])

    def _prepare(self):
        for i in range(len(self.psutil_values['count'])):
            self.template += '{count[' + str(i) + ']}\n'
        for i in range(len(self.psutil_values['frequency'])):
             self.template += '{frequency['+ str(i)  + ']}\n'
        for i in range(len(self.psutil_values['percent'])):
             self.template += '{percent['+ str(i)  + ']}\n'

class Psutil_mem(Utilabc):

    def get(self):
        self.psutil_values.update(virtual_memory=['virtual_memory used '+str(round(int(psutil.virtual_memory().used) / 1024 / 1024 / 1024, 1))+'Gb' , 'virtual_memory total '+str(round(int(psutil.virtual_memory().total) / 1024 / 1024 / 1024, 0))+'Gb'])
        self.psutil_values.update(SWAP_memory= ['SWAP_memory used '+str(round(int(psutil.swap_memory().used) / 1024 / 1024 / 1024, 1)) +'Gb', 'SWAP_memory total '+str(round(int(psutil.swap_memory().total) / 1024 / 1024 / 1024, 0))+'Gb' , 'SWAP_memory free '+str(round(int(psutil.swap_memory().free) / 1024 / 1024 / 1024, 0))+'Gb'])

    def _prepare(self):
        for i in range(len(self.psutil_values['virtual_memory'])):
            self.template += '{virtual_memory[' + str(i) + ']}\n'
        for i in range(len(self.psutil_values['SWAP_memory'])):
            self.template += '{SWAP_memory[' + str(i) + ']}\n'

def main():
    cpu = Psutil_cpu()
    mem = Psutil_mem()
    proc = Psutil_proc()

    cpu.get()
    cpu.show()
    mem.get()
    mem.show()
    proc.get()
    proc.show()

if __name__ == "__main__":
    colorama.init()
    main()