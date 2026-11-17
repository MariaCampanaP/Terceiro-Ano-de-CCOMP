import re
from unidecode import unidecode
from collections import Counter
import random
import spacy
import numpy as np
import nltk
import os
import math
from xmlrpc.server import SimpleXMLRPCServer

# Artigos, preposições, contrações e conjunções
STOPWORDS_ESTRUTURAIS = {
    "a", "o", "as", "os", "um", "uma", "uns", "umas",
    "de", "do", "da", "dos", "das", "dum", "duma",
    "em", "no", "na", "nos", "nas", "num", "numa", "nuns", "numas",
    "por", "pelo", "pela", "pelos", "pelas", "per",
    "para", "pra", "pro", "ao", "aos",
    "com", "sem", "sob", "sobre", "ate", "apos", "ante", "entre",
    "contra", "desde", "perante", "conforme", "durante", "mediante",
    "e", "ou", "mas", "porem", "contudo", "todavia", "entretanto",
    "porque", "porquanto", "pois", "que", "se", "como", "quando",
    "enquanto", "embora", "conquanto", "portanto", "logo", "ora", "nem",
    "quer", "seja", "caso",
}

# Pronomes e determinantes
STOPWORDS_PRONOMES = {
    "eu", "tu", "ele", "ela", "nos", "vos", "eles", "elas",
    "me", "te", "lhe", "lhes", "mim", "ti", "si",
    "comigo", "contigo", "consigo", "conosco", "convosco",
    "voce", "voces", "vossa", "vossemece",
    "meu", "minha", "meus", "minhas",
    "teu", "tua", "teus", "tuas",
    "seu", "sua", "seus", "suas",
    "nosso", "nossa", "nossos", "nossas",
    "vosso", "vossos", "vossas",
    "este", "esta", "estes", "estas", "isto",
    "esse", "essa", "esses", "essas", "isso",
    "aquele", "aquela", "aqueles", "aquelas", "aquilo",
    "quem", "qual", "quais", "cujo", "cuja", "cujos", "cujas",
    "onde", "aonde", "quanto", "quanta", "quantos", "quantas",
    "todo", "toda", "todos", "todas",
    "outro", "outra", "outros", "outras",
    "mesmo", "mesma", "mesmos", "mesmas",
    "algum", "alguma", "alguns", "algumas", "alguem", "algo",
    "nenhum", "nenhuma", "nenhuns", "nenhumas", "ninguem", "nada",
    "tudo", "qualquer", "quaisquer", "cada", "varios", "varias",
    "tal", "tais", "certo", "certa",
}

# Verbos auxiliares e de ligação (lemas e formas conjugadas frequentes)
STOPWORDS_VERBOS = {
    "ser", "sou", "es", "somos", "sao", "era", "eras", "eramos", "eram",
    "fui", "foste", "foi", "fomos", "foram", "sera", "serao", "seria",
    "seriam", "sejam", "fosse", "fossem", "for", "forem", "sido", "sendo",
    "estar", "estou", "estas", "estao", "estamos", "estava", "estavam",
    "esteve", "estiveram", "estivesse", "estivessem", "estado", "estando",
    "ter", "tenho", "tens", "tem", "temos", "tendes", "tinha", "tinhas",
    "tinham", "tive", "teve", "tivemos", "tiveram", "tivesse", "tivessem",
    "tera", "terao", "teria", "teriam", "tido", "tendo",
    "haver", "hei", "ha", "hao", "havia", "haviam", "houve", "houveram",
    "houvesse", "havera", "havendo", "havido",
    "poder", "pode", "podem", "podia", "podiam", "pude", "pudesse",
    "podera", "podendo", "podido",
    "ir", "vou", "vai", "vao", "ia", "iam", "irei", "ira", "irao", "indo",
    "fazer", "faco", "faz", "fazem", "fazia", "faziam", "fez", "fizeram",
    "fara", "farao", "fazendo", "feito",
    "dizer", "digo", "diz", "dizem", "dizia", "diziam", "disse",
    "disseram", "dira", "dizendo", "dito",
    "dever", "deve", "devem", "devia", "deviam",
}

# Advérbios e expressões de baixo valor semântico
STOPWORDS_ADVERBIOS = {
    "nao", "sim", "muito", "muita", "muitos", "muitas",
    "mais", "menos", "ja", "ainda", "tambem", "so", "somente", "apenas",
    "assim", "aqui", "ali", "la", "ca", "acola",
    "entao", "agora", "sempre", "nunca", "jamais", "talvez", "acaso",
    "bem", "mal", "melhor", "pior", "tao", "tanto", "tanta", "tantos",
    "tantas", "quase", "depois", "antes", "logo", "cedo", "tarde",
    "hoje", "ontem", "amanha", "outrora", "enfim", "afinal",
    "dentro", "fora", "acima", "abaixo", "adiante", "atras", "perto",
    "longe", "junto", "alem", "aquem", "atraves", "onde",
    "pouco", "pouca", "poucos", "poucas", "demais", "bastante",
    "porque", "porquanto", "salvo", "exceto", "inclusive",
}


STOPWORDS_LIVRO = {
    "coisa", "coisas", "vez", "vezes", "modo", "maneira", "tipo",
    "parte", "lado", "forma", "caso", "ponto", "meio", "sorte",
    "favor", "respeito", "fim", "inicio", "comeco",
    "senhor", "senhora", "senhores", "senhoras", "sr", "sra", "dom", "dona",
    "capitulo", "capitulos", "pagina", "paginas", "tomo", "volume",
    "livro", "nota", "notas", "indice", "prefacio", "sumario",
    "gutenberg", "project", "ebook", "etc", "coisinha"
}

STOPWORDS = (
    STOPWORDS_ESTRUTURAIS
    | STOPWORDS_PRONOMES
    | STOPWORDS_VERBOS
    | STOPWORDS_ADVERBIOS
    | STOPWORDS_LIVRO
)

TAMANHO_MINIMO = 3

global nlp
nlp = spacy.load("pt_core_news_lg")

caminho_livro = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "livro.txt"
)

with open(caminho_livro, "r", encoding="utf-8") as file:
    texto = file.read()

# Converte string para minúsculas, aplica unidecode para remover acentos e 
# executa a expressão regular re.sub para eliminar pontuações e símbolos
def normalizar_palavra(palavra):
    palavra = palavra.lower()
    palavra = unidecode(palavra)
    palavra = re.sub(r'[^a-z]', '', palavra)

    return palavra


def extrair_substantivos(texto):
    doc = nlp(texto)

    substantivos = []

    for token in doc:

        if (
            token.pos_ == "NOUN" # Mantém substantivos, outras classes gramaticais são descartadas
            and token.is_alpha # Aceita tokens formados por letras
            and not token.is_stop # Descarta stopwords da lista interna do spaCy
            and not token.is_punct
        ):

            palavra = normalizar_palavra(token.lemma_) # Obtém o lema, ou forma base, da palavra

            if palavra not in STOPWORDS:
                substantivos.append(palavra)

    return substantivos

#Constroi o vocabulario
def vocabulario(tokens, freq_min=20): 
    freq = Counter(tokens)

    vocab = []

    for palavra, count in freq.items():
        if count >= freq_min:
            vocab.append(palavra)

    return vocab

#Escolhe a palavra Aleatoria
def palavra_aleatoria(vocab):
    if not vocab:
        return None

    return random.choice(vocab)

# Calcula a similaridade --> A similaridade do cosseno compara o angulo
# entre dois vetores, ajudando a estimar a proximidade semântica
# valores próximos de 1.0 indicam alta proximidade semântica, 
# enquanto valores próximos de 0.0 indicam independência contextual entre os termos no modelo treinado.
def similaridade_cosseno (vetor_a, vetor_b): 
    produto = np.dot(vetor_a, vetor_b) 
    norma_a = np.linalg.norm(vetor_a) 
    norma_b = np.linalg.norm(vetor_b) 
    if norma_a == 0 or norma_b == 0: 
        return 0.0 
    return produto / (norma_a * norma_b) 

#Cria o ranking
def ranking(palavra_secreta, vocab, modelo): 
    vetor_secreto = modelo(palavra_secreta).vector 
    similaridades = {} 
    for palavra in vocab: 
        vetor_palavra = modelo(palavra).vector 
        similaridade = similaridade_cosseno(vetor_secreto, vetor_palavra) 
        similaridades[palavra] = similaridade

    return sorted(similaridades.items(), key=lambda x: x[1], reverse=True) # Retorna as 10 palavras mais similares

#Inicia o jogo
def iniciarJogo():
    global palavra_secreta
    palavra_secreta = palavra_aleatoria(vocab)
    
    global ranking_gerado
    ranking_gerado = ranking(
        palavra_secreta,
        vocab,
        nlp
    )
    
    global palavras_tentadas
    palavras_tentadas = []
    
    global posicao_atual # Registra a melhor posição alcançada
    posicao_atual = len(vocab)
    print("\nPalavra secreta:", palavra_secreta)

#Recebe uma palavra e retorna sua posicao
def calcularPosicao(palavra_enviada):        
    global vocab
    global ranking_gerado
    global posicao_atual
    global palavras_tentadas
    
    if palavra_enviada not in vocab:#verifica se a palavra e valida
        return -1
    elif palavra_enviada in palavras_tentadas:#verifica se a palavra ja foi tentada antes
        return -2
    else: # Posição no ranking 
        for posicao, (palavra, similaridade) in enumerate(ranking_gerado, start=1):
            if palavra_enviada == palavra:
                palavras_tentadas.append(palavra_enviada)
                if posicao < posicao_atual:
                    posicao_atual = posicao
                return posicao

# O servidor tenta selecionar uma palavra mais bem posicionada que o melhor palpite
# sem revelar diretamente a posição 1
def solicitarDica():
    posicaoDica = random.randrange(2, posicao_atual)
    for posicao, (palavra, similaridade) in enumerate(ranking_gerado, start=1):
        if posicaoDica == posicao:
            return palavra
        
def revelarPalavraSecreta():
    return palavra_secreta

substantivos = extrair_substantivos(texto)

global vocab
vocab = vocabulario(substantivos, freq_min=5)

global palavra_secreta

global ranking_gerado


#Guarda a posicao mais alta das tentativas para a solicitacao de dicas
global posicao_atual
posicao_atual = len(vocab)

#Configuracao Servidor
server = SimpleXMLRPCServer(("localhost", 9876), allow_none = True) #local do servidor

print("Servidor Contexto - Alice Iniciado")

#Registrar funcoes
server.register_function(iniciarJogo, "iniciarJogo")

server.register_function(calcularPosicao, "calcularPosicao")

server.register_function(solicitarDica, "solicitarDica")

server.register_function(revelarPalavraSecreta, "revelarPalavraSecreta")

server.serve_forever()