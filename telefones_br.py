import re

class Telefone():
    def __init__(self, numero):
        if self.valida(numero):
            self.telefone = numero
        else:
            raise ValueError("Numero inválido")

    def __str__(self):
        return self.formata()

    def valida(self, numero):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, numero)
        if resposta:
            return True
        return False

    def formata(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.telefone)
        return "+{} ({}) {}-{}".format(resposta.group(1),resposta.group(2),resposta.group(3),resposta.group(4))
