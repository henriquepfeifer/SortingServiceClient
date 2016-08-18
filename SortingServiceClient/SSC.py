#------Início do codigo
from operator import itemgetter, attrgetter

#Importando dados do arquivo de configuração
import json,sys

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
if (len(data)==0):
    sys.exit("Arquivo de configuracao vazio")

#Definição da Classe Livro
class Books:
    def __init__(self, title, author, edition):
        self.title = title
        self.author = author
        self.edition = edition
    def __repr__(self):
        return repr((self.title, self.author, self.edition))


#Atribuindo os títulos aos objetos
#Para facilitar, já foram adicionados os livros para teste
#Em uma versão final do programa, esse bloco deve ser removido
Books_objects = []
Books_objects.append(Books("Java How to Program", "Deitel & Deitel", 2007))
Books_objects.append( Books("Patterns of Enterprise Application Architecture", "Martin Fowler", 2002))
Books_objects.append( Books("Head First Design Patterns", "Elisabeth Freeman", 2004))
Books_objects.append( Books("Internet & World Wide Web: How to Program", "Deitel & Deitel", 2007))


print('Lista de livros adicionados:')
for i in range(len(Books_objects)):
    print(Books_objects[i])


cond=input("\nDeseja adicionar mais algum livro?  : ")

#Adicionar livros
while((cond[0]=='s')or(cond[0]=='S')):  #caso o usuário digite com letra maiúscula ou minúscula
    if ((cond[0]=='s')or(cond[0]=='S')):
        title1=input("Titulo do livro: ")
        author1=input("Autor do livro: ")
        edition1=input("Edicao do livro: ")
        Books_objects.append(Books(title1,author1,edition1))
        print('Livro Adicionado')
        print()
        print('Lista de livros adicionados:')
        for i in range(len(Books_objects)):
            print(Books_objects[i])
        cond=input("\nDeseja adicionar mais algum livro?  : ")





#Implementação da ordenação
#De acordo com o documento "Technical Assessments", a prioridade para ordenar alfabeticamente é dada na seguinte ordem:
#1- Edição
#2- Autor
#3- Título
#Isso significa que se o programa recebe a informação que deve ordenar alfabeticamente por Autor e Edição, primeiramente
#é ordenado por edição, depois por autor.
#Respeitando essa ordem prioritária, a lista deve ser ordenada do item menos prioritário ao mais prioritário, sendo que,
#quando existem dois valores iguais de uma classe mais prioritária, o comando "sort/sorted" não altera a ordem original
#da lista, preservando a ordenação feita anteriormente.


if (len(data['Title']) != 0):   #É necessário fazer essa verificação pois a próxima comparação não poderá ser feita caso
                                #essa condição não seja satisfeita
    if ((data['Title'][0] == 'A')or(data['Title'][0] == 'a')):  #Somente a primeira letra é verificada, portanto, se
                                                                #existirem erros de grafia por parte do usuário, o pro-
                                                                #grama funciona normalmente, desde que o usuário acerte
                                                                #a primeira letra
        Books_objects.sort(key=attrgetter('title'))
    elif((data['Title'][0] == 'D')or(data['Title'][0] == 'd')):
        Books_objects.sort(key=attrgetter('title'), reverse=True)

if (len(data['Author']) != 0):
    if((data['Author'][0] == 'A')or(data['Author'][0] == 'a')):
        Books_objects.sort(key=attrgetter('author'))
    elif((data['Author'][0] == 'D')or(data['Author'][0] == 'd')):
        Books_objects.sort(key=attrgetter('author'), reverse=True)

if (len(data['Edition']) != 0):
    if((data['Edition'][0] == 'A')or(data['Edition'][0] == 'a')):
        Books_objects.sort(key=attrgetter('edition'))
    elif ((data['Edition'][0] == 'D')or(data['Edition'][0] == 'd')):
        Books_objects.sort(key=attrgetter('edition'), reverse=True)

elif((len(data['Title'])+len(data['Edition'])+len(data['Author']))==0):
    #Caso o arquivo de configuração apresente todas as configurações vazias, uma exceção é aberta:
    #1- A lista é ordenada com uma prioridade diferente, Título, Autor e Edição, inversa a anterior.
    #2- Todos os 3 parâmetros são ordenados de forma ascendente
    print('Configuracoes vazias')
    print('Ordenando em ordem alfabetia ascendente')
    print('Ordem prioritária: Titulo, Autor, Edicao')
    Books_objects.sort(key=attrgetter('title','author','edition'))


print('\nOrdem:')
for i in range(len(Books_objects)):
    print(Books_objects[i])






