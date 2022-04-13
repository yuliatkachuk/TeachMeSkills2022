import psutil

class Psutil_mem():
    psutil_values = {}
    template = ''

    def get(self):
        self.psutil_values.update(virtual_memory=['virtual_memory used '+str(round(int(psutil.virtual_memory().used) / 1024 / 1024 / 1024, 1))+'Gb' , 'virtual_memory total '+str(round(int(psutil.virtual_memory().total) / 1024 / 1024 / 1024, 0))+'Gb'])
        self.psutil_values.update(SWAP_memory= ['SWAP_memory used '+str(round(int(psutil.swap_memory().used) / 1024 / 1024 / 1024, 1)) +'Gb', 'SWAP_memory total '+str(round(int(psutil.swap_memory().total) / 1024 / 1024 / 1024, 0))+'Gb' , 'SWAP_memory free '+str(round(int(psutil.swap_memory().free) / 1024 / 1024 / 1024, 0))+'Gb'])

    def _prepare(self):
        for i in range(len(self.psutil_values['virtual_memory'])):
            self.template += '{virtual_memory[' + str(i) + ']}\n'
        for i in range(len(self.psutil_values['SWAP_memory'])):
            self.template += '{SWAP_memory[' + str(i) + ']}\n'
    def show(self):
        self._prepare()
        print(self.template.format(**self.psutil_values))