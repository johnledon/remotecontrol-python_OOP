from rich.panel import Panel
from rich import print
from ex021 import quebrarlinha

class ControleRemoto:
    def __init__(self):
        self.canal_atual = 1
        self.volume_atual = 0
        return

    def canal_cores(self,canal):
        if self.canal_atual == canal:
            return f' [white on yellow] {canal} [/] '
        else:
            return f'  {canal}  '

    def volume_cores(self):
        return f'{'[black on green]     [/]'*self.volume_atual}{'[black on white]     [/]'*(5-self.volume_atual)}'



    def logica_init(self):
        r = ''
        while True:
            while r.count('@') % 2 == 0:
                print(Panel(':prohibited: [red]A TV está desligada[/]', title_align='center',title='[black bold on white][TV][/]',width=40,height=5, subtitle='-LIGAR/DESLIGAR: |@| -ENCERRAR: |0| '))
                print(f'\n< CH1 >   - VOL: 0 + ', end='')
                r += input(': ')
                quebrarlinha(10)
                if r[-1] == '0':
                    return
            quebrarlinha(10)
            while r.count('@') % 2 != 0:
                print(Panel(f'CANAL  ={self.canal_cores(1):<3}{self.canal_cores(2):<3}{self.canal_cores(3):<3}{self.canal_cores(4):<3}{self.canal_cores(5):<3}\n'
                            f'VOLUME = {self.volume_cores()}', title_align='center', title='[black bold on white][TV][/]', width=40, height=5,subtitle='-LIGAR/DESLIGAR: |@| -ENCERRAR: |0|' ))
                print(f'\n< CH{self.canal_atual} >   - VOL: {self.volume_atual} + ', end='')
                r += '.'
                r += input(': ')
                if r[-1] == '>':
                    self.canal_atual += 1
                    if self.canal_atual == 6:
                        self.canal_atual = 1
                if r[-1] == '<':
                    self.canal_atual -= 1
                    if self.canal_atual == 0:
                        self.canal_atual = 5
                if r[-1] == '+':
                    self.volume_atual += 1
                    if self.volume_atual == 6:
                        self.volume_atual = 5
                if r[-1] == '-':
                    self.volume_atual -= 1
                    if self.volume_atual == -1:
                        self.volume_atual = 0
                quebrarlinha(10)
                if r[-1] == '0':
                    return

c = ControleRemoto()
c.logica_init()
print(Panel('[bold red]FIM DO PROGRAMA!!', expand=False))
