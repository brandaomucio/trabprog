from peewee import *
import os 

arq = "bla.bd"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Funcionario(BaseModel):
    nome = CharField()
    salario = CharField()

class Cliente(BaseModel):
    nome = CharField()
    cpf = CharField()

class Fornecedor(BaseModel):
    nom_fornecedor = CharField()
    tempo_entrega = CharField()

class Maquinario(BaseModel):
    nome_maq = CharField()
    fornecedor_maq = ForeignKeyField(Fornecedor)

class Construtora(BaseModel):
    nom_empresa = CharField()
    clientes = ManyToManyField(Cliente)

class Engenheiro(BaseModel):
    nome = CharField()
    nom_empresa = ForeignKeyField(Construtora)

class Arquiteto(BaseModel):
    nome = CharField()
    nom_empresa = ForeignKeyField(Construtora)

class Material(BaseModel):
    nome_material = CharField()
    quantidade = CharField()
    fornecedor = ForeignKeyField(Fornecedor)

class Equipe(BaseModel):
    nome = CharField()
    nom_empresa = ForeignKeyField(Construtora)
    funcionarios = ManyToManyField(Funcionario)

class Obra(BaseModel):
    equipe = ForeignKeyField(Equipe)
    nom_empresa = ForeignKeyField(Construtora)
    valor = CharField()
    materiais = ForeignKeyField(Material)

class Acabamento(BaseModel):
    nome_space = CharField()
    decoracao = CharField()
    nom_empresa = ForeignKeyField(Construtora)


if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)

    db.connect() 
    db.create_tables([Funcionario, Cliente, Fornecedor,  Maquinario, Construtora, Engenheiro, Arquiteto, Material, Equipe, Obra, Acabamento, Construtora.clientes.get_through_model(), Equipe.funcionarios.get_through_model()])

#funcionario ok
    fun1 = Funcionario.create(nome = "Carlos", salario = "4300")

#cliente ok
    c1 = Cliente.create(nome = "Múcio", cpf = "222333444-90")

#fornecedor ok
    f1 = Fornecedor.create(nom_fornecedor = "Gustavo Bosco", tempo_entrega = "6 dias")

#maquinario ok
    maq1 = Maquinario.create(nome_maq = "Trator", fornecedor_maq = f1)

#construtora ok
    cons1 = Construtora.create(nom_empresa = "Paninfaria")
    
#engenheiro ok
    e1 = Engenheiro.create(nome = "Tiago", nom_empresa = cons1)

#arquiteto ok
    a1 = Arquiteto.create(nome = "Bruna", nom_empresa = cons1)

#material ok
    m1 = Material.create(nome_material = "Porcelanato", quantidade = "10 metros quadrados", fornecedor = f1)

#equipe ok
    eq1 = Equipe.create(nome = "TRIPLO X", nom_empresa = cons1)

#obra ok
    o1 = Obra.create(equipe = e1, nom_empresa = cons1, valor = "10500", materiais = m1)

#acabamento ok
    ac1 = Acabamento.create(nome_space = "Área de lazer", decoracao = "Estilo industrial", nom_empresa = cons1)

#ManyToMany
    eq1.funcionarios.add(fun1)
    cons1.clientes.add(c1)

    print("nome: ",fun1.nome,"||    salario: ",fun1.salario)

    print("nome maquinário: ",maq1.nome_maq,"||     fornecedor do maquinário: ",maq1.fornecedor_maq.nom_fornecedor)

    print("nome : ",c1.nome,"||     CPF: ",c1.cpf)

    print("nome do fornecedor: ",f1.nom_fornecedor,"||     Tempo de entrega: ",f1.tempo_entrega)

    print("nome da empresa: ",cons1.nom_empresa, end = ', ')
    for cli1 in cons1.clientes:
        print ("||     cliente : ",cli1.nome,"||     CPF: ",cli1.cpf)

    print("nome: ",e1.nome,"||     Nome da empresa que trabalha: ",e1.nom_empresa.nom_empresa)

    print("nome: ",a1.nome,"||     Nome da empresa que trabalha: ",a1.nom_empresa.nom_empresa)

    print("nome do material: ",m1.nome_material,"||     Quantidade: ",m1.quantidade,"||     Fornecedor: ",m1.fornecedor.nom_fornecedor)

    print("nome: ",eq1.nome, end = ', ')
    for fun in eq1.funcionarios:
        print ("||     nome: ",fun.nome,"||    salario: ",fun.salario)

    print("Obra: ",o1.equipe.nome,"||     Nome da empresa que trabalha: ",o1.nom_empresa.nom_empresa, "||     Valor: ",o1.valor, "||     Materiais: ",o1.materiais.nome_material)

    print("nome do espaço: ",ac1.nome_space,"||     Estilo da decoração: ",ac1.decoracao,"||     Nome da empresa que trabalha: ",ac1.nom_empresa.nom_empresa)