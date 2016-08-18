
Para configurar o modo de ordenação do programa, alterar arquivo config.json.
As configurações podem ser:
1- "Ascending": ordena os livros em ordem alfabética ascendente
2- "Descending": ordena os livros em ordem alfabética descendente
3- Vazio: Desconsidera o atributo na ordenação

Para executar, deve ser aberto o arquivo SSC.py

Existem três atributos que podem ser selecionados como modo de classificação
-Título (Title)
-Autor	(Author)
-Edição	(Edition)

Caso mais de um seja selecionado simultaneamente, a ordem prioritária é a seguinte:
1- Edição
2- Autor
3- Título

Sendo que, se se edição e título forem selecionados, a lista de livros será classificada por edição, e caso existam duas edições iguais, o critério para ordenação considerado será o título

No programa já estão registrados os quatro livros utilizados para teste, no entanto, o usuário pode adicionar mais livros livremente.

