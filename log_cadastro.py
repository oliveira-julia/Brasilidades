from datetime import datetime, timedelta

class Tempo:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata()

    def formata(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro