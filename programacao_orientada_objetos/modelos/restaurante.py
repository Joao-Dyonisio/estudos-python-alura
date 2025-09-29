from avaliacao import Avaliacao

#Classe (Letra  Maiuscula)
class Restaurante:
    restaurantes = [] #Lista

    #Construtor
    def __init__(self, nome, categoria):  # self (this) é a referência da instância do objeto naquele momento (eu quero esses valores)

        #this, referente ao objeto, não é um padrão do Python. 
        # O padrão do Python é o chamado self. Mas, se executarmos o programa, ele funciona normalmente.

        self._nome = nome.title() # com objeto _ (esta protegendo ele) não tem como alterar o valor dele
        self._categoria = categoria.upper() 
        self._ativo = False
        self._avaliacao = [] #Lista
        Restaurante.restaurantes.append(self)

    # Métodos especiais (já existe e contém dois __)
    # Mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f"{self._nome} | {self.categoria}" 
    
    #Criando um próprio método
    @classmethod #@classmethod e estamos utilizando informações referentes a esse método, podemos colocar como argumento entre os parênteses do método um cls
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} |{'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)}|{restaurante.ativo}')
    
    @property
    #utilizarmos @property, queremos modificar como aquele atributo vai ser lido.
    #@property, temos a capacidade de pegar um atributo — neste caso, o ativo
    def ativo(self):
        return "☒" if self._ativo else "☐"
    
    #Esse método, diferente do método de listar restaurantes,
    #não é um método para a classe restaurante, mas para os objetos. Então ele não é um @classmethod.
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao: #Se tiver nenhuma avaliacao, retorna ZERO (0)
            return '-'
        
        #soma de todas as notas, utilizando o "sum"(para cada avaliacao nossa lista, só quero pegar o nota(avaliacao._nota))
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao) # quantidade de notas utilizando o len
        media = round(soma_das_notas / quantidade_de_notas, 1) # media, com 1 casa decimal utilizando o round
        return media