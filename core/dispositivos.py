from core.base import Dispositivo

class Lampada(Dispositivo):
    def __init__(self, nome, comodo):
        # O super() chama o __init__ da classe pai (Dispositivo)
        super().__init__(nome, comodo) 
        self.brilho = 100
        self.cor = "Branca"

    def ajustar_brilho(self, valor):
        if self.ligado:
            self.brilho = valor
            return f"Brilho da {self.nome} ajustado para {self.brilho}%."
        return f"A {self.nome} precisa estar ligada para ajustar o brilho."

    def obter_status(self):
        estado = "Ligada" if self.ligado else "Desligada"
        return f"[{estado}] {self.nome} ({self.comodo}) | Brilho: {self.brilho}% | IP: {self.ip}"


class ArCondicionado(Dispositivo):
    def __init__(self, nome, comodo):
        super().__init__(nome, comodo)
        self.temperatura = 23
        self.modo = "Resfriar"

    def ajustar_temperatura(self, valor):
        if self.ligado:
            self.temperatura = valor
            return f"Temperatura do {self.nome} ajustada para {self.temperatura}°C."
        return f"O {self.nome} precisa estar ligado para mudar a temperatura."

    def obter_status(self):
        estado = "Ligado" if self.ligado else "Desligado"
        return f"[{estado}] {self.nome} ({self.comodo}) | Temp: {self.temperatura}°C ({self.modo}) | IP: {self.ip}"


class SmartTV(Dispositivo):
    def __init__(self, nome, comodo):
        super().__init__(nome, comodo)
        self.volume = 20
        self.canal = "HDMI 1"

    def mudar_canal(self, novo_canal):
        if self.ligado:
            self.canal = novo_canal
            return f"{self.nome} mudou para {self.canal}."
        return f"A {self.nome} está desligada."

    def obter_status(self):
        estado = "Ligada" if self.ligado else "Desligada"
        return f"[{estado}] {self.nome} ({self.comodo}) | Canal: {self.canal} | Vol: {self.volume} | IP: {self.ip}"


class TomadaInteligente(Dispositivo):
    def __init__(self, nome, comodo):
        super().__init__(nome, comodo)
        self.consumo_atual_w = 0  # Consumo em Watts

    def definir_consumo(self, watts):
        # Só registra consumo se a tomada estiver passando energia (ligada)
        if self.ligado:
            self.consumo_atual_w = watts
            return f"{self.nome} agora está consumindo {self.consumo_atual_w}W."
        return f"{self.nome} está desligada. Não há consumo de energia."

    def obter_status(self):
        estado = "Ligada" if self.ligado else "Desligada"
        consumo = self.consumo_atual_w if self.ligado else 0
        return f"[{estado}] {self.nome} ({self.comodo}) | Consumo: {consumo}W | IP: {self.ip}"


class ControleInfravermelho(Dispositivo):
    def __init__(self, nome, comodo):
        super().__init__(nome, comodo)
        self.aparelhos_pareados = []  # Lista vazia de controles aprendidos

    def aprender_controle(self, nome_aparelho):
        # Adiciona um aparelho "bobo" (ex: "Portão da Garagem", "TV Antiga") na memória
        if self.ligado:
            if nome_aparelho not in self.aparelhos_pareados:
                self.aparelhos_pareados.append(nome_aparelho)
                return f"{self.nome} clonou o controle do(a) {nome_aparelho}."
            return f"O {self.nome} já conhece os comandos do(a) {nome_aparelho}."
        return f"Ligue o {self.nome} primeiro para aprender controles."

    def enviar_comando_ir(self, nome_aparelho, comando):
        # Finge disparar o laser IR para o aparelho específico
        if not self.ligado:
            return f"Erro: {self.nome} está desligado."
            
        if nome_aparelho in self.aparelhos_pareados:
            return f">>> {self.nome} emitiu sinal IR para {nome_aparelho}: '{comando}'"
            
        return f"Erro: {self.nome} não tem o controle do(a) '{nome_aparelho}' salvo."

    def obter_status(self):
        estado = "Ligado" if self.ligado else "Desligado"
        # Transforma a lista de aparelhos num texto separado por vírgulas
        lista_aparelhos = ", ".join(self.aparelhos_pareados) if self.aparelhos_pareados else "Nenhum"
        return f"[{estado}] {self.nome} ({self.comodo}) | Pareados: [{lista_aparelhos}] | IP: {self.ip}"