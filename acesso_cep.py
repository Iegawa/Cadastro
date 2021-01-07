import requests

class Cep():

    def __init__(self, cep):
        cep = str(cep)
        if self.cepValido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido")

    def __str__(self):
        return self.formata()

    def cepValido(self, cep):
        if len(cep) == 8:
            return True
        return False

    def formata(self):
        return "{}-{}".format(self.cep[:5],self.cep[5:])

    def acessaViaCep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados["bairro"],
            dados["localidade"]
        )