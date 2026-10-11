import math 
import os  
import customtkinter as ctk  

# Configuração de tema e cores
# Define o tema visual e as cores utilizadas em toda a interface
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_tema = os.path.join(diretorio_atual, "tema_contexto.json")

# Define a aparência da aplicação como modo claro
ctk.set_appearance_mode("light")

if os.path.exists(caminho_tema):
    ctk.set_default_color_theme(caminho_tema)
else:
    ctk.set_default_color_theme("blue")

# Cores principais da interface, seguindo a identidade visual inspirada em Alice no País das Maravilhas
FUNDO = "#F7F0DF"
PAINEL = "#FFFDF5"

AZUL_ALICE = "#A9D6E5"
AZUL_HOVER = "#8EC6D8"
AZUL_ESCURO = "#426A78"

VERMELHO = "#B94A48"
VERMELHO_HOVER = "#A83D3B"

ROSA = "#E9B5BE"
ROSA_HOVER = "#DFA0AB"

DOURADO = "#D8B765"
DOURADO_CLARO = "#E8D39A"

MARROM = "#493B35"
MARROM_CLARO = "#75645B"
BRANCO = "#FFFFFF"

# Janela principal e Container
# Cria a janela principal e o container onde as diferentes telas serão exibidas
root = ctk.CTk()  # Cria a janela principal da aplicação
root.title("Contexto - Alice no País das Maravilhas")
root.geometry("430x620")  # Resolução maior para evidenciar a centralização
root.configure(fg_color=FUNDO)  # Cor de fundo padrão da janela exterior

container = ctk.CTkFrame(root, fg_color="transparent")  # Área onde as telas serão carregadas
container.pack(fill="both", expand=True)

frame_atual = None  # Guarda referência para a tela que está sendo exibida.

# Funções de navegação e helpers
# Funções auxiliares usadas para trocar telas, sair do programa e criar botões padronizados
# Troca a tela atual pela tela indicada pela função recebida
def mostrar_tela(funcao_tela):
    # Muda a tela exibida centralizando o novo cartão no container
    global frame_atual
    if frame_atual is not None:
        frame_atual.destroy()

    frame_atual = funcao_tela(container)
    frame_atual.pack(expand=True)

# Encerra a aplicação
def sair():
    # Fecha o programa
    root.destroy()

# Cria um botão seguindo o padrão visual definido para o projeto
def criar_botao(pai, texto, comando, cor, hover):
    # Padroniza a criação de botões com as cores e bordas do tema
    botao = ctk.CTkButton(
        pai,
        text=texto,
        command=comando,
        width=210,
        height=40,
        corner_radius=14,
        fg_color=cor,
        hover_color=hover,
        text_color=MARROM,
        font=("Alice", 14, "bold"),
        border_width=1,
        border_color=DOURADO_CLARO,
    )
    botao.pack(pady=4)
    return botao


# 1. TELA: Menu Principal
# Monta a tela inicial com título, decoração e opções de navegação
# Cria e configura a tela principal do sistema
def tela_menu(pai):
    frame_externo = ctk.CTkFrame(
        pai, fg_color=FUNDO, corner_radius=24, width=340, height=540
    )
    frame_externo.pack_propagate(False)

    frame_menu = ctk.CTkFrame(
        frame_externo,
        fg_color=PAINEL,
        corner_radius=20,
        border_width=2,
        border_color=DOURADO_CLARO,
    )
    frame_menu.pack(fill="both", expand=True, padx=4, pady=4)

    canvas_topo = ctk.CTkCanvas(
        frame_menu, width=300, height=115, bg=PAINEL, highlightthickness=0
    )
    canvas_topo.pack(pady=(15, 0))

    canvas_topo.create_text(
        45, 35, text="♥", font=("Times New Roman", 22), fill=VERMELHO
    )
    canvas_topo.create_text(
        255, 35, text="♠", font=("Times New Roman", 22), fill=AZUL_ESCURO
    )
    canvas_topo.create_text(
        75, 78, text="♦", font=("Times New Roman", 22), fill=VERMELHO
    )
    canvas_topo.create_text(
        255, 78, text="♣", font=("Times New Roman", 22), fill=AZUL_ESCURO
    )

    # Desenha o relógio do Coelho Branco usando elementos do Canvas
    cx, cy, r = 150, 52, 38
    canvas_topo.create_oval(
        cx - r + 2, cy - r + 3, cx + r + 2, cy + r + 3, fill="#D9CDB7", outline=""
    )
    canvas_topo.create_oval(
        cx - r, cy - r, cx + r, cy + r, fill=BRANCO, outline=DOURADO, width=3
    )
    canvas_topo.create_oval(
        cx - 31, cy - 31, cx + 31, cy + 31, outline=DOURADO, width=1
    )

    for i in range(12):
        ang = math.radians(i * 30 - 90)
        x1, y1 = cx + math.cos(ang) * 27, cy + math.sin(ang) * 27
        x2, y2 = cx + math.cos(ang) * 32, cy + math.sin(ang) * 32
        canvas_topo.create_line(x1, y1, x2, y2, fill=MARROM, width=2)

    canvas_topo.create_line(cx, cy, cx, cy - 25, fill=AZUL_ESCURO, width=3)
    canvas_topo.create_line(cx, cy, cx + 17, cy + 12, fill=VERMELHO, width=4)
    canvas_topo.create_oval(cx - 4, cy - 4, cx + 4, cy + 4, fill=VERMELHO, outline="")

    # Exibe o título e o subtítulo da aplicação
    label_titulo = ctk.CTkLabel(
        frame_menu,
        text="CONTEXTO",
        font=("Alice", 28, "bold"),
        text_color=MARROM,
    )
    label_titulo.pack(pady=(0, 2))

    label_subtitulo = ctk.CTkLabel(
        frame_menu,
        text="Encontre a palavra secreta",
        font=("Alice", 13, "italic", "bold"),
        text_color=AZUL_ESCURO,
    )
    label_subtitulo.pack(pady=(0, 12))

    # Cria uma linha decorativa com um naipe de cartas no centro
    canvas_linha = ctk.CTkCanvas(
        frame_menu, width=240, height=25, bg=PAINEL, highlightthickness=0
    )
    canvas_linha.pack()
    canvas_linha.create_line(20, 12, 220, 12, fill=DOURADO, width=1)
    canvas_linha.create_text(
        120, 12, text="♥", font=("Times New Roman", 16), fill=VERMELHO
    )

    # Cria os botões que levam para as demais telas
    criar_botao(
        frame_menu,
        "♥ ENTRAR ♥",
        lambda: mostrar_tela(tela_jogo),
        AZUL_ALICE,
        AZUL_HOVER,
    )
    criar_botao(
        frame_menu,
        "♣ AJUDA ♣",
        lambda: mostrar_tela(tela_ajuda),
        "#DCEEF2",
        "#C6E3EA",
    )
    criar_botao(
        frame_menu,
        "♠ SOBRE ♠",
        lambda: mostrar_tela(tela_sobre),
        "#F3E5B5",
        "#EAD79A",
    )

    botao_sair = ctk.CTkButton(
        frame_menu,
        text="♦ SAIR ♦",
        command=sair,
        width=210,
        height=40,
        corner_radius=14,
        fg_color=ROSA,
        hover_color=ROSA_HOVER,
        text_color=MARROM,
        font=("Alice", 14, "bold"),
        border_width=1,
        border_color="#D89BA5",
    )
    botao_sair.pack(pady=(6, 12))

    label_frase = ctk.CTkLabel(
        frame_menu,
        text='"Eu não sou louco, minha realidade\né apenas diferente da sua."',
        font=("Alice", 13, "italic", "bold"),
        text_color=MARROM_CLARO,
    )
    label_frase.pack(pady=(5, 15))

    return frame_externo


# 2. TELA: Ajuda
# Exibe as instruções básicas de funcionamento do jogo
# Cria a tela com as instruções de como jogar
def tela_ajuda(pai):
    frame_externo = ctk.CTkFrame(
        pai, fg_color=FUNDO, corner_radius=24, width=340, height=540
    )
    frame_externo.pack_propagate(False)

    frame_conteudo = ctk.CTkFrame(
        frame_externo,
        fg_color=PAINEL,
        corner_radius=20,
        border_width=2,
        border_color=DOURADO_CLARO,
    )
    frame_conteudo.pack(fill="both", expand=True, padx=4, pady=4)

    # Desenha uma pequena representação do Absolem e do cogumelo usando Canvas
    canvas_absolem = ctk.CTkCanvas(
        frame_conteudo, width=180, height=85, bg=PAINEL, highlightthickness=0
    )
    canvas_absolem.pack(pady=(12, 0))

    cx, cy = 90, 52

    # Desenha a fumaça em formato de espiral
    canvas_absolem.create_arc(
        cx - 25, cy - 48, cx - 5, cy - 28, start=90, extent=180, style="arc", outline=AZUL_ALICE, width=2
    )
    canvas_absolem.create_arc(
        cx - 15, cy - 52, cx + 5, cy - 32, start=270, extent=180, style="arc", outline=AZUL_ALICE, width=2
    )

    # Desenha o talo do cogumelo
    canvas_absolem.create_polygon(
        cx - 12, cy + 28, cx + 12, cy + 28, cx + 9, cy + 5, cx - 9, cy + 5, fill="#E8DFD1", outline=MARROM, width=1.5
    )

    # Desenha o chapéu do cogumelo
    canvas_absolem.create_arc(
        cx - 38, cy - 12, cx + 38, cy + 22, start=0, extent=180, fill=VERMELHO, outline=MARROM, width=1.5
    )
    canvas_absolem.create_oval(cx - 24, cy - 2, cx - 14, cy + 5, fill=BRANCO, outline="")
    canvas_absolem.create_oval(cx + 12, cy - 5, cx + 22, cy + 3, fill=BRANCO, outline="")

    # Desenha os segmentos do corpo da lagarta
    canvas_absolem.create_oval(cx - 18, cy - 16, cx - 6, cy - 4, fill=AZUL_ESCURO, outline=MARROM, width=1)
    canvas_absolem.create_oval(cx - 10, cy - 22, cx + 2, cy - 10, fill=AZUL_ESCURO, outline=MARROM, width=1)
    canvas_absolem.create_oval(cx - 2, cy - 28, cx + 10, cy - 16, fill=AZUL_ESCURO, outline=MARROM, width=1)

    # Desenha a cabeça e os detalhes do personagem
    canvas_absolem.create_oval(cx + 4, cy - 35, cx + 18, cy - 21, fill="#4EA8DE", outline=MARROM, width=1)
    canvas_absolem.create_line(cx + 8, cy - 28, cx + 14, cy - 28, fill=MARROM, width=1.5)
    canvas_absolem.create_line(cx + 12, cy - 34, cx + 10, cy - 40, fill=MARROM, width=1)
    canvas_absolem.create_line(cx + 15, cy - 34, cx + 17, cy - 40, fill=MARROM, width=1)
    canvas_absolem.create_line(cx + 10, cy - 24, cx - 12, cy - 18, fill=DOURADO, width=2)

    # Adiciona símbolos de cartas nas laterais da ilustração
    canvas_absolem.create_text(18, cy, text="♣", font=("Times New Roman", 15), fill=AZUL_ESCURO)
    canvas_absolem.create_text(162, cy, text="♥", font=("Times New Roman", 15), fill=VERMELHO)
    
    # Exibe o título da tela de ajuda
    label_titulo = ctk.CTkLabel(
        frame_conteudo,
        text="COMO JOGAR",
        font=("Alice", 22, "bold"),
        text_color=MARROM,
    )
    label_titulo.pack(pady=(2, 2))

    # Cria uma linha decorativa com um naipe de cartas no centro
    canvas_linha = ctk.CTkCanvas(
        frame_conteudo, width=220, height=16, bg=PAINEL, highlightthickness=0
    )
    canvas_linha.pack()
    canvas_linha.create_line(15, 8, 205, 8, fill=DOURADO, width=1)
    canvas_linha.create_text(110, 8, text="♦", font=("Times New Roman", 12), fill=VERMELHO)

    # Texto com as instruções básicas do jogo
    texto_instrucoes = (
        "\nDescubra a palavra secreta. Você pode tentar\nquantas vezes precisar.\n\n\n"
        "Depois de enviar uma palavra, você verá a posição\nem que ela está. A palavra secreta é a número 1\n\n\n"
        "Quanto menor o número, mais perto você\nestá da resposta!\n"
    )

    label_info = ctk.CTkLabel(
        frame_conteudo,
        text=texto_instrucoes,
        font=("Alice", 13),
        text_color=MARROM_CLARO,
        justify="left",
    )
    label_info.pack(pady=10, padx=15)

    criar_botao(
        frame_conteudo,
        "↩ VOLTAR",
        lambda: mostrar_tela(tela_menu),
        AZUL_ALICE,
        AZUL_HOVER,
    )

    return frame_externo


# 3. TELA: Sobre
# Exibe informações sobre o projeto e seus desenvolvedores
# Cria a tela com as informações do projeto e dos desenvolvedores
def tela_sobre(pai):
    frame_externo = ctk.CTkFrame(
        pai, fg_color=FUNDO, corner_radius=24, width=340, height=540
    )
    frame_externo.pack_propagate(False)

    frame_conteudo = ctk.CTkFrame(
        frame_externo,
        fg_color=PAINEL,
        corner_radius=20,
        border_width=2,
        border_color=DOURADO_CLARO,
    )
    frame_conteudo.pack(fill="both", expand=True, padx=4, pady=4)

    # Desenha três cartas decorativas inspiradas no baralho de Alice no País das Maravilhas
    canvas_cartas = ctk.CTkCanvas(
        frame_conteudo, width=180, height=85, bg=PAINEL, highlightthickness=0
    )
    canvas_cartas.pack(pady=(15, 0))

    cx, cy = 90, 45

    # Desenha a carta de Copas inclinada
    canvas_cartas.create_polygon(
        cx - 55, cy - 20, cx - 20, cy - 26, cx - 12, cy + 24, cx - 47, cy + 30, fill=BRANCO, outline=MARROM, width=1.5
    )
    canvas_cartas.create_polygon(
        cx - 52, cy - 17, cx - 23, cy - 22, cx - 16, cy + 21, cx - 44, cy + 26, fill="", outline=DOURADO_CLARO, width=1
    )
    canvas_cartas.create_text(cx - 33, cy + 2, text="♥", font=("Times New Roman", 18, "bold"), fill=VERMELHO)

    # Desenha a carta de Ouros inclinada
    canvas_cartas.create_polygon(
        cx + 20, cy - 26, cx + 55, cy - 20, cx + 47, cy + 30, cx + 12, cy + 24, fill=BRANCO, outline=MARROM, width=1.5
    )
    canvas_cartas.create_polygon(
        cx + 23, cy - 22, cx + 52, cy - 17, cx + 44, cy + 26, cx + 16, cy + 21, fill="", outline=DOURADO_CLARO, width=1
    )
    canvas_cartas.create_text(cx + 33, cy + 2, text="♦", font=("Times New Roman", 18, "bold"), fill=VERMELHO)

    # Desenha a carta central de Espadas
    canvas_cartas.create_polygon(
        cx - 16, cy - 30, cx + 24, cy - 26, cx + 20, cy + 26, cx - 20, cy + 22, fill="#D9CDB7", outline=""
    )
    canvas_cartas.create_polygon(
        cx - 18, cy - 32, cx + 22, cy - 28, cx + 18, cy + 24, cx - 22, cy + 20, fill=BRANCO, outline=MARROM, width=1.5
    )
    canvas_cartas.create_polygon(
        cx - 14, cy - 28, cx + 18, cy - 24, cx + 14, cy + 20, cx - 18, cy + 16, fill="", outline=DOURADO, width=1
    )
    canvas_cartas.create_text(cx, cy - 4, text="♠", font=("Times New Roman", 22, "bold"), fill=AZUL_ESCURO)

    canvas_cartas.create_text(18, cy, text="♣", font=("Times New Roman", 15), fill=AZUL_ESCURO)
    canvas_cartas.create_text(162, cy, text="♥", font=("Times New Roman", 15), fill=VERMELHO)
    
    # Exibe o título da tela
    label_titulo = ctk.CTkLabel(
        frame_conteudo,
        text="SOBRE",
        font=("Alice", 22, "bold"),
        text_color=MARROM,
    )
    label_titulo.pack(pady=(4, 2))

    # Cria uma linha decorativa com um naipe de cartas no centro
    canvas_linha = ctk.CTkCanvas(
        frame_conteudo, width=220, height=16, bg=PAINEL, highlightthickness=0
    )
    canvas_linha.pack()
    canvas_linha.create_line(15, 8, 205, 8, fill=DOURADO, width=1)
    canvas_linha.create_text(110, 8, text="♥", font=("Times New Roman", 12), fill=VERMELHO)

    # Exibe os nomes das alunas 
    label_devs = ctk.CTkLabel(
        frame_conteudo,
        text="\nDesenvolvido por:\nLuna Osti de França\nMaria Rita Campana Peixoto\nVallentina Rodrigues Costa Groetaers Sousa",
        font=("Alice", 12, "bold"),
        text_color=AZUL_ESCURO,
    )
    label_devs.pack(pady=(0, 8))

    # Exibe as informações sobre as disciplinas e a universidade
    label_info = ctk.CTkLabel(
        frame_conteudo,
        text=(
            "Trabalho Desenvolvido para as Disciplinas de:\n"
            "Inteligência Artificial\n"
            "Redes e Sistemas Distribuídos\n\n"
            "Curso de Bacharelado em Ciência da Computação\n"
            "UNESPAR - Universidade Estadual do Paraná"
        ),
        font=("Alice", 13),
        text_color=MARROM_CLARO,
        justify="center",
    )
    label_info.pack(pady=(12, 20), padx=15)

    # Botão utilizado para retornar ao menu principal
    criar_botao(
        frame_conteudo,
        "↩ VOLTAR",
        lambda: mostrar_tela(tela_menu),
        AZUL_ALICE,
        AZUL_HOVER,
    )

    return frame_externo

# 4. TELA: Jogo
# Monta a interface principal do jogo
# Cria a tela onde o usuário interage com a parte inicial do jogo
def tela_jogo(pai):

    frame_externo = ctk.CTkFrame(
        pai,
        fg_color=FUNDO,
        corner_radius=24,
        width=340,
        height=540
    )
    frame_externo.pack_propagate(False)

    frame_conteudo = ctk.CTkFrame(
        frame_externo,
        fg_color=PAINEL,
        corner_radius=20,
        border_width=2,
        border_color=DOURADO_CLARO
    )
    frame_conteudo.pack(fill="both", expand=True, padx=4, pady=4)

# Decoração do Topo
# Cria os elementos decorativos exibidos na parte superior da tela do jogo
    canvas_topo = ctk.CTkCanvas(
        frame_conteudo,
        width=320,
        height=18,
        bg=PAINEL,
        highlightthickness=0
    )
    canvas_topo.pack(fill="x", padx=10, pady=(6, 0))

    canvas_topo.create_line(
        15, 9, 130, 9,
        fill=DOURADO_CLARO,
        width=1
    )

    canvas_topo.create_line(
        190, 9, 305, 9,
        fill=DOURADO_CLARO,
        width=1
    )

    canvas_topo.create_text(
        160, 9,
        text="♥",
        font=("Times New Roman", 12),
        fill=VERMELHO
    )

# Título + Menu de Três Pontos
# Exibe o título do jogo e prepara o menu de opções
    frame_topo = ctk.CTkFrame(
        frame_conteudo,
        fg_color="transparent",
        border_width=0
    )
    frame_topo.pack(
        fill="x",
        padx=15,
        pady=(2, 4)
    )

    label_titulo = ctk.CTkLabel(
        frame_topo,
        text="CONTEXTO",
        font=("Alice", 18, "bold"),
        text_color=MARROM
    )
    label_titulo.pack(side="left")

    # Lista usada para guardar a referência do menu aberto, assim é possível fechar o menu quando o usuário clicar novamente
    frame_menu_opcoes = [None]

    # Lista usada para manter o número de tentativas dentro das funções internas
    contador_tentativas = [0]

    # Controla se a partida já foi encerrada
    jogo_finalizado = [False]

    # Palavra secreta exibida na tela de resultado da desistência
    palavra_secreta = "A revelação da palavra secreta\nserá implementada posteriormente."

# Função para adicionar tentativa na tabela
# Adiciona uma palavra digitada pelo usuário e sua posição simulada ao histórico

    # Registra visualmente uma nova tentativa na tabela
    def adicionar_tentativa_tabela(palavra, posicao):

        contador_tentativas[0] += 1

        label_tentativas.configure(
            text=f"TENTATIVAS: {contador_tentativas[0]}"
        )

        item_frame = ctk.CTkFrame(
            frame_tabela,
            fg_color="#F9F6EE",
            corner_radius=8,
            border_width=1,
            border_color=DOURADO_CLARO
        )
        item_frame.pack(
            fill="x",
            padx=4,
            pady=3
        )

        lbl_palavra = ctk.CTkLabel(
            item_frame,
            text=palavra,
            font=("Alice", 13, "bold"),
            text_color=MARROM
        )
        lbl_palavra.pack(
            side="left",
            padx=10,
            pady=4
        )

        lbl_posicao = ctk.CTkLabel(
            item_frame,
            text=str(posicao),
            font=("Alice", 12, "bold"),
            text_color=MARROM_CLARO
        )
        lbl_posicao.pack(
            side="right",
            padx=10,
            pady=4
        )

# Envio da palavra
# Obtém a palavra digitada e registra a tentativa na tabela
    def processar_envio(event=None):

        # A partida terminou: não permite novas tentativas.
        if jogo_finalizado[0]:
            return

        palavra = entry_palavra.get().strip().lower()

        if palavra:
            # Valor temporário usado apenas para demonstrar o funcionamento da interface
            posicao_simulada = 142

            adicionar_tentativa_tabela(
                palavra,
                posicao_simulada
            )

            entry_palavra.delete(
                0,
                "end"
            )

# DICA
# Abre um pop-up informando que a funcionalidade dicas ainda não está implementada
    def pedir_dica():
        popup_dica = ctk.CTkFrame(
            frame_conteudo,
            fg_color=PAINEL,
            corner_radius=16,
            border_width=2,
            border_color=DOURADO_CLARO,
            width=270,
            height=150
        )

        popup_dica.pack_propagate(False)

        popup_dica.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        label_titulo_dica = ctk.CTkLabel(
            popup_dica,
            text="Dica",
            font=("Alice", 16, "bold"),
            text_color=MARROM
        )
        label_titulo_dica.pack(
            pady=(15, 5)
        )

        label_dica = ctk.CTkLabel(
            popup_dica,
            text="A funcionalidade de dicas\nserá implementada posteriormente.",
            font=("Alice", 12),
            text_color=MARROM_CLARO,
            justify="center"
        )
        label_dica.pack(
            padx=15,
            pady=5
        )

        btn_fechar = ctk.CTkButton(
            popup_dica,
            text="Entendi",
            font=("Alice", 12, "bold"),
            fg_color=AZUL_ALICE,
            hover_color=AZUL_HOVER,
            text_color=MARROM,
            width=90,
            height=30,
            corner_radius=10,
            command=popup_dica.destroy
        )
        btn_fechar.pack(
            pady=(5, 10)
        )

# Desistência
# Abre a confirmação de desistência e permite cancelar ou confirmar a ação
    def confirmar_desistencia():

        popup_confirmacao = ctk.CTkFrame(
            frame_conteudo,
            fg_color=PAINEL,
            corner_radius=18,
            border_width=2,
            border_color=DOURADO_CLARO,
            width=290,
            height=165
        )

        popup_confirmacao.pack_propagate(False)

        popup_confirmacao.place(
            relx=0.5,
            rely=0.45,
            anchor="center"
        )

        # Botão X usado para fechar o pop-up de confirmação.
        btn_x = ctk.CTkButton(
            popup_confirmacao,
            text="✕",
            width=26,
            height=26,
            corner_radius=13,
            fg_color="#F2ECE1",
            hover_color=DOURADO_CLARO,
            text_color=MARROM,
            font=("Arial", 11, "bold"),
            command=popup_confirmacao.destroy
        )

        btn_x.place(
            relx=0.93,
            rely=0.07,
            anchor="ne"
        )

        label_pergunta = ctk.CTkLabel(
            popup_confirmacao,
            text="Tem certeza de que quer desistir?",
            font=("Alice", 13, "bold"),
            text_color=MARROM,
            wraplength=200,
            justify="center"
        )

        label_pergunta.pack(
            padx=15,
            pady=(35, 10)
        )

        frame_botoes = ctk.CTkFrame(
            popup_confirmacao,
            fg_color="transparent",
            border_width=0
        )

        frame_botoes.pack(
            pady=(0, 10)
        )

# Botão Sim
# Confirma a desistência do usuário
        def desistir():

            # Encerra a partida atual.
            # A tela do jogo será substituída pela tela de resultado,
            # impedindo novas tentativas.
            jogo_finalizado[0] = True
            popup_confirmacao.destroy()

            mostrar_tela(
                lambda pai: tela_resultado_desistencia(
                    pai,
                    contador_tentativas[0],
                    palavra_secreta
                )
            )

        btn_sim = ctk.CTkButton(
            frame_botoes,
            text="Sim",
            font=("Alice", 12, "bold"),
            fg_color=AZUL_ALICE,
            hover_color=AZUL_HOVER,
            text_color=MARROM,
            border_width=1,
            border_color=DOURADO_CLARO,
            width=80,
            height=32,
            corner_radius=10,
            command=desistir
        )

        btn_sim.pack(
            side="left",
            padx=8
        )


# Botão Não       
# Cancela a desistência e fecha o pop-up de confirmação
        btn_nao = ctk.CTkButton(
            frame_botoes,
            text="Não",
            font=("Alice", 12, "bold"),
            fg_color=VERMELHO,
            hover_color=VERMELHO_HOVER,
            text_color=BRANCO,
            width=80,
            height=32,
            corner_radius=10,
            command=popup_confirmacao.destroy
        )

        btn_nao.pack(
            side="left",
            padx=8
        )

# Pop-Up "Como jogar"
# Exibe as regras básicas do jogo em uma janela sobreposta
    def abrir_popup_como_jogar():

        popup = ctk.CTkFrame(
            frame_conteudo,
            fg_color=BRANCO,
            corner_radius=16,
            border_width=2,
            border_color=DOURADO_CLARO,
            width=270,
            height=300
        )

        popup.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        label_titulo_pop = ctk.CTkLabel(
            popup,
            text="Como Jogar",
            font=("Alice", 16, "bold"),
            text_color=MARROM
        )

        label_titulo_pop.pack(
            pady=(14, 6)
        )

        texto_regras = (
            "Tente adivinhar a palavra secreta.\n\n"
            "Cada tentativa mostrará a proximidade "
            "da sua palavra com a correta.\n\n"
            "Quanto menor o número da posição,\n"
            "mais perto você está!"
        )

        label_texto = ctk.CTkLabel(
            popup,
            text=texto_regras,
            font=("Alice", 12),
            text_color=MARROM,
            justify="left",
            wraplength=220
        )

        label_texto.pack(
            padx=15,
            pady=8,
            fill="both",
            expand=True
        )

        btn_fechar = ctk.CTkButton(
            popup,
            text="Entendi!",
            font=("Alice", 12, "bold"),
            fg_color=AZUL_ALICE,
            hover_color=AZUL_HOVER,
            text_color=MARROM,
            height=32,
            corner_radius=10,
            command=popup.destroy
        )

        btn_fechar.pack(
            pady=(0, 14)
        )
        
# Menu dos três pontos
# Cria e controla as opções exibidas ao clicar nos três pontos
    def alternar_menu():

        if frame_menu_opcoes[0] is not None:

            frame_menu_opcoes[0].destroy()
            frame_menu_opcoes[0] = None

        else:

            menu = ctk.CTkFrame(
                frame_conteudo,
                fg_color=BRANCO,
                corner_radius=16,
                border_width=1,
                border_color=DOURADO_CLARO,
                width=160
            )

            menu.place(
                relx=0.95,
                rely=0.08,
                anchor="ne"
            )

            frame_menu_opcoes[0] = menu

            def acao_menu(comando):

                menu.destroy()
                frame_menu_opcoes[0] = None
                comando()

            opcoes = [
                ("?  Como jogar", abrir_popup_como_jogar),
                ("💡  Dica", pedir_dica),
                ("⚑  Desistir", confirmar_desistencia),
                ("↩  Voltar Menu", lambda: mostrar_tela(tela_menu))
            ]

            for texto, comando in opcoes:

                btn = ctk.CTkButton(
                    menu,
                    text=texto,
                    anchor="w",
                    fg_color="transparent",
                    hover_color=FUNDO,
                    text_color=MARROM,
                    font=("Alice", 12, "bold"),
                    height=32,
                    command=lambda c=comando: acao_menu(c)
                )

                btn.pack(
                    fill="x",
                    padx=6,
                    pady=2
                )

# Botão dos Três Pontos
# Botão que abre ou fecha o menu de opções
    btn_tres_pontos = ctk.CTkButton(
        frame_topo,
        text="⋮",
        width=32,
        height=32,
        corner_radius=16,
        fg_color="#F2ECE1",
        hover_color=DOURADO_CLARO,
        text_color=MARROM,
        font=("Arial", 18, "bold"),
        command=alternar_menu
    )

    btn_tres_pontos.pack(
        side="right"
    )

# Contador de Tentativas
# Exibe na interface a quantidade de tentativas realizadas
    frame_info = ctk.CTkFrame(
        frame_conteudo,
        fg_color="transparent",
        border_width=0
    )

    frame_info.pack(
        fill="x",
        padx=16,
        pady=(4, 2)
    )

    label_tentativas = ctk.CTkLabel(
        frame_info,
        text="TENTATIVAS: 0",
        font=("Alice", 11, "bold"),
        text_color=MARROM_CLARO
    )

    label_tentativas.pack(
        side="left"
    )
    
# Campo para digitar palavra
# Campo onde o usuário pode escrever uma palavra para enviar como tentativa
    frame_input = ctk.CTkFrame(
        frame_conteudo,
        fg_color="transparent",
        border_width=0
    )

    frame_input.pack(
        fill="x",
        padx=15,
        pady=(4, 10)
    )

    entry_palavra = ctk.CTkEntry(
        frame_input,
        placeholder_text="digite uma palavra",
        font=("Alice", 13),
        height=42,
        corner_radius=10,
        border_width=1,
        border_color=MARROM_CLARO,
        fg_color=BRANCO,
        text_color=MARROM
    )

    entry_palavra.pack(
        fill="x",
        expand=True
    )

    # Permite enviar a palavra pressionando a tecla ENTER
    entry_palavra.bind(
        "<Return>",
        processar_envio
    )

# === Área do Histórico / Ranking ===
# Área rolável que mostra as palavras já enviadas e suas posições
    frame_tabela = ctk.CTkScrollableFrame(
        frame_conteudo,
        fg_color=BRANCO,
        corner_radius=12,
        border_width=1,
        border_color=DOURADO_CLARO
    )

    frame_tabela.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=(0, 15)
    )

    # Desenha a cabeça e os detalhes do personagem da tabela
    frame_cabecalho = ctk.CTkFrame(
        frame_tabela,
        fg_color=FUNDO,
        corner_radius=8
    )

    frame_cabecalho.pack(
        fill="x",
        padx=4,
        pady=(4, 6)
    )

    label_palavra = ctk.CTkLabel(
        frame_cabecalho,
        text="PALAVRA",
        font=("Alice", 11, "bold"),
        text_color=MARROM
    )

    label_palavra.pack(
        side="left",
        padx=10,
        pady=5
    )

    label_posicao = ctk.CTkLabel(
        frame_cabecalho,
        text="POSIÇÃO",
        font=("Alice", 11, "bold"),
        text_color=MARROM
    )

    label_posicao.pack(
        side="right",
        padx=10,
        pady=5
    )

    return frame_externo

# 5. TELA: Resultado da Desistência
# Exibe o resultado final quando o usuário desiste.
# A partida é encerrada e não é mais possível enviar tentativas.
def tela_resultado_desistencia(pai, tentativas, palavra_secreta):

    frame_externo = ctk.CTkFrame(
        pai,
        fg_color=FUNDO,
        corner_radius=24,
        width=340,
        height=540
    )
    frame_externo.pack_propagate(False)

    frame_resultado = ctk.CTkFrame(
        frame_externo,
        fg_color=PAINEL,
        corner_radius=20,
        border_width=2,
        border_color=DOURADO_CLARO
    )
    frame_resultado.pack(
        fill="both",
        expand=True,
        padx=4,
        pady=4
    )

    # Decoração superior
    canvas_topo = ctk.CTkCanvas(
        frame_resultado,
        width=300,
        height=70,
        bg=PAINEL,
        highlightthickness=0
    )
    canvas_topo.pack(pady=(18, 0))

    canvas_topo.create_text(
        35, 25,
        text="♥",
        font=("Times New Roman", 20),
        fill=VERMELHO
    )

    canvas_topo.create_text(
        265, 25,
        text="♠",
        font=("Times New Roman", 20),
        fill=AZUL_ESCURO
    )

    canvas_topo.create_line(
        55, 25, 245, 25,
        fill=DOURADO_CLARO,
        width=1
    )

    label_titulo = ctk.CTkLabel(
        frame_resultado,
        text="CONTEXTO",
        font=("Alice", 24, "bold"),
        text_color=MARROM
    )
    label_titulo.pack(pady=(0, 18))

    label_mensagem = ctk.CTkLabel(
        frame_resultado,
        text="Mais sorte na próxima!",
        font=("Alice", 15, "bold"),
        text_color=MARROM
    )
    label_mensagem.pack(pady=(8, 8))

    label_tentativas_resultado = ctk.CTkLabel(
        frame_resultado,
        text=f"Você desistiu em {tentativas} tentativa{'s' if tentativas != 1 else ''}.",
        font=("Alice", 13),
        text_color=MARROM_CLARO
    )
    label_tentativas_resultado.pack(pady=4)

    label_palavra_secreta = ctk.CTkLabel(
        frame_resultado,
        text=f"A palavra secreta era:\n {palavra_secreta.lower()}",
        font=("Alice", 14),
        text_color=MARROM
    )
    label_palavra_secreta.pack(pady=(4, 30))

    # Depois de desistir, a única ação disponível é voltar ao menu.
    criar_botao(
        frame_resultado,
        "↩ VOLTAR AO MENU",
        lambda: mostrar_tela(tela_menu),
        AZUL_ALICE,
        AZUL_HOVER
    )

    return frame_externo


# INICIALIZAÇÃO 
# Exibe o menu principal e inicia o loop de eventos da interface
mostrar_tela(tela_menu)
root.mainloop()