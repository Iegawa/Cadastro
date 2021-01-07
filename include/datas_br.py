from datetime import datetime, timedelta

class Data():
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata()

    def mesCadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def diaSemana(self):
        dias_da_semana = [
            "segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"
        ]
        dia_cadastro = self.momento_cadastro.weekday() 
        return dias_da_semana[dia_cadastro]

    def formata(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempoCadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro
