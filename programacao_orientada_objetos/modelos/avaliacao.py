class Avaliacao:

    #Construtor
    def __init__(self, cliente, nota):
        self._cliente = cliente #boas praticas de programação, deixar protegido o atributo com _
        self._nota = nota