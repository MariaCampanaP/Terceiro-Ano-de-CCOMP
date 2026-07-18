import numpy as np
import math
import copy
import random
from collections import deque
import matplotlib.pyplot as plt
import time

class Cidade:
  def __init__(self):
    self.cidade = 1
    self.x = 0.0
    self.y = 0.0
    
  def __str__(self):#Retorno de string
    return(str(self.cidade) + " " + str(self.x) + " " + str(self.y))
  
  def distancia(self, b):
    return math.sqrt((b.x - self.x)**2 + (b.y - self.y)**2)

class Caminho:
  def __init__(self):
    self.caminho = []
    self.distancia = 0.0
    
  #Calcula a distância total do caminho
  def calculaDistancia(self):
    self.distancia = 0.0 #Reseta a distancia para calculos futuros
    for i in range (len(self.caminho) - 1):
      self.distancia+= self.caminho[i].distancia(self.caminho[i+1])
  
  def imprimirCaminho(self):
    for i in range (len(self.caminho)):
      print(str(self.caminho[i].cidade))
      
  def imprimirDistancia(self):
    print(str(self.distancia))

     
print("Digite as cidades e suas cordenadas:")

cidades = []
n = 0
listaPosicoes = []

while(True):
  try:
      linha = input().strip()
      if not linha:
        break # Sai do loop se a linha estiver vazia
        
      p = Cidade()
      cidade, x, y = linha.split()
      
      cidade = int(cidade)
      x = float(x)
      y = float(y)
        
      p.cidade = cidade
      p.x = x
      p.y = y
      cidades.append(p)
      listaPosicoes.append(n)
      n += 1
  except EOFError:
    break
  
print("Iniciando o algoritmo genético")

tamanho = len(cidades)
populacaoInicial = []
melhorCaminho = Caminho()
melhorCaminho.distancia = math.inf

# Lista para o gráfico
historico_distancias = []

contador_individuos = 0
historico_individuos = []

tempos_execucao = []
inicio_total = time.time()

#Criação da população inicial
for i in range (1000):
  caminhoInicial = Caminho() #Caminho a ser criado
  posicoes = listaPosicoes.copy()
  random.shuffle(posicoes) #Sorteia a ordem das cidades
  
  for j in range(tamanho):
    caminhoInicial.caminho.append(cidades[posicoes[j]]) #Adiciona as cidades ao novo caminho baseado na ordem sorteada
  
  caminhoInicial.caminho.append(caminhoInicial.caminho[0]) #Adiciona a cidade de origem no final to caminho
  caminhoInicial.calculaDistancia() #Calcula a distancia total
  #caminhoInicial.imprimirDistancia()
  populacaoInicial.append(caminhoInicial)
  
  if caminhoInicial.distancia < melhorCaminho.distancia:
    melhorCaminho = caminhoInicial
    
#Criação das populações subsequentes
for geracoes in range (1000):
    novaPopulacao = []
    populacaoElite = []
    
    #Definição da elite
    populacaoElite = populacaoInicial.copy()
    populacaoElite.sort(key = lambda x: x.distancia)
    for i in range (25):
      novaPopulacao.append(copy.copy(populacaoElite[i]))
    
    while len(novaPopulacao) < len(populacaoInicial):#Apenas gera novos individuos enquanto o tamanho da populacao for menor ao tamanho da populacao inicial
      
      p = random.randrange(1, 100, 1) #Sorteio do metodo de selecao
      
      amostra = random.sample(populacaoInicial, 2) #Torneio
      vencedor = Caminho()
      vencedor.distancia = math.inf
      for n in range (2):
        if amostra[n].distancia < vencedor.distancia:
          vencedor = copy.copy(amostra[n])
            
      if p <= 85: #Cruzamento
        amostra = random.sample(populacaoInicial, 2) #Torneio para selecionar o par
        par = Caminho()
        par.distancia = math.inf
        for n in range (2):
          if amostra[n].distancia < par.distancia:
            par = copy.copy(amostra[n])
            
        #definicao dos pontos de corte
        c1 = (tamanho) //4
        if c1 < 1:
          c1 = 1
        c2 = ((tamanho)*3) //4
        if c2 > tamanho-1:
          c2 = tamanho-1
        
        filho = Caminho()
        herdados = Caminho()
        
        for i in range (tamanho): #filho "herda" alguns dos cromossomos do pai
          if i > c1 and i < c2:
            herdados.caminho.append(vencedor.caminho[i])
            
        #Cria sets para agilizar a verificação de elementos
        herdadosSet = set(herdados.caminho)
        filhoSet = set()

        j = 0
        k = 0
        
        for i in range (tamanho):#Preenchimento das lacunas do filho
          if i <= c1 or i >= c2:
            for j in range(tamanho):
              if par.caminho[j] not in herdadosSet and par.caminho[j] not in filhoSet:
                  filho.caminho.append(par.caminho[j])
                  filhoSet.add(par.caminho[j])
                  break
              else:
                j += 1
          else:
            filho.caminho.append(herdados.caminho[k])
            filhoSet.add(herdados.caminho[k])
            k += 1
            
        filho.caminho.append(filho.caminho[0])
        filho.calculaDistancia()
        novaPopulacao.append(filho)
        
        if filho.distancia < melhorCaminho.distancia:#Atualiza o melhor caminho encontrado
          melhorCaminho = filho
            
      elif p > 85 and p <= 95: #Reprodução
        novaPopulacao.append(copy.copy(vencedor)) #Passa o individuo selecionado adiante
        
      elif p > 95: #Mutação
        
        novoIndividuo = copy.copy(vencedor)
        troca = random.sample(listaPosicoes, 2)# Seleciona dois cromossomos e os troca de lugar
      
        aux = novoIndividuo.caminho[troca[0]]
        novoIndividuo.caminho[troca[0]] = novoIndividuo.caminho[troca[1]]
        novoIndividuo.caminho[troca[1]] = aux
        
        if troca[0] == 0 or troca[1] == 0:#Corrige as cidades de origem e destino caso tenham sido alteradas
          novoIndividuo.caminho[tamanho] = novoIndividuo.caminho[0]
        elif troca[0] == tamanho or troca[1] == tamanho:
          novoIndividuo.caminho[0] = novoIndividuo.caminho[tamanho]
          
        novoIndividuo.calculaDistancia() #Calcula a nova distancia do individuo
        novaPopulacao.append(novoIndividuo)
        
        if novoIndividuo.distancia < melhorCaminho.distancia:
          melhorCaminho = novoIndividuo
          
        
    populacaoInicial = novaPopulacao.copy()
    melhorCaminho.imprimirDistancia()
    
    #Registro do tempo
    tempo_atual = time.time() - inicio_total
    tempos_execucao.append(tempo_atual)
    
    #Registro do número de indivíduos gerados
    contador_individuos += len(populacaoInicial)
    historico_individuos.append(contador_individuos)
    
    # Salva a distância para o gráfico
    historico_distancias.append(melhorCaminho.distancia)
  
  
print("\nMelhor caminho encontrado:")
melhorCaminho.imprimirCaminho()

print("\nDistância final:")
melhorCaminho.imprimirDistancia()

# Gráficos

# Cria um gráfico de linha com os valores de distância ao longo das gerações
plt.plot(historico_distancias)
plt.xlabel("Gerações") # Eixo x (número de gerações)
plt.ylabel("Distância") # Eixo Y (distância do caminho)
plt.title("Evolução da distância ao longo das gerações")
plt.grid(True)
plt.show()

plt.figure()

# Crie um gráfico de linha relacionando número de cidades com tempo de execução
plt.plot(historico_individuos, tempos_execucao)
plt.xlabel("Número de cidades") # Eixo X
plt.ylabel("Tempo de Execução (s)") # Eixo Y
plt.title("Tempo de execução vs Número de cidades")
plt.grid(True)
plt.show()