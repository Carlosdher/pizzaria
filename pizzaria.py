class User():
    def __init__ (self, nome):
        self.nome = nome

    def __str__ (self):
        return "%s" %(self.nome)

class Table ():
    def __init__ (self, user, cardapio = {}):
        self.user = user
        self.cardapio = cardapio

    def add_cardapio (self, produto, valor):
        self.cardapio[produto] = valor
        return self.cardapio

    def del_cardapio (self, produto):
        if produto in self.cardapio:
            del(self.cardapio[produto])
        else:
            return False

user = User('carlos')
mesa = Table(user)
print (mesa)
mesa.add_cardapio('pizza de macarrao', 12.50)
print (mesa.cardapio)
mesa.del_cardapio('pizza de macarrao')
print (mesa.cardapio)
print (id(mesa))
