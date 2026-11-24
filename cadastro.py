class Partici():
    nome = ""
    email = ""
    tel = 0
    cep = 0
    alt = 0

    def __init__(self, nome, email, tel, cep, alt):
        self.nome = nome
        self.email = email
        self.tel = tel
        self.cep = cep
        self.alt = alt

    def cadastrar(self):
        for i in range(0, 5):
            self.nome = input("Qual é o seu nome?")
            self.email = input("Qual é o seu e-mail?")
            self.tel = input("Qual é o seu telefone?")
            self.cep = input("Qual é o seu CEP?")
            self.alt = input("Qual é a sua altura?")


pess1 = Partici(input("Qual é seu nome?"), input("Qual é seu email?"), input("Qual é o seu telefone?"), input("qual é o seu cep?"), input("Qual é a sua altura?"))

pess2 = Partici(input("Qual é seu nome?"), input("Qual é seu email?"), input("Qual é o seu telefone?"), input("qual é o seu cep?"), input("Qual é a sua altura?"))

pess3 = Partici(input("Qual é seu nome?"), input("Qual é seu email?"), input("Qual é o seu telefone?"), input("qual é o seu cep?"), input("Qual é a sua altura?"))

pess4 = Partici(input("Qual é seu nome?"), input("Qual é seu email?"), input("Qual é o seu telefone?"), input("qual é o seu cep?"), input("Qual é a sua altura?"))

pess5 = Partici(input("Qual é seu nome?"), input("Qual é seu email?"), input("Qual é o seu telefone?"), input("qual é o seu cep?"), input("Qual é a sua altura?"))
