# Importar toda a célula de código do restaurante para app.py

from restaurante import Restaurante

restaurante_praca = Restaurante("praça", "Gourmet")
restaurante_praca.receber_avaliacao("Gui", 10)
restaurante_praca.receber_avaliacao("João", 8)
restaurante_praca.receber_avaliacao("Emy", 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()