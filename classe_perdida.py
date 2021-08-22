from config import *

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    cidade = db.Column(db.String(254))
    bairro = db.Column(db.String(254))
    senha = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'{self.id}, {self.nome}, '+\
               f'{self.email}, {self.telefone}, ' +\
                f'{self.cidade}, {self.bairro}, ' +\
                f'{self.senha}'
    
    # método padrão json
    def json(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "email" : self.email,
            "telefone" : self.telefone,
            "cidade" : self.cidade,
            "bairro" : self.bairro,
            "senha" : self.senha
        }


# classe filha Perdido para lista de animais cadastrados como perdidos
class Perdido(Pessoa):
    # atributos do animal perdido
    id_perdido = db.Column(db.Integer, primary_key=True)
    nome_perdido = db.Column(db.String(254))
    idade = db.Column(db.String(254))
    sexo = db.Column(db.String(254))
    tamanho = db.Column(db.String(254))
    pelagem = db.Column(db.String(254))
    especie = db.Column(db.String(254))
    raca = db.Column(db.String(254))
    cor = db.Column(db.String(254))
    coleira = db.Column(db.String(254))
    descricao = db.Column(db.String(254))
    cidade_perdido = db.Column(db.String(254))
    bairro_perdido = db.Column(db.String(254))
    rua_perdido = db.Column(db.String(254))

    #chave estrangeira
    id_pessoa = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable= False)
    
    
    # método para expressar o animal perdido em forma de texto
    def __str__(self):
        return f'{self.id_perdido}, {self.nome_perdido}, '+\
               f'{self.idade}, {self.sexo}, ' +\
                f'{self.tamanho}, {self.pelagem}, ' +\
                f'{self.especie}, {self.raca}, ' +\
                f'{self.cor}, {self.coleira}, ' +\
                f'{self.descricao}, {self.cidade_perdido}, ' +\
                f'{self.bairro_perdido}, {self.rua_perdido}' 
    
    # método padrão json
    def json(self):
        return {
            "id" : self.id_perdido,
            "nome" : self.nome_perdido,
            "idade" : self.idade,
            "sexo" : self.sexo,
            "tamanho" : self.tamanho,
            "pelagem" : self.pelagem,
            "especie" : self.especie,
            "raca" : self.raca,
            "cor" : self.cor,
            "coleira" : self.coleira,
            "descricao" : self.descricao,
            "cidade" : self.cidade_perdido,
            "bairro" : self.bairro_perdido,
            "rua" : self.rua_perdido
        }

# teste das classe
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()
    
    # teste da classe Pessoa
    p1 = Pessoa(nome = "Aluisio", email = "aluisio@gmail.com", telefone = "11 1111-1111", 
                cidade = "cidade1", bairro =  "bairro1", senha = "senha1")
    p2 = Pessoa(nome = "Eloisa", email = "eloisamartins375@gmail.com", telefone = "22 2222-2222", 
                cidade = "cidade2", bairro =  "bairro2", senha = "senha2")       
    #persistir
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    todas = db.session.query(Pessoa).all()
    for p in todas:
        print(p)
        print(p.json())

    # teste da classe Perdido
    pet1 = Perdido(nome_perdido = "Dustin", idade = "2 anos", sexo = "macho", tamanho = "médio", pelagem = "curta", especie = "cachorro", raca = "vira-lata",
                cor = "caramelo" , coleira = "azul com bolinhas" , descricao = "cão agitado e carente, com rabo grande",
                cidade_perdido = "Indaial", bairro_perdido =  "João Paulo II", rua_perdido = "Santana")
    
    pet2 = Perdido(nome_perdido = "Lilica", idade = "1 anos", sexo = "fêmea", tamanho = "pequeno", pelagem = "longa", especie = "cachorro", raca = "vira-lata",
                cor = "preta" , coleira = " " , descricao = "cachorra que se assusta fácil, tem medo de outros animais",
                cidade_perdido = "Indaial", bairro_perdido =  "João Paulo II", rua_perdido = "Santana")
    
    # persistir
    db.session.add(pet1)
    db.session.add(pet2)
    db.session.commit()
    todos = db.session.query(Perdido).all()
    for pet in todos:
        print(pet)
        print(pet.json())