import psutil

class Psutil_cpu():
    psutil_values = {}
    template = '\n'

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
    def show(self):
        self._prepare()
        print(self.template.format(**self.psutil_values))
