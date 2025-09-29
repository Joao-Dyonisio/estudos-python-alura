# 1) Crie uma classe chamada `ContaBancaria` com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False # Atributo protegido

#2) Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self.saldo}"
    
    def ativar_conta(self):
        self._ativo = not self._ativo

#Crie duas instâncias da classe e imprima essas instâncias. 
conta1 = ContaBancaria("João", 2600)
conta2 = ContaBancaria("Maria", 1500)

print(conta1)
print(conta2)

conta3 = ContaBancaria("Carlos", 500)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")

ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")


class ClienteBanco:
    def __init__(self, nome, saldo, idade, cpf):
        self.nome = nome
        self.saldo = saldo
        self.idade = idade
        self.cpf = cpf
        self._ativo = False # Atributo protegido

cliente1 = ClienteBanco("Eduardo", 500, 20, 54612345690)
cliente2 = ClienteBanco("Maria", 600, 21, 54612345690)
cliente3 = ClienteBanco("Luiza", 700, 31, 54612345690)
