import os
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:9876")

def listar_livros():
    livros = proxy.listar_livros()
    
    for l in livros:
        print("\n")
        print(l)
    input("Digite uma tecla para continuar...")

def buscar():
    str_busca = input("Digite o nome do autor: ")
    resultado = proxy.busca(str_busca)
    print("resultado: ", resultado)

while True:
    print("\n Biblioteca")
    print("[1] Listar Livros")
    print("[2] Buscar Livros por Autor")
    print("[3] Sair")
    
    opcao = input("Opcao: ")
    
    if opcao == "1":
        listar_livros()
    elif opcao == "2":
        buscar()
    else:
        break