from abc import ABC, abstractmethod
import random

class Dispositivo(ABC): # Cria a classe molde e garante que ela seja abstrata
    def __init__(self, nome, comodo): 
        self.id = random.randint(1000, 9999) # Simula um ID único no banco de dados
        self.nome = nome 
        self.comodo = comodo
        self.ligado = False
        self.ip = f"192.168.0.{random.randint(2, 254)}" # F-string gerando IP dinâmico

    def verificar_conexao(self):
        """
        No MVP: Finge que está checando a rede e sempre retorna True (Mocking).
        No Sistema Final: Aqui entra um ping real no self.ip.
        """
        return True 

    def ligar(self):
        # O sistema checa a conexão ANTES de mudar o status
        if self.verificar_conexao(): 
            self.ligado = True
            return f"{self.nome} ligado com sucesso."
        return f"Falha na rede: {self.nome} ({self.ip}) não está respondendo."
    
    def desligar(self):
        # O sistema checa a conexão ANTES de mudar o status
        if self.verificar_conexao():
            self.ligado = False
            return f"{self.nome} desligado com sucesso."
        return f"Falha na rede: {self.nome} ({self.ip}) não está respondendo."

    @abstractmethod
    def obter_status(self):
        pass