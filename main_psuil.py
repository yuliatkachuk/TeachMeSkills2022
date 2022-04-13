import psutil
import colorama
from colorama import Fore, Back, Style

from cpu import Psutil_cpu
from mem import Psutil_mem
from process import Psutil_proc
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
