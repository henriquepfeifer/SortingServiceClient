
Para configurar o modo de ordenacao do programa, alterar arquivo config.json.
As configuracoes podem ser:
1- "Ascending": ordena os livros em ordem alfabetica ascendente
2- "Descending": ordena os livros em ordem alfabetica descendente
3- Vazio: Desconsidera o atributo na ordenacao

Para executar, deve ser aberto o arquivo SSC.py

Existem tres atributos que podem ser selecionados como modo de classificacao
-Titulo (Title)
-Autor	(Author)
-Edicao	(Edition)

Caso mais de um seja selecionado simultaneamente, a ordem prioritária e a seguinte:
1- Edicao
2- Autor
3- Titulo

Por exemplo, se se edicao e titulo forem selecionados, a lista de livros sera classificada por edicao, e caso existam duas edicoes iguais, o criterio para ordenacao considerado sera o titulo

No programa ja estao registrados os quatro livros utilizados para teste, no entanto, o usuario pode adicionar mais livros livremente.

