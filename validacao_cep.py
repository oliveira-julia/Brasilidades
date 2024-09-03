import requests
 
class Cep:
    def __init__(self, cep):
        cep = str(cep)
        if self.validacao(cep):
            self.cep = cep
        else:
            raise ValueError ("CEP INVÁLIDO")


    def __str__(self):
        return self.formata()

    def validacao(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formata(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acessa_viacep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        return (
            dados["logradouro"],
            dados ["bairro"],
            dados["localidade"],
            dados["uf"]
        )
