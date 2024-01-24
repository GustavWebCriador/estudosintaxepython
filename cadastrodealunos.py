#class é criada para repsentar um aluno, ela possui um construtor 'init' que inicializa os três atributos. 
class Aluno: 
    def __init__(self, nome, idade, notas): 
        self.nome = nome
        self.idade = idade
        self.notas = notas 
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
#lista para armazenar os alunos cadastrados
lista_alunos = []

#função para cadastrar um novo aluno 
def cadastrar_aluno(): 
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

#Solicitar as notas e armazená-las em uma lista
    notas = []
    qtd_notas = int(input("Quantas notas deseja inserir? "))
    for i in range (qtd_notas):
        nota = float(input(f"Digite a nota { i + 1}: "))
        notas.append(nota)

#Criar uma instância da classe Aluno 
        aluno=Aluno(nome, idade, notas)

#Adicionar o aluno à lista de alunos 
        lista_alunos.append(aluno)
        print(f"\nAluno {nome} cadastro com sucesso!\n")
#Função para exebi informações de todos os alunos
def exibir_alunos():
    print("\nLista de Alunos: ")
    for aluno in lista_alunos:
        print(f"\nNome: {aluno.nome}")
        print(f"Idade: {aluno.idade}")
        print(f"Notas: {aluno.notas}")
        print(f"Média: {aluno.calcular_media()}")

#Menu principal
while True:
    print("1. Cadastrar Aluno")
    print("2. Exibir Alunos")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao =="1":
        cadastrar_aluno()
    elif opcao == "2":
        exibir_alunos()
    elif opcao == "3":
        print ("Saindo do programa. Até mais!")
        break
    else: 
        print("Opção inválida. Tente novamente. \n")