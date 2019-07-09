import re

if __name__ == "__main__":
    adresses = ["Rua Marechal Floriano, 405 - segundo andar. CEP 96810-002",
                "Rua 7 de setembro, 59, apto 302, CEP 96810-016",
                "Rua Vinte e Oito de Setembro, 1997, CEP 96814-200"]

    for adress in adresses:
        adress_list = re.split(r", | - |\. CEP", adress)
        print(adress_list)
