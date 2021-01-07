from cpf_cnpj import *
from telefones_br import *
from datas_br import *
from acesso_cep import *


documento = Documento()
print(documento.criaDocumento("12345678912"))

tel = Telefone("551112345678")
print(tel)

data = Data()
print(data.tempoCadastro())

cep = Cep("12345678")
# print(cep.acessaViaCep().json())
# print(cep.acessaViaCep().text)
bairro,cidade,estado = cep.acessaViaCep()
print(bairro, cidade, estado)