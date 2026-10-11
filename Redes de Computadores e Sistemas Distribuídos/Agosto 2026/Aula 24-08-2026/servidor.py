from xmlrpc.server import SimpleXMLRPCServer

acervo = {
    1:{
        "título" : "Sistemas Distribuídos",
        "ano" : 2007,
        "edição" : 4,
        "autor" : "Coulouris"
    },
}

def listar_livros():
    lista = []
    for livro in acervo.values():
        lista.append({"título" : livro["título"], "autor" : livro["autor"]})
    return lista

def buscar(str_busca):
    resultados = []
    for livro in acervo.values():
        if str_busca.lower() in livro["autor"].lower():
            resultados.append({"título" : livro["título"], "autor" : livro["autor"]})
    return resultados

server = SimpleXMLRPCServer(("localhost", 9876))
print("Servidor iniciado")

server.register_function(listar_livros, "listar_livros")
server.register_function(buscar, "buscar")

server.serve_forever()