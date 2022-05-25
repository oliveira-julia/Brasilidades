from validate_docbr import CPF
from validate_docbr import CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta!")

class Cpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError ("CPF INVÁLIDO!")

    def __str__(self):
        return self.formata()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class Cnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError ("CNPJ INVÁLIDO!")

    def __str__(self):
        return self.formata()

    def valida(self,documento):
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(documento)

    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
