class Cliente:
    def __init__(self, mail, username, password, plano):
        self.mail = mail
        self.username = username
        self.password = password
        self.plano = plano
        self.filmesVistos = []
        self.SeriesVistas = []

    def VerFilme(self):
        filme = str(input("Qual filme sera visto?"))
        self.filmesVistos.append(filme)

    def VerSerie(self):
        serie = str(input("Qual filme sera visto?"))
        self.filmesVistos.append(serie)
        
    
lucas = Cliente("gmail", "user", "password", "mais barato")
lucas.VerFilme()
print(lucas.filmesVistos)
    
        
print('olá')