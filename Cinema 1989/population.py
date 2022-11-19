filmes = [
    {
        "titulo":"Shrek",
        "diretor":"Ciro",
        "ano_lacamento":1995,
        "avaliacao_imdb":9.5,
    },
    {
        "titulo":"Shrek 2",
        "diretor":"Ciro",
        "ano_lacamento":2000,
        "avaliacao_imdb":9,
    },
    {
        "titulo":"Shrek 3",
        "diretor":"Ciro",
        "ano_lacamento":2005,
        "avaliacao_imdb":7,
    },
    {
        "titulo":"Shrek 4",
        "diretor":"Ciro",
        "ano_lacamento":2010,
        "avaliacao_imdb":5,
    },
    {
        "titulo":"As cores do Amor",
        "diretor":"Ciro",
        "ano_lacamento":2021,
        "avaliacao_imdb":10,
    },
]


sessoes = [
    {
        "localizacao":"C1"
    },

    {
        "localizacao":"C2"
    },

    {
        "localizacao":"C3"
    },
]

def population(database):
    for filme in filmes:
        database.addFilme(filme)

    for sessao in sessoes:
        database.addSessao(sessao.get("localizacao"))