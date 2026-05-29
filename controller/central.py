# Arquivo: controllers/central.py
from core.dispositivos import Lampada, ArCondicionado, SmartTV, TomadaInteligente, ControleInfravermelho

class CentralIoT:
    def __init__(self):
        # A memória principal da casa: uma lista vazia aguardando aparelhos
        self.dispositivos = [] 

    def adicionar_dispositivo(self, aparelho):
        #Recebe um objeto (ex: Lampada) e guarda na lista da casa.
        self.dispositivos.append(aparelho)
        return f"> Sucesso: '{aparelho.nome}' foi adicionado ao cômodo '{aparelho.comodo}'."

    def listar_todos(self):
        """Varre a lista e pede o status de cada aparelho."""
        if not self.dispositivos:
            return "Nenhum dispositivo cadastrado na central."
            
        relatorio = ["--- STATUS DA CASA ---"]
        for aparelho in self.dispositivos:
            relatorio.append(aparelho.obter_status())
        
        # Junta a lista em um texto com quebras de linha para ficar bonito no terminal
        return "\n".join(relatorio) 

    def buscar_aparelho(self, nome_aparelho, comodo):
        #Procura um aparelho específico na lista para podermos controlá-lo.
        for aparelho in self.dispositivos:
            # Transforma tudo em minúsculo (.lower()) para evitar erros de digitação do usuário
            if aparelho.nome.lower() == nome_aparelho.lower() and aparelho.comodo.lower() == comodo.lower():
                return aparelho
        return None  # Retorna vazio se não achar nada