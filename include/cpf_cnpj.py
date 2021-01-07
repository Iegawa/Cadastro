from validate_docbr import CPF, CNPJ

class Documento():
    @staticmethod
    def criaDocumento(documento):
        tamanho_documento = len(str(documento))
        if tamanho_documento == 11:
            return Cpf(documento)
        elif tamanho_documento == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Quantidade de digitos incorreta")


class Cpf():
    def __init__(self, documento):
        if self.valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.formatar()

    def valido(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def formatar(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class Cnpj():
    def __init__(self, documento):
        if self.valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")
    
    def __str__(self):
        return self.formatar()
    
    def valido(self, documento):
        validador = CNPJ()
        return validador.validate(documento)   

    def formatar(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
