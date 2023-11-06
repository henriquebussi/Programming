from os import system
import random 

conquistas1 = 'Conquistas: '

Kingfinal = 'True King'
revengeorc = 'Vingança(Orc)'
Sinuca = 'Sinuca Master'
Swordsman = 'Caminho da Espada'
marriedeater = 'Mendigo Givaldo'
Lostrevenge = 'Friends of Bow'
Zeus = 'God of Thunder'
Loveshot = 'Love Shot Final'
Reborn = 'Reborn Final'
Bestarcher = 'Best Archer of History, "The Arrow that Burns Everything (True Final)"'
Legendary = 'Legendary Couple of Bow and Arrow, the Dragonslayers (True Final)"'

conquistaappend = []

conquistas = {
  Kingfinal: 1,
  revengeorc: 2,
  Sinuca: 3,
  Swordsman: 4,
  marriedeater: 5,
  Lostrevenge: 6,
  Zeus: 7,
  Loveshot: 20,
  Reborn: 21,
  Bestarcher: 100,
  Legendary: 101
  
}

truetravel = 0
fasttravel = 0
truetravel == False
fasttravel == False


def func1():

  bemvindo = input("""
  Bem vindo ao  
 _____  ____  __  __ __  __ ____     ____  ____   __  _  _____  ____    ____ __  __
|_   _|/ () \|  |/  /\ \/ // () \   | ===|/ () \ |  \| ||_   _|/ () \  (_ (_`\ \/ /
  |_|  \____/|__|\__\ |__| \____/   |__| /__/\__\|_|\__|  |_| /__/\__\.__)__) |__| , 
  
  um jogo de texto, feito apenas por python.

  [1] Jogar
  [2] Conquistas
  [3] Fast Travel
  [4] Créditos.
""")
  system('clear')
  if bemvindo == '1':
    funcinicio()
  elif bemvindo == '2':
    conquistas()
  elif bemvindo == '3':
    fastravel()
  elif bemvindo == '4':
    creditos()
    

def funcinicio():
  nome = input('Digite o nome do seu personagem: ')
  
  system('clear')
  
  escolha_direcao = input("""
  Seu Nome é """+ nome + """ um garoto que vive em uma pequena vila no reino de Westfallen, sua vida era normal, até que depois de voltar da cidade, encontra sua aldeia queimada, com todos os habitantes, inclusive, sua familia, morta.
  
  Depois de se ver sem lar, sem casa, e sem família, """+ nome + """ percebe que agora tem que viver por si só. E depois de fazer suas malas, vai em     busca de sobreviver e de entender oque aconteceu em sua própria vila
  
  Depois de se preparar, """+ nome + """ esta pronto para suas aventuras, para onde ele irá?  
  
  Digite [1] para seguir ao leste em direção a capital
  Digite [2] para seguir ao norte em direção a floresta
""")
  system('clear')
  
  if escolha_direcao == '1':
    func2()
  elif escolha_direcao == '2':
    func3()
  else:
    func1()

def func2():
  print("""
  Depois de um longo percurso, chega na capital, uma cidade enorme.
Aqui, ele iria reconstruir sua vida
  """)
  
  escolha_cidade_trabalho = input("""
  Chegando la, percebe que precisa arrumar um emprego. Na cidade nova: não conhecia ninguem; não tinha moradia e não havia nada que soubesse fazer. Oque você tenta fazer?
  
  Digite [1] para ser criminoso
  Digite [2] para ser mercante
  Digite [3] para não fazer nada da vida
  """)
  system('clear')

  if escolha_cidade_trabalho == '1':
    func4()
  elif escolha_cidade_trabalho == '2':
    func12()
  elif escolha_cidade_trabalho == '3':
    func26()
  else:
    func2()

def func3():
  escolha_branch = input("""
  No caminho pela floresta, percebe marcas de carroças em direção á sua antiga aldeia. E marcas de volta...

  Quanto mais anda, mais recente as marcas são. você nem presta mais atenção aos arredores, apenas quer saber alguma informação sobre aquele incidente.

  Anoitece, e eventualmente chega a uma pequena cidade, já esta cansado e andar naquelas noites é muito perigoso, mas, também tem medo de perder qualquer chance de conseguir alguma informação.

  Digite [1] para mesmo com a noite, você continuar andando em busca de pistas
  Digite [2] para passar a noite e uma taverna na pequena cidade
  """)
  system('clear')

  if escolha_branch == '1':
    func27()
  elif escolha_branch == '2':
    func34()
  else:
    func3()

def func4():
  print("""
  Começa uma vida no crime!
  
  voce começa roubando pequenas lojas até que começa a crescer na vida do crime e é convidado para ser soldado da Gangue BILAU (Batalhão Inteligente de Latrocínio, Automobilismo e Urologismo)
  """)
  
  escolha_mercenario = input("""
  Digite [1] para fazer o maior crime da sua vida
  Digite [2] para Trair a gangue BILAU e virar informante
  Digite [3] para tentar se aproximar do chefe
  """)
  system('clear')
  
  if escolha_mercenario == '1':
    func5()
  elif escolha_mercenario == '2':
    func6()
  elif escolha_mercenario == '3':
    func9()
  else:
    func4()

def func5():
  input("""

██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

  
  você é preso, imediatamente tu é morto pela gangue rival, após isso você aparece estripado na cela.  

  Aperte "enter" para jogar de novo.
  """)
  system('clear')
  func1()

def func6():
  escolha_trair_gangue = input("""
  matar crianças mulheres idosos e roubar inocentes pra conseguir mais informação?

  Digite [1] para Sim
  Digite [2] para Não
  """)
  system('clear')

  if escolha_trair_gangue == '1':
    func7()
  elif escolha_trair_gangue == '2':
    func8()
  else:
    func6()

def func7():
    input("""

██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

  
  você é preso, imediatamente tu é morto pela gangue rival, após isso você aparece estripado na cela.  

  Aperte "enter" para jogar de novo.
  """)
    system('clear')
    func1()

def func8():
  input("""
███████ ██ ███    ██  █████  ██          ███████ ███████ ██      ██ ███████ ██ 
██      ██ ████   ██ ██   ██ ██          ██      ██      ██      ██    ███  ██ 
█████   ██ ██ ██  ██ ███████ ██          █████   █████   ██      ██   ███   ██ 
██      ██ ██  ██ ██ ██   ██ ██          ██      ██      ██      ██  ███       
██      ██ ██   ████ ██   ██ ███████     ██      ███████ ███████ ██ ███████ ██ 


  você consegue informações rasas que conseguem prender 5 integrantes e o subchefe é liberado, agora tu é caçado pela mafia.

  Você consegue despistar a mafia e vive uma vida normal como mercador e nunca mais se envolve com a vida criminosa.

  Aperte "enter" para jogar de novo.
  """)
  system('clear')
  func1()

def func9():
  escolha_prisao = input("""
  você consegue virar subchefe, mas é pego pela policia.
  
  Digite [1] para usar sua influencia e sair da prisão
  Digite [2] para ficar e ajudar seus comparsas
  """)
  system('clear')

  if escolha_prisao == '1':
    func10()
  elif escolha_prisao == '2':
    func11()
  else:
    func9()

def func10():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     


  Você será expulso da mafia, e será caçado pelos BILAU e pela policia.

  Após 2 anos de fuga você é encontrado por um membro de sua antiga mafia, e acaba tomando um tiro.

  Aperte "enter" para jogar de novo.
  """)
  system('clear')
  func1()

def func11():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

      
  Sua gangue entra em guerra com a gangue rival! Vocês ganham, mas você acaba sendo morto na batalha.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func12():
  escolha1_mercante = input("""
  O que você faz?
  
  Digite [1] para criar uma lojinha e começar a vender nela
  Digite [2] para virar um politico
  """)
  system('clear')

  if escolha1_mercante == '1':
    func13()
  
  elif escolha1_mercante == '2':
    func14()
  else:
    func12()

def func13():
  input("""
███████ ██ ███    ██  █████  ██          ████████ ██████  ██ ███████ ████████ ███████ 
██      ██ ████   ██ ██   ██ ██             ██    ██   ██ ██ ██         ██    ██      
█████   ██ ██ ██  ██ ███████ ██             ██    ██████  ██ ███████    ██    █████   
██      ██ ██  ██ ██ ██   ██ ██             ██    ██   ██ ██      ██    ██    ██      
██      ██ ██   ████ ██   ██ ███████        ██    ██   ██ ██ ███████    ██    ███████ 

                                                                                      
  você segue sua vida normal consegue uma esposa, é traído, vive meio pobre mas tem amigos.                                                                             
  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func14():
  escolha_dinheiro = input("""
  Você conseguiu virar uma figura politica, e tem ambições maiores...

  Você acaba sonegando impostos para ter mais dinheiro...

  Digite [1] para comprar apoiadores
  Digite [2] para subornar policiais
  """)
  system('clear')

  if escolha_dinheiro == '1':
    func15()
  elif escolha_dinheiro == '2':
    func16()
  else:
    func14()
  
def func15():
  escolha_apoiadores = input("""
  Você compra apoiadores...

  Você irá fazer um discurso para ganhar votos.

  Digite [1] para fazer discurso apoiando as minorias
  Digite [2] para ser moderado
  Digite [3] para fazer discurso supremacista
  """)
  system('clear')

  if escolha_apoiadores == '1':
    func17()
  elif escolha_apoiadores == '2':
    func18()
  elif escolha_apoiadores == '3':
    func19()
  else:
    func15()

def func16():
  input("""
███████ ██ ███    ██  █████  ██          ████████ ██████  ██ ███████ ████████ ███████ 
██      ██ ████   ██ ██   ██ ██             ██    ██   ██ ██ ██         ██    ██      
█████   ██ ██ ██  ██ ███████ ██             ██    ██████  ██ ███████    ██    █████   
██      ██ ██  ██ ██ ██   ██ ██             ██    ██   ██ ██      ██    ██    ██      
██      ██ ██   ████ ██   ██ ███████        ██    ██   ██ ██ ███████    ██    ███████ 


  Você é preso, e solto após 5 anos de prisão.

  Após ser solto você segue sua vida normalmente consegue uma esposa, é traído, vive meio pobre mas tem amigos.

  Aperte "enter" para jogar de novo.
  """)
  system('clear')
  func1()

def func17():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     


  não funcionou, o rei não gostou e você será executado.

  Aperte "enter" para jogar de novo.
  """)
  system('clear')
  func1()

def func18():
  escolha_promeca = input("""
  Você faz promessas, principalmente ao exercito, atrás de votos.

  Digite [1] para prometer a erradicação da fome
  Digite [2] para prometer guerras, poder e glória
  """)
  system('clear')

  if escolha_promeca == '1':
    func20()
  elif escolha_promeca == '2':
    func21()
  else:
    func18()

def func19():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     


  Você faz um discurso supremacista, mas a minoria não gosta e te emboscam em um beco...

  Aperte "enter" para jogar de novo.
  """)
  system('clear')
  func1()

def func20():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     


  Só a peble te dá ouvidos, o rei não gosta e você é executado.

  Aperte "enter" para jogar de novo.
  """)
  system('clear')
  func1()

def func21():
  escolha_população = input("""
  Você consegue uma grande parte da população ao seu lado. Você deverá escolher como será seu governo

  Digite [1] para ser pacifista
  Digite [2] para ser Militarista, Armamentista, Salazarista e Antissemita
  """)
  system('clear')

  if escolha_população == '1':
    func22()
  elif escolha_população == '2':
    func23()
  else:
    func21()

def func22():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     


  O rei aproveita sua misericordia e corta sua cabeça.

  Aperte "enter" para jogar de novo.
  """)
  system('clear')
  func1()

def func23():
  escolha_golpe = input("""
  Você consegue dar um golpe de estado e se torna monarca.

  Nenhum Pais te reconhece e acabam fazendo uma coalizão contra você e seu reino.

  Digite [1] para lutar sozinho essa guerra 
  Digite [2] para tentar usar a diplomacia a seu favor
  """)
  system('clear')

  if escolha_golpe == '1':
    func24()
  elif escolha_golpe == '2':
    func25()
  else:
    func23()

def func24():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     


  Você não consegue ganhar uma guerra sozinho, tu é morto e sua cabeça é pendurada no centro da cidade, fim do seu reinado tirano.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func25():
  input("""
██    ██  ██████   ██████ ███████ 
██    ██ ██    ██ ██      ██      
██    ██ ██    ██ ██      █████   
 ██  ██  ██    ██ ██      ██      
  ████    ██████   ██████ ███████
  
███████ ███████ 
██      ██      
███████ █████   
     ██ ██      
███████ ███████

████████  ██████  ██████  ███    ██  █████  
   ██    ██    ██ ██   ██ ████   ██ ██   ██ 
   ██    ██    ██ ██████  ██ ██  ██ ███████ 
   ██    ██    ██ ██   ██ ██  ██ ██ ██   ██ 
   ██     ██████  ██   ██ ██   ████ ██   ██

██████  ███████ ██  ██ 
██   ██ ██      ██  ██ 
██████  █████   ██  ██ 
██   ██ ██      ██  
██   ██ ███████ ██  ██ 


  Depois de uma guerra sangrenta você acaba sendo reconhecido e se tornando um verdadeiro rei!

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  conquistaappend.append(Kingfinal)
  fasttravelbrabo()

def func26():
  input("""
███████ ██ ███    ██  █████  ██          ██████  ██████   ██████  ██   ██  █████  
██      ██ ████   ██ ██   ██ ██          ██   ██ ██   ██ ██    ██  ██ ██  ██   ██ 
█████   ██ ██ ██  ██ ███████ ██          ██████  ██████  ██    ██   ███   ███████ 
██      ██ ██  ██ ██ ██   ██ ██          ██   ██ ██   ██ ██    ██  ██ ██  ██   ██ 
██      ██ ██   ████ ██   ██ ███████     ██████  ██   ██  ██████  ██   ██ ██   ██ 


voce vira mendigo e mora debaixo da ponte, depois de 10 anos pega uma doença e morre.

Aperte "enter" para jogar de novo.
  """)
  system('clear')
  fasttravelbrabo()
  func1()


def func27():
  escolha_continuar = input("""
  Depois de um tempo caminhando no escuro, finalmente acha outro sinal de vida. E olha só, as marcas de carroça também acabavam.

  Em sua frente acontecia um acampamento em grupo, tinha quase 7 individuos, de todas raças possiveis, tinha 2 humanos, 2 elfos, 1 anão e 2 Orcs.

  O que você faz?

  Digite [1] para você se aproximar
  Digite [2] para você se aproximar cuidadosamente e para tentar ouvir alguma informação
  Digite [3] para você voltar a cidade e dormir na taverna
  """)
  system('clear')

  if escolha_continuar == '1':
    func28()
  elif escolha_continuar == '2':
    func29()
  elif escolha_continuar == '3':
    func30()
  else:
    func27()
    
def func28():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

    Você se aproxima do grupo, eles o identificam e o matam sem dó, e usam sua carne para se alimentarem.

    Aperte "enter" para jogar de novo 
  """)
  system('clear')
  func1()


def func29():
  escolha_conversa = input("""
  Você acaba escutando a história: Aquele grupo realmente tinha queimado a vila, mas, não com a aprovação de todos, na verdade, apenas com a aprovação do lider.

  O grupo se separa, com aqueles leais ao líder  continuando, enquanto o resto se separa.

  Os que saíram foram a metade do grupo, saiu uma bela Elfa, que saiu silenciosamente com um olhar sério, saiu um Orc, que saiu puto, e um humano que saiu chorando.

  O que você faz?

  Digite [1] para tentar conversar com a Elfa
  Digite [2] para tentar conversar com o Humano 
  Digite [3] para tentar conversar com o Orc
  """)
  system('clear')

  if escolha_conversa == '1':
    func31()
  elif escolha_conversa == '2':
    func32()
  elif escolha_conversa == '3':
    func33()
  else:
    func29()

def func30():
  func38()

def func31():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░    

      A elfa acha que você é uma pessoa hostil, então ela dá um tiro em seu cranio.

      Aperte "enter" para jogar de novo.
  """)
  system('clear')
  func1()

def func32():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░    

      O humano pega você de surpresa e o mata com diversas facadas no abdômen

      Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func33():
  input("""
██▒   █▓ ██▓ ███▄    █   ▄████  ▄▄▄       ███▄    █  ▄████▄   ▄▄▄      
▓██░   █▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▒████▄     ██ ▀█   █ ▒██▀ ▀█  ▒████▄    
 ▓██  █▒░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒██  ▀█▄  ▓██  ▀█ ██▒▒▓█    ▄ ▒██  ▀█▄  
  ▒██ █░░░██░▓██▒  ▐▌██▒░▓█  ██▓░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ 
   ▒▀█░  ░██░▒██░   ▓██░░▒▓███▀▒ ▓█   ▓██▒▒██░   ▓██░▒ ▓███▀ ░ ▓█   ▓██▒
   ░ ▐░  ░▓  ░ ▒░   ▒ ▒  ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░ ▒▒   ▓▒█░
   ░ ░░   ▒ ░░ ░░   ░ ▒░  ░   ░   ▒   ▒▒ ░░ ░░   ░ ▒░  ░  ▒     ▒   ▒▒ ░
     ░░   ▒ ░   ░   ░ ░ ░ ░   ░   ░   ▒      ░   ░ ░ ░          ░   ▒   
      ░   ░           ░       ░       ░  ░         ░ ░ ░            ░  ░

▄████▄   ▒█████   ███▄    █  ▄████▄   ██▓     █    ██  ██▓▓█████▄  ▄▄▄      
▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █ ▒██▀ ▀█  ▓██▒     ██  ▓██▒▓██▒▒██▀ ██▌▒████▄    
▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▒▓█    ▄ ▒██░    ▓██  ▒██░▒██▒░██   █▌▒██  ▀█▄  
▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒██░    ▓▓█  ░██░░██░░▓█▄   ▌░██▄▄▄▄██ 
▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░▒ ▓███▀ ░░██████▒▒▒█████▓ ░██░░▒████▓  ▓█   ▓██▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░ ▒░▓  ░░▒▓▒ ▒ ▒ ░▓   ▒▒▓  ▒  ▒▒   ▓▒█░
  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░  ░  ▒   ░ ░ ▒  ░░░▒░ ░ ░  ▒ ░ ░ ▒  ▒   ▒   ▒▒ ░
░        ░ ░ ░ ▒     ░   ░ ░ ░          ░ ░    ░░░ ░ ░  ▒ ░ ░ ░  ░   ░   ▒   
░ ░          ░ ░           ░ ░ ░          ░  ░   ░      ░     ░          ░  ░


  Na verdade, o Orc era o bonzinho da historia, então você conversa com ele, e mata todo o grupo que botou fogo na vila.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  conquistaappend.append(revengeorc)
  fasttravelbrabo()


def func34():
  escolha_truco_ou_sinuca = input("""
  Você decide passar a noite em uma taverna da pequena cidade.

  Antes de dormir, você é convidado a jogar algum jogo.

  Qual jogo você irá jogar?

  Digite [1] para jogar truco apostado
  Digite [2] para jogar sinuca
  """)
  system('clear')

  if escolha_truco_ou_sinuca == '1':
    func35()
  elif escolha_truco_ou_sinuca == '2':
    func36()
  else:
    func34()

def func35():
  truco = random.choice([5, 0])
  
  escolha_aceitar_ou_recusar = input("""
  Ele ganha, mas seus adversarios querem uma revanche, dobrando a aposta.

  O que você faz?

  Digite [1] para aceitar
  Digite [2] para recusar
  """)
  system('clear')

  if escolha_aceitar_ou_recusar == '1':
    if truco % 2 == 0:
      input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██    
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒   
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░   
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░   
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓    
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒    
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░    
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░    
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░      


      Você ganha de novo, e seus adversarios, furiosos, o matam.

      Aperte "enter" para jogar de novo
      """)
      system('clear')
      func1()
    else:
      input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██    
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒   
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░   
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░   
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓    
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒    
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░    
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░    
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░  


      Você perde, e como um pobre, você tem que pagar com a vida.

      Aperte "enter" para jogar de novo
      """)
      system('clear')
      func1()
  if escolha_aceitar_ou_recusar == '2':
    func38()
  else:
    func35()

def func36():
  escolha_sinuca = input("""
  Você acaba caindo com um profissional e perde.

  Após jogar um pouco, você dorme.
  
  Depois de acordar, tenta seguir os rastros, mas não consegue achar nada.

  O que você faz ?

  Digite [1] para desistir de achar a carroça e continua na pequena cidade
  Digite [2] seguir ao norte, procurando algo
  """)
  system('clear')

  if escolha_sinuca == '1':
    func39()
  elif escolha_sinuca == '2':
    func40()
  else:
    func36()

def func38():
  escolha_oque_fazer = input("""
  Você vai dormir...
  
  Depois de acordar, tenta seguir os rastros, mas não consegue achar nada.

  O que você faz ?

  Digite [1] para desistir de achar a carroça e continua na pequena cidade
  Digite [2] seguir ao norte, procurando algo
  """)
  system('clear')

  if escolha_oque_fazer == '1':
     func39()
  elif escolha_oque_fazer == '2':
    func40()
  else:
    func36()

def func39():
  input("""
███████ ██ ███    ██  █████  ██          ███████ ███████ ██      ██ ███████ 
██      ██ ████   ██ ██   ██ ██          ██      ██      ██      ██    ███  
█████   ██ ██ ██  ██ ███████ ██          █████   █████   ██      ██   ███   
██      ██ ██  ██ ██ ██   ██ ██          ██      ██      ██      ██  ███    
██      ██ ██   ████ ██   ██ ███████     ██      ███████ ███████ ██ ███████ 


  Acaba começando a trabalhar na taverna, faz amigos e começa um caso com Klefera, dona do estabelecimento e uma mulher da raça dos anãos.

  Você vive uma vida pacifica na pequena cidade, acaba se casando com Klefera, vive administrando a taverna, ou seja, festa, rum e jogos todo dia. Vira nível profissional no sinuca e tem muitos amigos

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  conquistaappend.append(Sinuca)
  fasttravelbrabo()
  

def func40():
  escolha_fera = input("""
  Você continua seu caminho pela floresta, agora já desacreditado. E ouvia barulhos estranhos ao redor. Estava com medo.

  E de repente é atacado por uma Quimera, um Leão com uma segunda cabeça de bode e com uma cauda de cobra.

  O que você faz ?

  Digite [1] para combater a fera
  Digite [2] para deixar para deus matar
  Digite [3] para fugir da fera
  """)
  system('clear')

  if escolha_fera == '1':
    func41()
  elif escolha_fera == '2':
    func42()
  elif escolha_fera == '3':
    func43()
  else:
    func40()

def func41():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░    
      

  Você tenta fazer algo, mas a fera fica mais furiosa ainda e arranca sua cabeça violentamente.

  Aperte "enter" para jogar de novo.
  """)
  system('clear')
  func1()

def func42():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

      
  Deus não ligou para seu pedido, e deixa você morrer... AMÉM

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func43():
  escolha_fugir = input("""
  Você tenta fugir, mas a fera puxa seu pé e rasga seu peito.

  De repente uma flecha é atirada na sua direção atingindo a fera na cabeça.

  O que você faz?

  Digite [1] para fugir 
  Digite [2] para se aproximar do arqueiro 
  """)
  system('clear')

  if escolha_fugir == '1':
    func44()
  elif escolha_fugir == '2':
    func200()
  else:
    func43()

def func200():
  aproximate = input("""
  Como você ira se aproximar?

  
  [1] Investir Rapidamente em direção a ela
  [2] Se Aproximar Lentamente
  """)
  system('clear')

  if aproximate == '1':
    func201()
  elif aproximate == '2':
    func202()
  else:
    func200()

def func201():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

      
  Quando você decide ir um pouco mais rápido você já se depara morto

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func202():
  dar_ideia = input("""
  Depois de um tempo andando, você chega no arqueiro, na verdade, arqueirA, ela era uma Elfa linda de cabelos loiros que havia disparado
  
  [1] Tentar dar ideia na mina
  [2] Conversar como um ser humano racional
  """)
  system('clear')

  if dar_ideia == '1':
    func203()
  elif dar_ideia == '2':
    func45()

def func203():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     


Oque você esperava??

Gentileza tem limites né! Tu morre

Aperte "enter" para jogar de novo

""")
  system('clear')
  func1()

  
def func44():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     


  Quando você tenta fugir o arqueiro o identifica como ameaça e o mata com uma flechada na cabeça.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()


def func45():
  escolha_chegar = input("""
  Ela se mostra muito mais gentil que você imaginava e depois de um tempo conversando você acaba virando amigo dela, e depois de mais um tempo conversando, ela te conta o porque dela estar na floresta. De como ela foi ordenada a atirar em civis de uma pequena aldeia, e de como essa experiencia foi traumática para ela.

  Antes você tinha duvidas, mas agora é certeza, era sua vila a que ela estava falando.

  O que você faz?

  Digite [1] para dizer para a Elfa que era a sua vila da qual ela estava falando 
  Digite [2] para não dizer nada
  """)
  system('clear')

  if escolha_chegar == '1':
    func46()
  elif escolha_chegar == '2':
    func47()
  else:
    func45()

def func46():
  escolha_vinganca = input("""
  Quando você fala a verdade sobre sua aldeia ela se enche de culpa e tristeza, ela era realmente uma boa pessoa, apenas um pouco timida...

  E com mais raiva ainda de sei antigo líder,  ela te convida para uma vingança em conjunto.

  Digite [1] para aceitar
  Digite [2] para recusar
  """)
  system('clear')

  if escolha_vinganca == '1':
    func48()
  elif escolha_vinganca == '2':
    func49()
  else:
    func46()

def func47():
  escolha_planejar = input("""
  Você presta muita atenção no que ela fala, na verdade, você pergunta coisas muito especificas sobre o lider e outras coisas, ela estranha, mas fica quieta...

  Depois daquela conversa, você, utilizando as informações que ela havia te dado na conversa. Era a ultima decisão, PLANEJAR A VINGANÇA?

  Digite [1] para planejar a vingança
  Digite [2] para deisitir
  """)
  system('clear')

  if escolha_planejar == '1':
    func50()
  elif escolha_planejar == '2':
    func51()
  else:
    func47()


def func48():
  arco = input("""
  Vocês planejam a vingança.

  O plano seria simples: em uma semana, vocês iriam invadir o acampamento principal do grupo que havia assassinado sua aldeia.

  Durante esse tempo, descobre o nome da elfa: Sgàthach Vanyar, mas ela o deixa apenas a chamar de Scat.

  Scat acaba, nesse tempo, te ensinando varias coisas, inclusive, como manusear um arco.

  Você acaba se mostrando talentoso com o arco, e logo Scat fica mais animada ainda com o fato de te ensinar.

  Você precisa fazer um arco, e preferencialmente, como o de Scat, um arco feito utilizando materiais da floresta...

  Agora você fará seu arco.

  Como irá ser o corpo do arco?

  Digite [1] para ser feito de galhos das arvores
  Digite [2] para ser feito de madeira lisa
  Digite [3] para ser feito de pedra 
  Digite [4] ???
  """)
  system('clear')

  if arco == '4':
    func_secreto()

  input("""
  Como irá ser a corda?

  Digite [1] para a corda ser de linha
  Digite [2] para a corda ser de crina de cavalo
  """)
  system('clear')

  input("""
  Como irá ser as flechas?

  Digite [1] para serem feitas de galhos e pedras lisas
  Digite [2] para serem feitas de osso
  """)
  system('clear')

  if arco == '1' or arco == '2' or arco == '3':
    func96()
  else:
    func48()

def func49():
  input("""
  ███████ ██ ███    ██  █████  ██          ███████ ███████ ██      ██ ███████ 
  ██      ██ ████   ██ ██   ██ ██          ██      ██      ██      ██    ███  
  █████   ██ ██ ██  ██ ███████ ██          █████   █████   ██      ██   ███   
  ██      ██ ██  ██ ██ ██   ██ ██          ██      ██      ██      ██  ███    
  ██      ██ ██   ████ ██   ██ ███████     ██      ███████ ███████ ██ ███████ 


  Ela fica admirada com sua maturidade mas mesmo assim tenta te convidar, depois de mais uma recusa ela acaba desistindo do plano.

  Você desistiu da sua vingança, mas conseguiu algo muito mais importante, uma amizade.
  
  Ela te ensina sobre a arte do arco e você vira parceiro dela como caçador/mercenário.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()
  

def func50():
  escolha_aceitar = input("""
  É obvio que você iria tentar! Você planeja sua vingança sozinho, e utiliza as poucas informações que sabe para formular um plano.
  Você tem apenas uma informação relevante: a localização não exata da base daquele grupo. e você vai usar muito bem essa informação...
  Brevemente você vai para capital, você iria precisar se preparar para sua vingança.

  O que você faz ?

  Digite [1] para trabalhar por recursos
  Digite [2] para roubar recursos
  """)
  system('clear')

  if escolha_aceitar == '1':
    func65()
  elif escolha_aceitar == '2':
    func66()
  else:
    func50()


def func51():
  input("""
███████ ██ ███    ██  █████  ██          ██████  ██████   ██████  ██   ██  █████  
██      ██ ████   ██ ██   ██ ██          ██   ██ ██   ██ ██    ██  ██ ██  ██   ██ 
█████   ██ ██ ██  ██ ███████ ██          ██████  ██████  ██    ██   ███   ███████ 
██      ██ ██  ██ ██ ██   ██ ██          ██   ██ ██   ██ ██    ██  ██ ██  ██   ██ 
██      ██ ██   ████ ██   ██ ███████     ██████  ██   ██  ██████  ██   ██ ██   ██ 


Você estava com a faca e o queijo na mão e acabou desistindo...

Você morre arrependido,  sem objetivo...

Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()


def func_secreto():
  labirinto = input("""
  Olha só... parece que você quer algo mais ambicioso né?
  Cuidado, esse caminho pode trazer sua morte, você ainda assim, quer continuar?

  Digite [1] para continuar
  Digite [2] para desistir
  """)
  system('clear')

  if labirinto == '1':
    labirinto_continuacao()
  elif labirinto == '2':
    func52()
  else:
    func_secreto()

def labirinto_continuacao():
  func_caminho_labirinto = input("""
  Não sei se é Corajoso... Ou se é burro, mas enfim, vamos continuar.
  
  Você ouve falar de um tal Labirinto, que quem terminar, recebe uma arma dos deuses.
  Você vai para o labirinto sem falar nada para Scat, ela sabia que aquele lugar era muito perigoso e não queria te ver lá. A entrada era em um túnel, embaixo do palácio próximo.
  Tinha varias pessoas lá, algumas estavam apenas para vender, ou nos avisar, outras, como você, queriam entrar no labirinto. Para entrar no labirinto você precisa comprar um tipo especifico de arma, de um metal estranho, pois outras armas, com outros metais não funcionaria.

  Logo você compra um arco desse com o resto de dinheiro que você ainda tinha. O labirinto era feito de um tipo de pedra especial e tinha varias entradas.
  
  por qual caminho ir ?

  Digite [1] para ir pela esquerda
  Digite [2] para ir pela direita 
  """)
  system("clear")

  if func_caminho_labirinto == '1':
    func53()
  elif func_caminho_labirinto == '2':
    func54()
  else:
    labirinto_continuacao()


def func52():
  input("""
  Ok, justificável, nesse caso, o corpo de seu arco será feito de ossos

  Como irá ser a corda?

  Digite [1] para a corda do seu arco ser feita de linha
  Digite [2] para a corda do seu arco ser feita de crina de cavalo 
  """)
  system('clear')

  osso = input("""
  Como irá ser as flechas do seu arco?

  Digite [1] para ser feito de galho e pedra polida
  Digite [2] para ser feito de ossos
  """)
  system('clear')

  if osso == '1' or osso == '2':
    func96()
  else:
    func52()

def func53():
  lado_esquerdo = input("""
  Você anda mais um pouco até chegar a mais uma divisão, o caminho esquerdo parecia estar congelado, enquanto o direito estava queimado.

  Você vai por qual lado?

  Digite [1] para ir pelo lado queimado
  Digie [2] para ir pelo lado congelado
  """)
  system('clear')

  if lado_esquerdo == '1':
    func55()
  elif lado_esquerdo == '2':
    func56()
  else:
    func53()

def func54():
  caminho_cor = input("""
  E agora começara, o Labirinto do Minotauro...

  Você anda reto até chegar a mais uma divisão, o caminho esquerdo estava pintado vermelho, enquanto o direito estava pintado azul.

  Digite [1] para ir pelo caminho azul
  Digite [2] para ir pelo caminho vermelho
  """)
  system('clear')

  if caminho_cor == '1':
    func57()
  elif caminho_cor == '2':
    func58()
  else:
    func54()

def func55():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

      
  Você mal consegue aguentar o calor absurdo que ali havia, e para completar, você é recebido por um monstro de pé grande fumante, que te mata lentamente.
  """)
  system('clear')
  func1()

def func56():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

      
  Você mal consegue aguentar o frio infernal que ali havia, e para completar, você é recebido por um monstro das neves, que te mata rapidamente.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func57():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██    
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒   
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░   
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░   
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓    
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒    
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░    
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░    
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░      

      
  Conforme você vai se aprofundando no caminho azul, você acaba ficando sonolento, e depois de um tempo, você dorme ali mesmo, e nunca mais acorda. Seu sonho é o seus mais profundos desejos.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func58():
  divisao = input("""
  Você segue o caminho da vermelho, e conforme mais profundo você vai, mais lembranças passadas aparecem, memórias com sua antiga família...
  Você consegue seguir, mas chorando. Mais uma divisão pode ser vista, agora, bem mais... misterioso? O caminho da esquerda era feito de pedra, com pilares de estrutura greco-romana, mas   era um caminho cinza, parecia mais seguro, mas parecia "errado". Enquanto o caminho da direita era um caminho quase florestal, com pichações nas paredes, que eram feitas de madeira,   parecia mais perigoso, mas parecia "certo".

  Para qual lado você vai?

  Digite [1] para ir pelo lado de pedras
  Digite [2] para ir pelo lado florestal
  """)
  system('clear')

  if divisao == '1':
    func59()
  elif divisao == '2':
    func60()
  else:
    func58()

def func59():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██    
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒   
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░   
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░   
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓    
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒    
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░    
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░    
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░      

      
  Você anda naquele caminho perfeitamente construído, até que o teto começa a lentamente abaixar, você tenta ir mais rápido, mas não importa o quão mais longe você vai, não tem como fugir.
  Você é morto esmagado...

  Aperte "enter" para jogar de novo.
  """)
  system('clear')
  func1()

def func60():
  angelical_metal = input("""
  Mesmo com o piso desregulado e alguns buracos no chão, você continua seu caminho normal. Mais uma divisão pode ser vista, agora de maneira bem mais direta, no lado esquerdo, se vê um caminho todo branco, com uma fumaça branca quase angelical, era um caminho muito bonito e reconfortante, o caminho direito era um caminho feito de metal puro, mas dava para ver o caminho todo dali, não era um caminho bonito e provocava uma insegurança.

  Qual caminho você vai ?

  Digite [1] para ir no caminho angelical
  Digite [2] para ir no caminho de metal
  """)
  system('clear')

  if angelical_metal == '1':
    func61()
  elif angelical_metal == '2':
    func62()
  else:
    func60()

def func61():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██    
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒   
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░   
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░   
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓    
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒    
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░    
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░    
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   

      
  Você segue seu caminho no caminho angelical, que foi, inicialmente, muito confortável e reconfortante, só que, quanto mais tempo se passava, você ficava a duvidar se aquele era o caminho certo, você é contaminado pela insegurança, e você acaba caindo naquela fumaça e morre...

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func62():
  caminho_branco_ou_preto = input("""
  Você segue no caminho metal, foi uma experiencia interessante, de uma grande incerteza e insegurança no começo, mas conforme o tempo, com o final se aproximando, você se sentiu muito realizado.

  Você continua seu caminho e encontra mais uma divisão, você já estava começando a ficar cansado disso, mas enfim, ambos os caminhos pareciam uma sala de um reino, com a única diferença sendo que o caminho á esquerda era todo branco, enquanto o caminho direito era todo preto.

  Qual caminho você vai?

  Digite [1] para ir no caminho preto
  Digite [2] para ir no caminho branco
  """)
  system('clear')

  if caminho_branco_ou_preto == '1':
    func63()
  elif caminho_branco_ou_preto == '2':
    func64()
  else:
    func62()

def func63():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██    
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒   
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░   
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░   
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓    
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒    
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░    
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░    
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░ 

      
  Você acaba seguindo seu caminho pelo caminho real preto, até chegar em uma sala de um rei, e o rei estava ali.
  O rei preto te desafia para um duelo, e o mesmo te deixa começar, e depois de uma flechada nada eficaz, ele rapidamente te mata com sua espada.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()
  
def func64():
  input("""
██    ██  ██████   ██████ ███████     
██    ██ ██    ██ ██      ██          
██    ██ ██    ██ ██      █████       
 ██  ██  ██    ██ ██      ██          
  ████    ██████   ██████ ███████ 

███████ ███████ 
██      ██      
███████ █████   
     ██ ██      
███████ ███████ 

████████  ██████  ██████  ███    ██  ██████  ██    ██     
   ██    ██    ██ ██   ██ ████   ██ ██    ██ ██    ██     
   ██    ██    ██ ██████  ██ ██  ██ ██    ██ ██    ██     
   ██    ██    ██ ██   ██ ██  ██ ██ ██    ██ ██    ██     
   ██     ██████  ██   ██ ██   ████  ██████   ██████ 

███████ ███████ ██    ██ ███████ 
   ███  ██      ██    ██ ██      
  ███   █████   ██    ██ ███████ 
 ███    ██      ██    ██      ██ 
███████ ███████  ██████  ███████ 

 
  
  Você acaba seguindo seu caminho pelo caminho real branco, até chegar em uma sala de um rei, e o rei estava ali.
  O rei branco te desafia para um duelo, e o mesmo começa rápido, e depois de desviar do ataque, você da uma flechada na cabeça dele, o matando. E depois de mata-lo, uma grande luz te   cobre, para logo você surgir em um tipo salão dourado, com um lindo altar dourado, e em cima dele, um arco.
  Um arco dourado com detalhes de relâmpagos, e suas flechas... Não tem flechas?

  Você pega o arco dourado e logo em seguida você é teletransportado para fora do labirinto. Você surge de um trovão próximo e logo, animado pela nova arma, vai diretamente para a base inimiga. Chegando em uma montanha próxima, você se prepara para testar seu arco atirando na grande casa de longe. Você puxa a linha divina, e solta como se estivesse atirando uma flecha.
  Quando você atira, um enorme trovão engole toda casa que acaba sendo aniquilada.

  Depois desse disparo, você é teleportado para os céus, onde você recebe o titulo de Deus dos Trovões por Zeus, que logo morre. Agora você era um Deus, que viveria por milhares de anos até ter que se passar seu legado, assim como Zeus.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  fasttravelbrabo()

def func65():
  desistir_ou_nao = input("""
  Você acaba conseguindo um trampo em um restaurante de dia enquanto pagava para estudar a arte da espada a noite. Você acaba se mostrando bem talentoso na espada, e em pouco tempo, vira o mais talentoso de sua sala, e em torneios, acaba se tornando um grande competidor e um dos maiores prodigios da capital. Seu mestre, impressionado e orgulhoso pelo seu desenvolvimento rápido, te dá de presente de aniversário uma espada incrível, e te convida para trabalhar com ele.

  O que você faz?

  Digite [1] para aceitar
  Digite [2] para recusar
  """)
  system('clear')

  if desistir_ou_nao == '1':
    func67()
  elif desistir_ou_nao == '2':
    func68()
  else:
    func65()

def func66():
  roubar = input("""
  Você vai em um bar, e você encontra um cavaleiro bêbado. 

  O que você faz?

  Digite [1] para tentar roubar a espada do cavaleiro
  Digite [2] para tentar achar outra pessoa
  """)
  system('clear')

  if roubar == '1':
    func69()
  elif roubar == '2':
    func70()
  else:
    func66


def func67():
  input("""
██    ██  ██████   ██████ ███████     
██    ██ ██    ██ ██      ██          
██    ██ ██    ██ ██      █████       
 ██  ██  ██    ██ ██      ██          
  ████    ██████   ██████ ███████  

██    ██ ██ ██████   ██████  ██    ██ 
██    ██ ██ ██   ██ ██    ██ ██    ██ 
██    ██ ██ ██████  ██    ██ ██    ██ 
 ██  ██  ██ ██   ██ ██    ██ ██    ██ 
  ████   ██ ██   ██  ██████   ██████  

██    ██ ███    ███ 
██    ██ ████  ████ 
██    ██ ██ ████ ██ 
██    ██ ██  ██  ██ 
 ██████  ██      ██ 

███████ ███████ ██████   █████  ██████   █████   ██████ ██   ██ ██ ███    ███ 
██      ██      ██   ██ ██   ██ ██   ██ ██   ██ ██      ██   ██ ██ ████  ████ 
█████   ███████ ██████  ███████ ██   ██ ███████ ██      ███████ ██ ██ ████ ██ 
██           ██ ██      ██   ██ ██   ██ ██   ██ ██      ██   ██ ██ ██  ██  ██ 
███████ ███████ ██      ██   ██ ██████  ██   ██  ██████ ██   ██ ██ ██      ██ 


  Você, emocionado e feliz pelas palavras de seu mestre, aceita e continua na vida da espada, desistindo de sua vingaça. E você continuou evoluindo, e depois de se consolidar como um dos melhores espadachins da capital, se despede em lagrimas do seu mestre para fazer sua própria escola de esgrima. Você conseguiu se consolidar como um dos melhores espadachins do reino, você ensinou guerreiros, lendas e reis. Você viveu uma vida confortável e conseguiu o respeito dos mestres espadachins, da nobreza, da burguesia. Na verdade, você conseguiu o respeito de todos

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  fasttravelbrabo()
  

def func68():
  print("""
  Mesmo emocionado e com lagrimas, você recusa, falando de seus objetivos, seu mestre, mesmo triste, respeita sua opinião e fala que você pode voltar quando quiser. A Espada te deu tudo, um mestre, que quase foi um pai. Te deu uma nova família, sua classe. Te deu um objetivo de vida...
  
  Foi muito doloroso recusar, e você fala para seu mestre que você ira voltar quando tudo isso acabar. Ele chora e você sai também chorando. 

  Depois de 1 ano, você se despede da capital, para ir em direção a sua vingança, mas agora, muito mais preparado, com uma mochila com comida e uma barraca, e é claro, com sua espada   incrível.

  No caminho para lá, você encontra a Elfa de novo, e em um pequeno churrasco com ela, você conta para ela seus planos, ela tenta se prontificar para te ajudar, mas você logo recusa, dizendo que essa era sua batalha.

  Ela entende, mas mesmo assim, se prontifica a pelo menos te ajudar a guardar suas coisas enquanto iria acontecer o ataque.

  Ela também confirma a localização da base e diz como era o Líder que ordenou o ataque, e era um Orc grande e forte, e que eu teria que ter cuidado com ele, e com o irmão dela, que também estava lá. E, para finalizar, em um tom cômico mas também mórbido, você pergunta para ela se, em uma possível morte, se ela poderia te enterrar e avisar seu mestre na capital.

  Ela fala que é melhor você voltar vivo, mas se isso acontecer, ela ira fazer seu funeral.

  E com a consciência agora limpa, se despede da Elfa , uma pessoa que se mostrou ser uma verdadeira amiga. 
  
  Agora, realmente rumo em direção a base...
  """)
  func73()

def func69():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░    

      
  Você consegue a roubar, mas um dia depois você é morto encurralado em um beco por cavaleiros que viram você roubando

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func70():
  roubar2 = input("""
  Você acha uma bela nobre bêbada, ela estava indo para fora e parecia estar mal. Não tinha mais ninguém no bar que parecesse ter dinheiro.

  O que você faz?

  Digite [1] para tentar roubar a bolsa dela
  Digite [2] para ajudar ela
  """)
  system('clear')

  if roubar2 == '1':
    func71()
  elif roubar2 == '2':
    func72()
  else:
    func70

def func71():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░    

      
  A principio você conseguiu roubar mulher, mas cavaleiros ao redor percebem e te espacam até a morte.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func72():
  input("""
███████ ██ ███    ██  █████  ██          ███████ ███████ ██      ██ ███████ 
██      ██ ████   ██ ██   ██ ██          ██      ██      ██      ██    ███  
█████   ██ ██ ██  ██ ███████ ██          █████   █████   ██      ██   ███   
██      ██ ██  ██ ██ ██   ██ ██          ██      ██      ██      ██  ███    
██      ██ ██   ████ ██   ██ ███████     ██      ███████ ███████ ██ ███████ 


  Você ajuda ela e depois a consola, a nobre tinha sido traída pelo esposo e estava afogando as magoas no bar. Se sentindo grata ela te da moradia e você acaba convivendo com ela.
  
  Você desiste da sua vingança, mas acaba conseguindo uma casa, uma amiga, que depois de um tempo, se tornou sua esposa, e uma vida consolidada e feliz como nobre.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  fasttravelbrabo()
  
def func73():
  ir_ou_n = input("""
  Depois de um tempo andando, percebe que estava na em cima de um grande planalto, e com sua vista de lá, consegue ver de longe a base. Era uma casa grande de madeira cercada por grandes cercas de madeira com pedras em cima. Tudo isso e ainda cercado por uma grande floresta.
  
  Se aproximando mais da casa, passando pela grande floresta correndo silenciosamente. Encontra já sinal de vida humana, na verdade, encontra um elfo armado com uma espada. Ele parecia   muito com sua amiga Elfa, ele tinha cabelos loiros, cara séria e era bonito.

  O que você faz?

  Digite [1] para evitar ele
  Digite [2] para ir em direção a ele
  """)
  system("clear")

  if ir_ou_n == '1':
    func74()
  elif ir_ou_n == '2':
    func75()
  else:
    func73()

def func74():
  entrada = input("""
  Você consegue contornar o elfo, mas percebe que não conseguirá entrar sem passar por ele.

  O que você faz?

  Digite [1] para passar pelo elfo
  Digite [2] para tentar achar outra entrada
  """)
  system('clear')

  if entrada == '1':
    func75()
  elif entrada == '2':
    func76()
  else:
    func74()




def func75():
  passar_pelo_elfo = input("""
  Você se aproxima empunhando sua espada em direção a ele e logo aponta a espada em direção ao elfo. Ele logo percebeu suas intenções e se prepara para batalha entre espadas. 

  O que você faz?

  Digite [1] para esperar o elfo fazer algo 
  Digite [2] par atacar primeiro
  """)
  system('clear')

  if passar_pelo_elfo == '1':
    func77()
  elif passar_pelo_elfo == '2':
    func78()
  else:
    func75()

def func76():
  batalha_sim_nao = input("""
  Você contorna toda casa em busca de uma entrada, até achar uma pequena entrada atrás da casa. Você entra, e se vê dentro do campo de treinamento do grupo. E no caminho para a casa principal, você avista dois   gêmeos humanos(um homem e uma mulher) e um anão conversando na porta da casa.

  O que você faz?

  Digite [1] para se aproximar para a batalha
  Digite [2] para evitar o conflito
  Digite [3] para tentar matá-los silenciosamente 
  """)
  system('clear')

  if batalha_sim_nao == '1':
    func93()
  elif batalha_sim_nao == '2':
    func94()
  elif batalha_sim_nao == '3':
    func95()
  else:
    func76()


def func77():
  morrer_ou_nao = random.choice([5, 0])
  
  if morrer_ou_nao % 2 == 0:
    print("""
    O Elfo logo, rapidamente, avança em sua direção.
    
    Você consegue repelir o ataque dele por puro reflexo, para logo o ferir com sua espada.""")
    func84()
  else:
    input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░    

    O Elfo logo, rapidamente, avança em sua direção.
    
    Você não consegue fazer nada a tempo e morre com sua cabeça cortada

    Aperte "enter" para jogar de novo
    """)
    system('clear')
    func1()
    
    

def func78():
  atacar_primeiro = input("""
  Você, logo, rapidamente avança na direção de seu adversário, ele continua parado.

  Como você ataca?

  Digite [1] para mirar na cabeça
  Digite [2] para mirar no peito
  Digite [3] mirar no braço dominante e buscar um combate verdadeiro
  """)
  system('clear')

  if atacar_primeiro == '1':
    func79()
  elif atacar_primeiro == '2':
    func80()
  elif atacar_primeiro == '3':
    func81()
  else:
    func78()

def func79():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░    

      
  Ele facilmente se esquiva para logo estocar sua espada na sua cabeça.
  Você morre empalado por seu oponente

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func80():
  estocar_ou_cortar = input("""
  Você tenta estocar ou desferir um corte em seu oponente ?

  Digite [1] para estocar
  Digite [2] para desferir um corte
  """)
  system('clear')

  if estocar_ou_cortar == '1':
    func82()
  elif estocar_ou_cortar == '2':
    func83()
  else:
    func80()

def func81():
  print("""
  Ele fica surpreso com sua ação e baixa a guarda, permitindo ser acertado por você""")
  func84()

def func82():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░    

      
  Ele Logo deflete seu ataque para contra-atacar e te estoca, você morre com seu corção perfurado por ele

  Aperte "enter para jogar de novo
  """)
  system('clear')
  func1()

def func83():
  print("""
  Depois de se defender, começou uma pequena batalha, e depois de um tempo, ficou claro que você era um melhor espadachim, com você conseguindo o ferir.""")
  func84()


def func84():
  matar_poupar = input("""
  Agora, na vantagem, você se permite ser cada vez mais ofensivo. Ele era bom, mas você ainda assim, era um pouco melhor. E com o tempo, você começou a acertar cada vez mais ataques, se   colocando cada vez mais como o mais provável vencedor. Ele foi ficando cada vez mais na desvantagem, conseguindo ser acertado varias vezes em sequencia. Até finalmente você dar um golpe fatal na barriga, ele cai no chão, ele estava a beira da morte.

  Você o mata, ou o poupa?

  Digite [1] para matá-lo
  Digite [2] para poupar sua vida
  """)
  system('clear')

  if matar_poupar == '1':
    func86()
  elif matar_poupar == '2':
    func85()
  else:
    func84()



def func85():
  print("""
  Mesmo você tendo o poupado, ele morre momentos depois, pelo golpe fatal
  """)
  func87()


def func86():
  matar_ouvir = input("""
  Antes de o matar, o Elfo pede um ultimo pedido. 
  
  Você o ouve, ou o mata ?

  Digite [1] para matá-lo
  Digite [2] para ouvir seu pedido
  """)
  system('clear')

  if matar_ouvir == '1':
    func87()
  elif matar_ouvir == '2':
    func88()
  else:
    func86()

def func87():
  andares = input("""
  Você não o ouve e logo depois, o mata empalado. Logo você continua sua jornada em direção a base.
  Você entra na casa e percebe que no primeiro andar da casa, não tem ninguém e que atras da casa tem 3 indivíduos, você esta cansado da batalha anterior.

  O que você faz?

  Digite [1] para ignorar os individuos
  Digite [2] para avançar neles
  """)
  system("clear")

  if andares == '1':
    func89()
  elif andares == '2':
    func90()
  else:
    func87()

def func88():
  avancar_ou_ignorar = input("""
  Você decide ouvi-lo, e em seu ultimo pedido, o Elfo pede para avisar a irmã dele sobre sua morte. E para finalizar, ele fala que foi a melhor luta que ele já esteve. Você o mata perfurando seu coração.
  Logo você continua sua jornada em direção a base. Você entra na casa e percebe que no primeiro andar da casa, não tem ninguém e que atras da casa tem 3 indivíduos, você esta cansado da batalha anterior.

  O que você faz?

  Digite [1] para ignorar os individuos e ir para o segundo andar
  Digite [2] para avançar neles
  """)
  system('clear')

  if avancar_ou_ignorar == '1':
    func89()
  elif avancar_ou_ignorar == '2':
    func90()
  else:
    func88()

def func89():
  orc = input("""
  Você segue para o segundo andar e logo se depara com uma grande porta, diferente das outras. Com certeza o Orc estava ali

  O que você faz?

  Digite [1] para tentar matá-lo silenciosamente
  Digite [2] para ir em um confronto sincero
  """)
  system('clear')

  if orc == '1':
    func91()
  elif orc == '2':
    func92()
  else:
    func89()


def func90():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   


      Você não ouviu que você estava cansado? Você morre facilmente pelo trio com uma flecha na cabeça.

      Aperte "enter" para jogar de novo 
  """)
  system('clear')
  func1()


def func91():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░    


      Você corre e tenta cortar a cabeça do Orc silenciosamente, o Orc desvia e te contra ataca com uma marretada em sua cabeça.
  """)

def func92():
  raiva = input("""
  Entrando naquela porta, você vê o grande Orc na sua frente. Ele era um grande Orc verde de 2,5m de altura, e muito musculoso a definição de "Berserk". Ele estava confuso do porque você estava ali, mas foi apenas você falar o nome da sua aldeia que ele abriu um grande sorriso. E você, furioso por aquele sorrisinho, pergunta o porque ele ordenou o ataque. E a resposta? Simples, porque ele queria. 

  Você estava confuso e... perplexo
  Ele estava sorrindo, e falando como ele testou a lealdade, o quão longe seus subordinados iriam o seguir. E ele falou que o resultado foi satisfatório, os que saíram tinham que sair, ele falou como ficou decepcionado do próprio irmão e da Elfa sair, mas que agora, em 1 ano, o grupo estava muito mais forte e leal que antes.

  E aquela raiva era tudo oque restava para aquela batalha, como você ira começar essa batalha?

  Digite [1] para Atacar Rapidamente
  Digite [2] para esperar o movimento dele
   """)
  system('clear')

  if raiva == '1':
    func113()
  elif raiva == '2':
    func114()
  else:
    func92()

def func93():
  chance_matar_morrer = random.choice([5, 0])
  
  aproximar_batalha = input("""
  Você lentamente vai em direção do grupo, que te vê e fica surpreso mas se prepara para a luta. O Grupo era composto pelo Anão, que estava com roupas    de ferreiro e tinha um martelo.O Humano Macho, que estava com roupas de arqueiro e portava um arco. E a Humana Fêmea, que estava com roupas de       ladina/ladra e que tinha duas adagas

  O que você faz?

  Digite [1] para esperar eles fazerem algo
  Digite [2] para avançar em direção ao Trio
  """)
  system('clear')

  if aproximar_batalha == '1':
    if chance_matar_morrer % 2 == 0:
      input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██    
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒   
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░   
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░   
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓    
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒    
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░    
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░    
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   

      
      Você morre com uma flecha na cabeça disparada pelo arqueiro

      Aperte "enter" para jogar de novo
      """)
      system('clear')
      func1()
    else:
      aceitar_duelo = input("""
      Você consegue defletir uma flecha.
      
      Logo você avança rapidamente, o arqueiro disparava suas flechas, mas ou você desviava, ou você defletia. Com você chegando cada vez mais perto, a       Ladina veio avançando em direção á você, propondo, indiretamente um duelo.

      O que você faz?

      Digite [1] para aceitar o duelo
      Digite [2] para recusar o duelo
      """)
      system('clear')

      if aceitar_duelo == '1':
        func100()
      elif aceitar_duelo == '2':
        func101()
      else:
        func102()
  if aproximar_batalha == '2':
    aceitar_duelo = input("""
    Logo você avança rapidamente, o arqueiro disparava suas flechas, mas ou você desviava, ou você defletia. Com você chegando cada vez mais perto, a Ladina veio avançando em direção á você, propondo, indiretamente um duelo.

    O que você faz?

    Digite [1] para aceitar o duelo
    Digite [2] para recusar o duelo
    """)
    system('clear')

    if aceitar_duelo == '1':
      func100()
    elif aceitar_duelo == '2':
      func101()
    else:
      func102()
  

def func94():
  conflito = random.choice([5,0])

  if conflito % 2 == 0:
    input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

      
    No seu caminho silencioso, o humano macho te vê e com seu arco, te mata.

    Aperte "enter" para jogar de novo
    """)
    system('clear')
    func1()
  else:
    orc_silencioso_ou_n_matar = input("""
    Você segue silenciosamente, rente a parede, até chegar em uma janela próxima, que você pula para entrar na casa. E depois de olhar um pouco o primeiro andar, você não acha ninguém, então você segue para o segundo andar. Você segue para o segundo andar e logo se depara com uma grande porta, diferente das outras, além disso,  você consegue ouvir uma grave  vindo daquele quarto. Com certeza o Orc estava ali.

    O que você faz?

    Digite [1] para ir para o combate
    Digite [2] para tentar matar silenciosamente
    """)
    system('clear')

    if orc_silencioso_ou_n_matar == '1':
      func92()
    elif orc_silencioso_ou_n_matar == '2':
      func109()
    else:
      func110()
def func95():
  escolha_silenciosa_teste = input("""
  Você acaba esperando até que os 2 humanos se afastam do anão.

  O Que você faz?

  Digite [1] para tentar matar os anãos furtivamente
  Digite [2] para Tentar matar os dois humanos furtivamente
  """)
  system('clear')

  if escolha_silenciosa_teste == '1':
    func111()
  elif escolha_silenciosa_teste == '2':
    func112()
  else:
    func95()


def func96():
  input("""
    Então é isso! Parabéns por fazer um arco!

  E no tempo restante, você acaba treinando mais ainda com Scat, até chegar o ultimo dia antes de acontecer o plano

  E no ultimo dia, você e Scat acabam fazendo um pequeno churrasco para comemorar esse tempo passado e para marcar que em um dia, vocês estariam arriscando a própria vida para cumprir uma vingança

  E já antes de dormir, enquanto afiava suas flechas, vê a garota dormindo, seu coração estava batendo mais rápido...

  Você percebeu ali, quem você precisa proteger e o risco real desse plano, o risco de a perder.

  """)
  system('clear')

  funcgroup1()

def func100():
  forma_de_batalha = input("""
  Você honradamente aceita o duelo com a Ladina, que começa já rápido, com você e a garota batalhando muito rápido.

  O que você faz?

  Digite [1] para diminuir a velocidade e tentar dominar a batalha com habilidade pura
  Digite [2] para continuar batalhando de forma rapida
  """)
  system('clear')

  if forma_de_batalha == '1':
    func103()
  elif forma_de_batalha == '2':
    func104()
  else:
    func100()


def func101():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

      
  Você acaba ignorando a garota, que fica muito puta e começa a te perseguir com muita velocidade. E quando você chega perto do arqueiro, você é parado pelo anão e seu martelo. Agora, cercado e com uma Ladina muito puta, tu é morto com uma adaga na garganta e uma flecha na cabeça.

  Aperte "enter" para jogar de novo.
  """)
  system('clear')
  func1



def func102():
  aceitar_duelo = input("""
  Logo você avança rapidamente, o arqueiro disparava suas flechas, mas ou você desviava, ou você defletia. Com você chegando cada vez mais perto, a     Ladina veio avançando em direção á você, propondo, indiretamente um duelo.

  O que você faz?

  Digite [1] para aceitar o duelo
  Digite [2] para recusar o duelo
  """)
  system('clear')

  if aceitar_duelo == '1':
    func100()
  elif aceitar_duelo == '2':
    func101()
  else:
    func102()

def func103():
  matala_poupala = input("""
  Você, demonstrando toda sua esgrima, domina o duelo lindamente, não deixando a mulher te atacar, e a atacando constantemente. E depois de um tempo, você ganha, a colocando para o chão, e ameaçando cortar a cabeça da mulher. 

  O que você faz?

  Digite [1] para poupa-la
  Digite [2] para matá-la
  """)
  system('clear')

  if matala_poupala == '1':
    func105()
  elif matala_poupala == '2':
    func106()
  else:
    func103()

def func104():
  duelo_rapido = random.choice([5, 0])

  print("""
  Vocês continuam com esse duelo que era um primor pros olhos, um duelo incrível a alta velocidade, ela se feria, você se feria. Esse era um duelo incrivel.
  """)
  
  if duelo_rapido % 2 == 0:
    func107()
  else:
    func108()

def func105():
  
  renderse_ou_nao = random.choice([5, 0])
  
  if renderse_ou_nao % 2 == 0:
    input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██    
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒   
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░   
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░   
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓    
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒    
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░    
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░    
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   

      
    Quem diria que você não podia confiar em uma ladra. Quando você baixa a guarda ela joga uma de suas adagas na cabeça, te matando.

    Aperte "enter" para jogar de novo
    """)
    system('clear')
    func1()
  else:
    input("""
███████ ██ ███    ██  █████  ██          ███████ ███████ ██      ██ ███████ ██ 
██      ██ ████   ██ ██   ██ ██          ██      ██      ██      ██    ███  ██ 
█████   ██ ██ ██  ██ ███████ ██          █████   █████   ██      ██   ███   ██ 
██      ██ ██  ██ ██ ██   ██ ██          ██      ██      ██      ██  ███       
██      ██ ██   ████ ██   ██ ███████     ██      ███████ ███████ ██ ███████ ██ 


    Ela aceita que perdeu e realmente se rende. Seus companheiros, percebendo que você não quer matar eles, ficam curiosos do porque você esta querendo atacar aquele lugar. Depois de contar o porque, eles entendem o seu motivo. O homem e o anão ficaram envergonhados, até porque, estavam no grupo naquele ataque, e mesmo que estivessem enojados, acreditavam que seu líder tivesse algum motivo oculto. Mas mesmo assim, saíram do seu caminho pacificamente em sinal de respeito, mas continuariam no grupo por lealdade.

    Agora a garota, que nunca tinha ouvido falar do incidente, tinha ficado totalmente desacreditada  e enojada, e se prontificou para te ajudar na sua luta contra o lider. Ela te guiou   até o quarto do líder, e juntos, conseguiram derrotar o grande Orc. Depois de completar sua vingança, ela pergunta para você se ela não pode viver com você, já que ela não tem para onde ir
Você aceita, e na capital, vocês viram o casal de mercenários, conhecidos como "Blades".

    Aperte "enter" para jogar de novo
    """)
    system('clear')
    func1()

def func106():
  escolha_orc_silenciosamente = input("""
  Você logo corta rapidamente a cabeça da linda mulher. Seu irmão, o arqueiro, possesso pelo desejo de vingança, começa a atirar cada vez mais flechas. Ele estava em pânico, estava desacreditado que sua irmã havia morrido. E você se aproximava cada vez mais, apenas defletindo e desviando das flechas. E em um movimento impulsivo e protestado pelo próprio anão, o arqueiro tentou avançar fisicamente contra você. E quando ele chega perto o suficiente, você enfia sua espada na garganta do arqueiro. E o Anão, desacreditado que seus companheiros foram mortos assim, desiste e te deixa ir. Agora Você entra na casa e procura por algo no primeiro andar. Não acha, então vai para o segundo andar

  Você segue para o segundo andar e logo se depara com uma grande porta, diferente das outras
Com certeza o Orc estava ali

  O que você faz?

  Digite [1] para tentar matá-lo silenciosamente
  Digite [2] para ir em um confronto sincero
  """)
  system('clear')

  if escolha_orc_silenciosamente == '1':
    func91()
  elif escolha_orc_silenciosamente == '2':
    func92()
  else:
    func106()


def funcgroup1():
  atacar_desistir_elfo = input("""
Depois de um tempo andando, vamos para uma área próxima, mas mais alta

  A base era uma casa grande de madeira cercada por grandes cercas de madeira com pedras em cima. Tudo isso e ainda cercado por uma grande floresta


  Você começa a vasculhar se tinha pessoas próximas, e tinha, você vê um Elfo com uma espada, bem parecido com Scat, e quando você conta para ela sua descoberta, ela reluta um pouco mas logo fala que esse era seu irmão

Até que vocês veem ele olhar em sua direção, ele pode ou não ter os visto, oque fazer?

  [1] Atacar ele primeiro
  [2] Desistir da posição e torcer para ele não ter visto
""")
  system('clear')
  if atacar_desistir_elfo == '1':
    funcgroup2()
  elif atacar_desistir_elfo == '2':
    loveshot1()
  else:
    funcgroup1()


def loveshot1():
  disparar_flecha = input("""
  Você da a volta em volta da casa, mas no caminho, você vê de uma janela do segundo andar um grande monstro forte e verde, era o Orc

Você fala para Scat, que você quer ter a honra, ela entende e te deixa fazer isso

Disparar uma flecha nele?

  [1] Sim
""")
  system('clear')
  if disparar_flecha == '1':
    loveshot2()
  else:
    loveshot1()

def loveshot2():
  mirar_onde = input("""
Mirar onde?

  [1] Mirar na cabeça
  [2] Mirar no peito
  """)
  system('clear')

  if mirar_onde == "1":
    loveshot3()
  elif mirar_onde == "2":
    loveshotdeath1()
  else:
    loveshot2()
  
def loveshotdeath1():
  print("""
  Depois de puxar a corda do arco até o limite, se puxasse mais, sua mão começaria a tremer e perderia sua precisão""")
  system('clear')
  loveshotdeath2()

def loveshotdeath2():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██    
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒   
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░   
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░   
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓    
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒    
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░    
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░    
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   

      
  Você acerta o peito do Orc com sucesso, mas o mesmo, com sua pilha de músculos, não morreu por isso.
E quando ele te olha de longe, ele sai por um tempo apenas para voltar com uma lança
E ele, com sua grande força, joga a lança em você, causando até um impacto no ar, de tanta força e velocidade

Você nem consegue reagir, sua cabeça é perfurada brutalmente pela lança

    Aperte "enter" para jogar de novo
    """)
  system('clear')
  func1()


def loveshot3():
  puxar_mais = input("""
Você percebe que teria que superar os limites para matar ele com apenas uma flecha na cabeça
  
Sua mão esta leve e seu arco esta flexível

Puxar mais a corda?

  [1] Puxar mais
  [2] Atirar
  """)
  system('clear')

  if puxar_mais == '1':
    loveshot4()
  elif puxar_mais == '2':
    loveshotdeath3()

def loveshotdeath3():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   


    Você atira a flecha muito fraca, e não causa nenhum dano no mesmo. Mas revelou sua posição, que foi aproveitada pelo o Elfo, que rapidamente vai em sua direção sem você saber

Ele te mata decapitando você

      Aperte "enter" para jogar de novo 
  """)
  system('clear')
  func1()

def loveshot4():
  puxar_mais2 = input("""
Sua mão esta mais firme e seu arco esta normal
  
Puxar mais a corda?
  
  [1] Puxar mais
  [2] Atirar
""")
  system('clear')

  if puxar_mais2 == '1':
    loveshot5()
  elif puxar_mais2 == '2':
    loveshotdeath4()
  else:
    loveshot4()


def loveshotdeath4():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   


  Se fosse qualquer um, literalmente qualquer um, até mesmo um Orc normal morreria, só que não era um Orc comum. era simplesmente o Líder do Grupo

A flecha perfura a cabeça do Orc, mas fica poucos centímetros do seu cérebro
  
Ele, olha para você, sorrindo. Você fica apavorado, que tipo de monstro era aquele.
  
  Para logo ele virem sua direção, destruindo tudo em seu caminho, inclusive a parede e logo dá um longo pulo, e com sua marreta, ele te esmaga de cima, destruindo sua cabeça junto de seu corpo

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def loveshot5():
  atirar = input("""
Sua mão esta tremendo e não firme, e seu arco esta literalmente no seu limite

Não tem como puxar mais a corda

  [1] Atirar
""")
  system('clear')
  
  if atirar == '1':
    loveshot6()
  else:
    loveshot5()

def loveshot6():
  print("""
  Você iria atirar, assim mesmo, tremendo e com pouca firmeza, você só estava torcendo para conseguir acertar ele até que...

  Scat segura sua mão e o arco, assim distribuindo a pressão do arco entre vocês dois, você logo olha para ela confuso, apenas para ver ela sorrindo

E agora, com mais firmeza e estabilidade, você mira na grande cabeça do Orc, você estava tenso, mas com a companhia de Scat, você fica mais relaxado

  A flecha exibia pequenos traços flamejantes, para logo você soltar junto de Scat a corda

  A flecha faz um belo rastro de chamas e acerta, a cabeça do Orc, que só percebe no ultimo momento, mas não consegue parar a flecha em chamas, que perfura a cabeça do Orc
  """)
  system('clear')
  loveshot7()

def loveshot7():
  print("""
  Depois de acertarem, ambos olham um para o outro, vocês estavam surpresos, mais felizes, e suas cabeças se aproximam lentamente até finalmente se beijarem
  """)
  system('clear')
  loveshot8()

def loveshot8():
  input ("""
 ___       ________  ___      ___ _______      
|\  \     |\   __  \|\  \    /  /|\  ___ \     
\ \  \    \ \  \|\  \ \  \  /  / | \   __/|    
 \ \  \    \ \  \\\  \ \  \/  / / \ \  \_|/__  
  \ \  \____\ \  \\\  \ \    / /   \ \  \_|\ \ 
   \ \_______\ \_______\ \__/ /     \ \_______\
    \|_______|\|_______|\|__|/       \|_______|

 ________  ___  ___  ________  _________   
|\   ____\|\  \|\  \|\   __  \|\___   ___\ 
\ \  \___|\ \  \\\  \ \  \|\  \|___ \  \_| 
 \ \_____  \ \   __  \ \  \\\  \   \ \  \  
  \|____|\  \ \  \ \  \ \  \\\  \   \ \  \ 
    ____\_\  \ \__\ \__\ \_______\   \ \__\
   |\_________\|__|\|__|\|_______|    \|__|
   \|_________| 
   
 ________ ___  ________   ________  ___          
|\  _____\\  \|\   ___  \|\   __  \|\  \         
\ \  \__/\ \  \ \  \\ \  \ \  \|\  \ \  \        
 \ \   __\\ \  \ \  \\ \  \ \   __  \ \  \       
  \ \  \_| \ \  \ \  \\ \  \ \  \ \  \ \  \____  
   \ \__\   \ \__\ \__\\ \__\ \__\ \__\ \_______\
    \|__|    \|__|\|__| \|__|\|__|\|__|\|_______|

    Vocês depois vivem em uma pequena casa na floresta, namorando, e depois, casados.

Vocês continuam sua vida no arco e flecha e trabalham como grande arqueiros no meio mercenário e respeitados no meio profissional da arquearia, conhecidos por todo reino como o "Casal que nunca erra uma flecha"

  Aperte "enter" para jogar de novo

    """)
  system('clear')
  func1()


  
def funcgroup2():
  archer_elf = input("""
  Você logo atira nele, que logo deflete sua flecha e olha diretamente para você, para logo avançar em direção á você
  
  Você e Scat logo continuam a atirar no Elfo, que desviava ou defletia todas flechas. Logo uma flecha é atirada em uma arvore próximas á você. Parecia que um Arqueiro também tinha entrado na batalha do lado do Elfo, vocês tem que dividir o trabalho em dois
  
  [1] Cuidar do Arqueiro
  [2] Cuidar do Elfo 
  """)
  system('clear')

  if archer_elf == '1':
    funcgroup3()
  elif archer_elf == '2':
    funcgroup7()
  else:
    funcgroup2()

def funcgroup3():
  search_more = input("""
Você logo começa a procurar incessantemente seu adversário mas não consegue o achar
  
  [1] Procurar mais
  [2] Esperar um ataque dele para ver de onde vem
  """)
  system('clear')

  if search_more == '1':
    funcgroupdeath1()
  elif search_more == '2':
    funcgroup4()
  else:
    funcgroup3()

def funcgroupdeath1():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   
      
  Você continua a procurar e você o consegue o achar, mas apenas para você achar que ele já havia disparado uma flecha contra você

Você morre com uma flecha em seu coração

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()
  
def funcgroup4():
  atirararcher = input("""
  Você vê uma flecha vindo do canto inferior direito, vinha do pátio daquela casa

  Você logo pensa em como o atirar

  [1] Tentar atirar no arco do arqueiro
  [2] Tentar atirar na cabeça do arqueiro
  """)
  system('clear')

  if atirararcher == '1':
    funcgroupdeath2()
  elif atirararcher == '2':
    funcgroup5()
  else:
    funcgroup4()

def funcgroupdeath2():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   
      
Você erra e ele te vê

Ele é mais rapido e te mata primeiro

  Aperte "enter" para jogar de novo
""")
  system('clear')
  func1()

def funcgroup5():
  atirar_head = input("""
Você puxa a corda de seu arco, você puxa Sua respiração pode ser ouvida, e logo você dispara.

Você acerta a flecha e o mata com uma flecha na cabeça

Você logo olha para o seu lado e você vê o Elfo se aproximando enquanto Scat tentava atirar nele

Você tenta prever o trajeto dele para atirar, onde tentar atirar?

  [1] Tentar atirar na cabeça
  [2] Tentar atirar na perna direita
  """)
  system('clear')

  if atirar_head == '1':
    funcgroupdeath3()
  elif atirar_head == '2':
    funcgroup6()
  else:
    funcgroup5()

def funcgroupdeath3():
  sacrifice = input("""
  Você erra, e o Elfo continua seu caminho, Scat atira e o Elfo deflete, na verdade, ele estava tendo dificuldades, mas ele logo deu uma ultima acelerada, e isso decretou o destino dela, a não ser que...
  
  [1] Não se Sacrificar
  [2] Se Sacrificar
  """)
  system('clear')

  if sacrifice == '1':
    funcgroupdeath4()
  elif sacrifice == '2':
    reborn1()
  else:
    funcgroupdeath3()

def funcgroupdeath4():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   
O Elfo a mata, e você vê a morte dela parado...

Ele logo avança contra você e você não tem muito oque fazer, você morre com um corte do peito

  Aperte "enter" para jogar de novo

""")
  system('clear')
  func1()

def reborn1():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   
      
Você logo se joga na frente de Scat, sua ultima visão foi de Scat, apavorada e assustada, você morreu sorrindo

  Aperte "enter" para jogar de novo
""")
  system('clear')
  reborn2()

def reborn2():
  input("""
  ...
  """)
  system('clear')
  reborn3()

def reborn3():
  input("""
  ....
  """)
  system('clear')
  reborn4()

def reborn4():
  input("""
  .....
  """)  
  system('clear')
  reborn5()

def reborn5():
  input("""
  Você é realmente sortudo ein...
  """)
  system('clear')
  reborn6()

def reborn6():
  input("""
  Você acorda em um tipo de casa de madeira, aos redores você vê coisas estranhas como poções
  """)
  system('clear')
  reborn7()

def reborn7():
  input("""
██████╗ ███████╗██████╗  ██████╗ ██████╗ ███╗   ██╗    ███████╗██╗███╗   ██╗ █████╗ ██╗     
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗████╗  ██║    ██╔════╝██║████╗  ██║██╔══██╗██║     
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝██╔██╗ ██║    █████╗  ██║██╔██╗ ██║███████║██║     
██╔══██╗██╔══╝  ██╔══██╗██║   ██║██╔══██╗██║╚██╗██║    ██╔══╝  ██║██║╚██╗██║██╔══██║██║     
██║  ██║███████╗██████╔╝╚██████╔╝██║  ██║██║ ╚████║    ██║     ██║██║ ╚████║██║  ██║███████╗
╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝

E na sua frente, você vê Scat, com roupas de maga e chorando ao te ver, você fica confuso, mas era real

Ela havia te ressuscitado

 Você viveu com ela depois, e por pedido dela, evitando todo tipo de perigo, vocês se casam e você vive junto dela pelo resto de sua vida naquela pequena casa
 """)
  system('clear')
  func1()

def funcgroup6():
  input("""
Você consegue o acertar o jogando para o chão, e logo Scat dispara, colocando uma flecha na cabeça do irmão

Ela olha triste para o irmão, mas para logo voltar a si

Vocês ainda tem que enfrentar o Orc
""")
  system('clear')
  orcbattle()

def funcgroup7():
  arrow = input("""
  Você logo troca de lado com Scat e começa a cuidar do Elfo, ele estava rapidamente se aproximando pela floresta, como o parar?
  [1] Tentar acertar apenas uma flecha certeira, prevendo o caminho perfeitamente e atirar
  [2] Tentar o acertar com varias flechas, mas não conseguindo com 100% de certeza
  """)
  system('clear')

  if arrow == '1':
    funcgroup8()
  elif arrow == '2':
    bestarcher1()
  else:
    funcgroup7()

def bestarcher1():
  input("""
  Ele não desacelera, e continua rapidamente em sua direção e em uma distancia bem mais perto, com ele defletindo todas suas flechas, ele acelera mais ainda e...
  """)
  system('clear')
  viver_ou_morrer = random.choice([5, 0])
  
  if viver_ou_morrer % 2 == 0:
    bestarcher2()
  elif viver_ou_morrer % 2 == 1:
    bestarcherdeath1()
  else:
    bestarcher1()

def bestarcherdeath1():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   
  Ele consegue, com sua grande velocidade, perfurar seu coração com sua espada

    Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def bestarcher2():
  input("""
Ele estava á centímetros de te matar até que...

Scat te joga para longe e se sacrifica por você, te dando mais uma chance de viver
""")
  system('clear')
  bestarcher3()

def bestarcher3():
  shoot_or_attack = input("""
Você fica perplexo com a morte de Scat, justo a única coisa que você não queria perder naquele momento

Você fica furioso

Muito furioso


E o Elfo também para, por um momento, mas apenas para voltar a avançar contra você

[1] Atirar mesmo de perto
[2] Tentar atacar fisicamente
""")
  system('clear')
  if shoot_or_attack == '1':
    bestarcher4()
  elif shoot_or_attack == '2':
    bestarcherdeath2()
  else:
    bestarcher3()

def bestarcherdeath2():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░    
  Você, comparado á ele no duelo físico, é nada.

E ele prova isso, te matando cortando sua cabeça rapidamente

  Aperte "enter" para jogar de novo
""")
  system('clear')
  func1()

def bestarcher4():
  input("""
  Você ainda estava no chão

Você estava vulnerável

Mas mesmo assim, você pega o arco de Scat que esta na chão, você mira e atira

Ele morre com uma flecha flamejante na cabeça
""")
  system('clear')
  bestarcher5()

def bestarcher5():
  puxar_ou_atirar = input("""
  Você nem tem tempo para ficar surpreso com as flechas flamejantes para logo você ter que desviar de novo de uma flecha do arqueiro inimigo
  
  Você logo pega cobertura em uma arvore qualquer, se abaixa, e se ajoelha em uma posição que consegue ver o outro arqueiro, seus olhos brilham em vermelho infernal

  [1] Atirar
  [2] Puxar e mirar mais
  """)
  system('clear')
  
  if puxar_ou_atirar == '1':
    bestarcherdeath3()
  elif puxar_ou_atirar == '2':
    bestarcher6()

def bestarcherdeath3():
  shoot1 = input("""
  Você erra
  
  [1] Atirar
  """)
  system('clear')
  
  if shoot1 == '1':
    bestarcherdeath4()
  else:
    bestarcherdeath3()

def bestarcherdeath4():
  shoot2 = input("""
  Você erra

  [1] Atirar
  """)
  system('clear')

  if shoot2 == '1':
    bestarcherdeath5()
  else:
    bestarcherdeath4()

def bestarcherdeath5():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   
      
      Antes mesmo de você conseguir atirar ele te percebe e atira uma flecha em você primeiro, te matando""")
  system('clear')
  func1()
  
def bestarcher6():
  input("""
  E agora, puxando até mais que normalmente você consegue, você atira no arqueiro, o ar sofre impacto, e com um grande rastro de fogo no céu, a flecha o mata, com a cabeça dele tendo um grande buraco com marcas de fogo magma

  Os outros inimigos que estavam perto do arqueiro ficam apavorados com o que aconteceu e rapidamente fogem
  """)
  system('clear') 
  bestarcher7()

def bestarcher7():
  shoot_distance = input("""
  E depois de um pequeno momento, o Orc salta de um quarto do segundo andar da casa quebrando toda parede e cai perto de você

  O Orc era enorme, com mais de 2 metros de altura, e ele era literalmente uma pilha de músculos, ele estava com sua marreta na sua mão direita e uma lança na mão esquerda


  Falar que você não ficou intimidado seria mentira, mas você logo aparece na frente dele, ele estava sorrindo maniacamente, e você, mesmo sério, abriu sem querer um sorrisinho

Ele logo, rapidamente, avança em você

  [1] Não se mexer e disparar
  [2] Manter a distância e continuar disparando de longe
  """)
  system('clear') 

  if shoot_distance == '1':
    bestarcherdeath6()
  elif shoot_distance == '2':
    bestarcher8()
  else:
    bestarcher7()

def bestarcherdeath6():
  input("""
  
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░    
      
Mesmo que não parecesse, o Orc, mesmo grande, era bem rápido e conseguiu chegar em você no mesmo tempo que você disparou

E assim foi, ele estocou contra você no mesmo tempo que você atirou nele

Você com seu coração perfurado, enquanto o Orc morreu com sua flecha com calor nível magma

Mas pelo menos no final, você conseguiu sua vingança
  """)
  system('clear')
  func1()

def bestarcher8():
  input("""
  Ele avançou e tentou te estocar, apenas para você recuar e atirar uma flecha nele, que também desviou
    
  Vocês dois sorriram
  
  E a situação continuou assim por um tempo, você desviava, ele também, até que depois dele te atacar, você desvia para o lado e acerta o braço esquerdo do Orc
  
Ele recua, logo fumaça começa sair do seu corpo, ele parecia estar queimando

Ele larga a marreta para o chão e apenas segura sua lança com sua mão direita
""")
  system('clear') 
  bestarcher9()

def bestarcher9():
  input("""
  E depois dessa mudança, ele acabou ficando muito mais rápido que antes, além de sua lança estar literalmente pegando fogo. Então só estava dando tempo apenas para se desviar, você nem conseguia atacar de volta
  
  Até que depois de você de você desviar de uma estocada da lança flamejante do Orc, você é surpreendido com um golpe da parte do bastão da lança na sua cabeça, para logo ele quase estocar perfeitamente no seu estomago, apenas para você desviar e para logo fazer uma grande distância
  """)
  system('clear') 
  bestarcher10()

def bestarcher10():
  input("""
  E agora, com uma distância entre vocês, o Orc segura lança, e de repente um grande fogo cobre ele e a lança, e logo ele arremessa essa lança de maneira a fazer impacto no ar, e um enorme fogo cobre a lança e aos a redores, tudo ao redor parecia estar reagindo

  Imagina um grande fogo vindo em direção a você á grande velocidade

  Era quase impossível você conseguir acertar uma flecha nele agora, aquele calor junto da velocidade estava criando uma grande onda de calor quente vindo em direção á você""")
  system('clear') 
  bestarcher11()

def bestarcher11():
  input("""
  Até que...

  Você logo dispara sua flecha, que assim como o do Orc, fez impacto no ar, só que diferente das outras, estava muito mais quente, mas muito mais. Sua flecha foi envolvido em algo parecido com um dragão de magma enquanto derretia tudo oque estava perto, até que aconteceu o momento do embate entre lança e flecha, ele esperava te ver morto mas...

  "Nunca escutou que o magma é muito mais quente que o fogo?" Você logo diz

  Sua flecha derrete completamente a lança e anula completamente a onda de calor, apenas para trazer um calor ainda mais escaldante para a região.

  Lugares onde a lança queimava, sua flecha derretia

  E a flecha seguiu até o Orc, que olhou com admiração para aquela grande flecha. A flecha completamente aniquilou tudo em seu caminho, inclusive o Orc, que virou cinzas enquanto sorria

  Parece que ele finalmente teve um oponente digno""")
  system('clear') 
  bestarcher12()

def bestarcher12():
  input("""
  E você cai no chão, olhando o arco de Scat nas suas mãos. Você logo sorri, finalmente você vingou sua família e sua amiga

  Você desmaia logo depois
""")
  system('clear') 
  bestarcher13()

def bestarcher13():
  input("""
████████╗██████╗ ██╗   ██╗███████╗    ███████╗██╗███╗   ██╗ █████╗ ██╗        
╚══██╔══╝██╔══██╗██║   ██║██╔════╝    ██╔════╝██║████╗  ██║██╔══██╗██║     ██╗
   ██║   ██████╔╝██║   ██║█████╗      █████╗  ██║██╔██╗ ██║███████║██║     ╚═╝
   ██║   ██╔══██╗██║   ██║██╔══╝      ██╔══╝  ██║██║╚██╗██║██╔══██║██║     ██╗
   ██║   ██║  ██║╚██████╔╝███████╗    ██║     ██║██║ ╚████║██║  ██║███████╗╚═╝
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   
   
██████╗ ███████╗███████╗████████╗     █████╗ ██████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
██████╔╝█████╗  ███████╗   ██║       ███████║██████╔╝██║     ███████║█████╗  ██████╔╝
██╔══██╗██╔══╝  ╚════██║   ██║       ██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  ██╔══██╗
██████╔╝███████╗███████║   ██║       ██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║
╚═════╝ ╚══════╝╚══════╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

 ██████╗ ███████╗    ██╗  ██╗██╗███████╗████████╗ ██████╗ ██████╗ ██╗   ██╗
██╔═══██╗██╔════╝    ██║  ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
██║   ██║█████╗      ███████║██║███████╗   ██║   ██║   ██║██████╔╝ ╚████╔╝ 
██║   ██║██╔══╝      ██╔══██║██║╚════██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝  
╚██████╔╝██║         ██║  ██║██║███████║   ██║   ╚██████╔╝██║  ██║   ██║   
 ╚═════╝ ╚═╝         ╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
 
 Você, depois de concluir sua vingança,  com o arco de Scat, continua a identidade da mesma no meio mercenário, na verdade, você se eternizou no meio mercenário, com suas grandes flechas mais quentes que o fogo, você conseguiu eternizar a garota na história, como a predecessora do maior arqueiro de todo reino

  Você ainda tem saudades da mesma, e também é muito grato, esse era o mínimo a se fazer

  Mas mesmo assim, você nunca parou de tentar virar mais, você tinha que marcar ela ainda mais na história

  No final...

  Virar o maior arqueiro da história foi só consequência
""")
  system('clear')
  truefasttravel()
  
def funcgroup8():
  arrowfoot = input("""
  Tentar acertar apenas uma flecha certeira, prevendo o caminho perfeitamente e atirar


  Você consegue acertar o pé direito do Elfo, e logo ele diminui o ritmo e se esconde atras de uma arvore
  
  Apenas para você ver ele dando a volta na arvore para disparar em sua direção, parece que mesmo com um pé ferido ele continua...

  [1] Mirar no peito
  [2] Mirar no outro pé
  """)
  system('clear')

  if arrowfoot == '1':
   funcgroupdeath5()
  elif arrowfoot == '2':
    funcgroup9()
  else:
    funcgroup8()

def funcgroupdeath5():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   
      
Ele deflete sua flecha com sua espada e em um ultimo impulso, ele te estoca na barriga, te matando

  Aperte "enter" para jogar de novo
""")
  system('clear')
  func1()

def funcgroup9():
  input("""
  Você com um grande foco, mira no outro pé do Elfo e...
  """)
  system('clear')
  funcgroup10()

def funcgroup10():
  input("""
  Da certo! Parece que ele não esperava isso e logo cai na sua frente
  
  E para finalizar você puxa a corda e...


  o Elfo é morto com sua cabeça sendo perfurada por uma flecha

  Você logo se vira para ver Scat eliminado o Arqueiro também, ela também sua eliminação. Ela fica parada por um tempo, olhando para o cadáver de seu irmão...

  Ela logo volta a si, e vocês agora tem que eliminar o Orc
""")
  system('clear')
  orcbattle()

def orcbattle():
  distanciascat = input("""
  Logo um grande monstro é visto quebrando uma parede da casa e logo pulando perto de vocês, ele tinha uma grande lança

Era justamente o Orc

  Você fica intimidado pela presença do Orc, mas logo você volta ao normal e pensa em como derrota-lo como dupla

  [1] Se distanciar de Scat e tentar disparar flechas de varios lugares 
  [2] Ficar perto de Scat, tentando disparar flechas mais "focalizadas"
""")
  system('clear')
  if distanciascat == '1':
    orcbattle2()
  elif distanciascat == '2':
    orcbattledeath()
  else:
    orcbattle()

def orcbattledeath():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   
      
  Você acerta uma flecha nele e logo se junta á Scat, ele logo, rapidamente, se aproxima e te perfura
  
    Aperte "enter" para jogar de novo
""")
  system('clear')
  func1()

def orcbattle2():
  dodge_or_shoot = input("""
  Você logo se distancia do grande Orc e dispara uma flecha, que não faz literalmente nada á ele, mas pelo menos ele agora tinha duas opções para avançar
  
Ele avança em você, oque fazer?
  
  [1] Desviar
  [2] Disparar uma flecha antes""")
  system('clear')

  if dodge_or_shoot == '1':
    orcbattle3()
  elif dodge_or_shoot == '2':
    orcbattledeath2()
  else:
    orcbattle2()
    
def orcbattledeath2():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   
      
  Você acerta essa flecha, mas como a ultima, não fez nenhum dano nele, que logo te empala com sua lança
  
    Aperte "enter" para jogar de novo
""")
  system('clear')
  func1()

def orcbattle3():
  shoot_or_run = input("""
  Você logo desvia e faz distancia, ele volta sua atenção de novo para você, para logo uma flecha acertar seu braço, que agora perfura de forma funda

  Scat tinha acertado ele, e o mesmo percebeu que ela era uma maior ameaça que você e logo desiste de perseguir você para logo avançar nela


Você atira algumas flechas no Orc, que não sente nada, e continua sua caminhada em direção á garota

  Você estava apavorado, ele ficou de frente da garota, para logo joga-la ao chão para instantes depois, pegar ela pelo pescoço e ameaçar a matar na sua frente e te provocando a atirar
  
  [1] Atirar nele imediatamente
  [2] Puxar a corda mais para depois atirar
  [3] Fugir
  """)
  system('clear')

  if shoot_or_run == '1':
    orcbattledeath3()
  elif shoot_or_run == '2':
    orcbattle4()
  elif shoot_or_run == '3':
    orcbattledeath4()
  else:
    orcbattle3()

def orcbattledeath3():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   
 
Você não percebeu que era uma provocação!?


Com você atirando muito rapido, sua flecha saiu muito fraca, ele ri, e logo a mata. Você perde o mundo por um momento

E antes de você conseguir se recuperar,  ele tira a lança do peito da garota para logo lança-la em você

Você morre com seu peito sendo perfurado por uma lança

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def orcbattledeath4():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   

Que patético...

Ele vendo sua atuação, desiste momentaneamente de tentar matar a garota e utiliza sua lança para lança-la em você

Você morre com sua cabeça perfurada por uma lança

  Aperte "enter" para jogar de novo
""")

def orcbattle4():
  input("""
Ele ainda continua com aquele sorrisinho, e agora com a lança cada vez mais perto da barriga de Scat
  
Você vê a cara de pânico de  Scat, era uma cara de desespero total e de mais puro medo.

  E você puxa um pouco mais a corda, até chegar no limite fisico do arco, um brilho azul tempestade pode ser visto nos seus olhos
  
  E você atira sua flecha...
""")
  system('clear')
  orcbattle5()

def orcbattle5():
  input("""
  A velocidade estava comparada a de um relâmpago, e trazendo efeitos de tempestade no ambiente ao redor, sua flecha estava envolta de eletricidade

  Ele não consegue desviar, e no seu peito, é fincado uma flecha pulsando eletricidade, e por ter sido atacado, ele inconscientemente solta Scat, que logo se afasta
  
  Ele, com dificuldade, tira a flecha de seu peito e olha surpreso para você, para logo abrir um sorriso, ele logo avança em direção á você, mas agora, ele parecia estar mais estranho, estava saindo faíscas amarelas de seu corpo""")
  system('clear')
  orcbattle6()

def orcbattle6():
  input("""
  Ele logo avança em você muito rapidamente, para logo, você desviar igualmente rápido para atirar uma flecha no Orc que desvia e continua seus avanços

  O duelo estava MUITO rápido, tanto que Scat, que á esse ponto já não conseguia a acompanhar a batalha, mas mesmo assim, ela foca e prepara um disparo

  E a batalha continuava a milhão, com ele tentando te acertar, para você desviar e contra-atacar, para logo ele desviar, até que subitamente recua
  """)
  system('clear')
  orcbattle7()

def orcbattle7():
  input("""
  Ele logo começa a preparar uma estocada, mas isso á 5 metros de distancia já, você fica em alerta para logo, como um raio, ele apareceu em sua frente pronto para estocar

Você por pouco conseguiu se desviar para logo você disparar uma flecha elétrica na costela dele

A ferida dele o desacelerou e o feriu consideravelmente

E você, depois de disparar tantas vezes, é obrigado á dar um descano

  E agora, estavam vocês, um na frente do outro, sem poder fazer nada, em um momento onde você podia estar matando ele, você sofre isso, até que...
""")
  system('clear')
  orcbattle8()

def orcbattle8():
  input("""
  Uma forte flecha atinge a nuca do Orc, que caí no chão morto, a flecha foi disparada por Scat, que vendo a situação de ambos, viu uma grande oportunidade...

  
E vocês de novo se reencontram, ambos estavam suados e cansados, mas ambos estavam felizes e aliviados

Vocês tinham derrotado o Orc


E nesse clima mesmo, seus rostos lentamente se aproximam e vocês se beijam

E logo depois do beijo você desmaia, você havia usado muita energia, e ela te leva em seus braços para casa""")
  system('clear')
  orcbattle9()


def orcbattle9():
  input("""
  
████████╗██████╗ ██╗   ██╗███████╗    ███████╗██╗███╗   ██╗ █████╗ ██╗        
╚══██╔══╝██╔══██╗██║   ██║██╔════╝    ██╔════╝██║████╗  ██║██╔══██╗██║     ██╗
   ██║   ██████╔╝██║   ██║█████╗      █████╗  ██║██╔██╗ ██║███████║██║     ╚═╝
   ██║   ██╔══██╗██║   ██║██╔══╝      ██╔══╝  ██║██║╚██╗██║██╔══██║██║     ██╗
   ██║   ██║  ██║╚██████╔╝███████╗    ██║     ██║██║ ╚████║██║  ██║███████╗╚═╝
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   


██╗     ███████╗ ██████╗ ███████╗███╗   ██╗██████╗  █████╗ ██████╗ ██╗   ██╗
██║     ██╔════╝██╔════╝ ██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
██║     █████╗  ██║  ███╗█████╗  ██╔██╗ ██║██║  ██║███████║██████╔╝ ╚████╔╝ 
██║     ██╔══╝  ██║   ██║██╔══╝  ██║╚██╗██║██║  ██║██╔══██║██╔══██╗  ╚██╔╝  
███████╗███████╗╚██████╔╝███████╗██║ ╚████║██████╔╝██║  ██║██║  ██║   ██║   
╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   

 ██████╗ ██████╗ ██╗   ██╗██████╗ ██╗     ███████╗
██╔════╝██╔═══██╗██║   ██║██╔══██╗██║     ██╔════╝
██║     ██║   ██║██║   ██║██████╔╝██║     █████╗  
██║     ██║   ██║██║   ██║██╔═══╝ ██║     ██╔══╝  
╚██████╗╚██████╔╝╚██████╔╝██║     ███████╗███████╗
 ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝╚══════╝

                                                                                    
  Vocês, depois de matarem o Orc, oficializam o namoro e começam a viver junto em uma casa na floresta

  Vocês dois trabalham como mercenários / caçadores de recompensa, e nessa profissão, vocês ficam mundialmente conhecidos por suas incríveis habilidades, Scat por seu domínio do arco, e você pela "Flecha Relâmpago", técnica que você conseguiu aprimorar depois da luta contra o Orc

  Vocês como mercenários, derrotaram vários oponentes como: guerreiros reais, Quimeras, Minotauro, Demônios, Anjos, Espadachins Lendários e até mesmo um Dragão

  E depois de derrotarem o dragão, você propõe ela em casamento, que aceita chorando de alegria, vocês vivem casados na casa na floresta, agora muito mais confortável, pois com a reputação mortal, também vem dinheiro

  No final, seus nomes ficaram gravados na história dos mercenários e da humanidade em geral, como os únicos humanos á derrotarem um Dragão, seus feitos viraram histórias para gerações, o "Casal Lendário do Arco e Flecha" é como te chamam
  """)
  system('clear')
  # conquista.append(Legendary)
  truefasttravel()
1

def conquistas():
  print(conquistaappend)
  achivement = input('\n [1] Voltar')
  system('clear')

  if achivement == '1':
     func1()
  else:
    conquistas()

  # def verificar_conquista(conquista, pontuacao):
  #   if conquista in conquistas and pontuacao == conquistas[conquista]:
  #       return conquista
  #   else:
  #       return None

  # def conquistas(pontuacao):
  #     print("Conquistas alcançadas:")
  #     for conquista in conquistas:
  #         if verificar_conquista(conquista,pontuacao):
  # print("- " + conquista)
  


def fasttravelbrabo():
  input("""
  Parabens, você desbloqueou o Fast Travel!
  """)
  system('clear')
  fasttravel == True
  func1()

def truefasttravel():
  input("""Parabens! Você conseguiu completar um "True Final", ou, "Final Verdadeiro", e de recompensa, disponibilizo para você o "True Fast Travel", uma versão melhorada do Fast Travel, para você conseguir outros finais, tanto os "True Finals", quanto os outros finais """)
  system('clear')
  truetravel == True
  func1()
  
def fastravel():
  if fasttravel == True and truetravel == False:
    fast = input("""
    Fast Travels Disponiveis:

    [1] Aldeia - "Você acorda, mas não vê nenhum rastro"
    [2] Acampamento - "Oquê fazer?"
    [3] Elfa - "Contar ou não contar?"
    [0] Voltar
    """)
    system('clear')
    
    if fast == '1':
      func38()
    elif fast == '2':
      func27()
    elif fast == '3':
      func46()
    elif fast == '0':
      func1()
    else:
      fastravel()
  elif fasttravel == False and truetravel == False:
    naofast = input("""
    Você ainda não tem acesso ao Fast Travel
    
    [1] Voltar""")
    system('clear')
    
    if naofast == '1':
      func1()
    else:
      fasttravel()
  elif fastravel == True:
    true = input("""
    Fast Travels Disponiveis:

    [1] Aldeia - "Você acorda, mas não vê nenhum rastro"
    [2] Acampamento - "Oquê fazer?"
    [3] Elfa - "Contar ou não contar?"
    [4] Grupo/Elfo - "Atacar primeiro ou desistir da posição?"
    [5] Grupo/Dupla - "Cuidar do elfo ou do Arqueiro?"
    [0] Voltar""")
    system('clear')


    if true == '1':
      func38()
    elif true == '2':
      func27()
    elif true == '3':
      func46()
    elif true == '4':
      funcgroup1()
    elif true == '5':
      funcgroup2()
    elif true == '0':
      func1()
    else:
      fastravel()
  else:
    pass
    
  
def creditos():
  creditos = input("""
  Progamador Principal: Guilherme Ferrarezi
  Progamador Auxiliar: Henrique Bussi
  
  Escritor Principal: Henrique Bussi

  Grupo(IDEV2): Guilherme Ferrarezi, Henrique Bussi, Carol e Camille
  
  Menções Honrosas para Juan Miguel, que tambem escreveu o caminho da cidade
  
  [1] Mais Creditos
  [2] Voltar
  """)
  system('clear')

  if creditos == '2':
    func1()
  elif creditos == '1':
    creditosexpandidos()
  else:
    creditos()

def creditosexpandidos():
  creditos2 = input("""
  Rota da Cidade:
  
  Programador: Guilherme Ferrarezi
  Escritor: Juan Miguel
  Extra: Henrique Bussi

  
  Rota da Floresta(Começo):
  
  Programador: Guilherme Ferrarezi
  Escritor: Henrique Bussi


  Rota da Floresta(Sozinho):
  
  Programador: Guilherme Ferrarezi
  Escritor: Henrique Bussi


  Rota da Floresta(Grupo):
  
  Programador: Henrique Bussi
  Escritor: Henrique Bussi

  Menu:
  
  Programador: Henrique Bussi

  (Inclusive é eu que estou escrevendo isso agr, xd)


  [1] Voltar para os créditos
  [2] Voltar para menu
  """)
  system('clear')

  if creditos2 == '1':
    creditos()
  elif creditos2 == '2':
    func1()
  else:
    creditos2()


def func107():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

      
  No final, ela ganha, e nos seus últimos momentos ela agradece pelo duelo, falando que foi um dos melhores que ela já teve, e ainda fala que você é gatinho, para logo inserir uma de suas   adagas em você.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func108():
  print("""
  No final, você ganha, cortando rapidamente a cabeça da linda mulher
  """)
  func106()

def func109():
  silenciosamente_certo_ou_nao = random.choice([5, 0])

  if silenciosamente_certo_ou_nao == '1':
    input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

      
    Você corre e tenta cortar a cabeça do Orc silenciosamente, apenas para o Orc desviar e te matar  com sua marreta.

    Aperte "enter" para jogar de novo
    """)
    system('clear')
    func1()
  else:
    input("""
██████  ███████ ██████  ███████ ███████  ██████ ████████     
██   ██ ██      ██   ██ ██      ██      ██         ██        
██████  █████   ██████  █████   █████   ██         ██        
██      ██      ██   ██ ██      ██      ██         ██        
██      ███████ ██   ██ ██      ███████  ██████    ██    

██ ███    ██ ███████ ██ ██   ████████ ██████   █████  ████████ ██  ██████  ███    ██     
██ ████   ██ ██      ██ ██      ██    ██   ██ ██   ██    ██    ██ ██    ██ ████   ██     
██ ██ ██  ██ █████   ██ ██      ██    ██████  ███████    ██    ██ ██    ██ ██ ██  ██     
██ ██  ██ ██ ██      ██ ██      ██    ██   ██ ██   ██    ██    ██ ██    ██ ██  ██ ██     
██ ██   ████ ██      ██ ███████ ██    ██   ██ ██   ██    ██    ██  ██████  ██   ████     

███████ ██ ███    ██  █████  ██      
██      ██ ████   ██ ██   ██ ██      
█████   ██ ██ ██  ██ ███████ ██      
██      ██ ██  ██ ██ ██   ██ ██      
██      ██ ██   ████ ██   ██ ███████ 


  Você consegue o matar e sai de lá silenciosamente, sem nenhuma ferida e sem nenhuma alarde. Você faz um churrasco com a Elfa e a convida para viver com você na cidade, ela aceita, e   vocês voltam para a cidade, onde você, junto da Elfa, trabalham com seu mestre. Depois de um tempo, você e ela abrem sua própria escola de esgrima e arquearia.

  Aperte "enter" para jogar de novo
    """)


def func110():
  orc_silencioso_ou_n_matar = input("""
    Você segue silenciosamente, rente a parede, até chegar em uma janela próxima, que você pula para entrar na casa. E depois de olhar um pouco o primeiro andar, você não acha ninguém, então você segue para o segundo andar. Você segue para o segundo andar e logo se depara com uma grande porta, diferente das outras, além disso,  você consegue ouvir uma grave  vindo daquele quarto. Com certeza o Orc estava ali.

    O que você faz?

    Digite [1] para ir para o combate
    Digite [2] para tentar matar silenciosamente
    """)
  system('clear')

  if orc_silencioso_ou_n_matar == '1':
    func92()
  elif orc_silencioso_ou_n_matar == '2':
    func109()
  else:
    func110()

def func111():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

      
  Você tenta matar ele furtivamente, mas ele logo percebe e antes que você pudesse mata-lo. Ele te da uma martelada na sua perna que quebra um osso. Com sua mobilidade reduzida, o Anão toma vantagem e te mata com uma martelada na cabeça

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func112():
  morrer_ou_nao2 = random.choice([5,0])

  if morrer_ou_nao2 % 2 == 0:
    input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   


    Você mata um, mas o outro te mata logo em seguida.

    Aperte "enter" para jogar de novo
    """)
    system('clear')
    func1()
  else:
    print("""
    Você consegue matar os dois com apenas uma estocada, perfurando a cabeça dos dois em apenas um movimento. Logo você entra na casa pela porta principal.
    """)
    func110()

def func113():
  plano = input("""
  Você rapidamente se aproxima do Orc, ele parece surpreso com sua velocidade, qual é o plano?

  Digite [1] para Estocar mirando seu coração
  Digite [2] para Cortar a cabeça dele
  """)
  system('clear')

  if plano == '1':
    func115()
  elif plano == '2':
    func116()
  else:
    func113()

def func114():
  desvio_ou_n = input("""
  Naquele momento, você percebeu que ele, por mais que seja enorme, ainda era bem rápido, e na sua frente, você vê o grande Orc segurando uma enorme marreta em uma só mão e a momentos de te atacar. 

  Digite [1] para tentar desviar
  Digite [2] para tentar atacar antes
  """)
  system('clear')

  if desvio_ou_n == '1':
    func116()
  elif desvio_ou_n == '2':
    func117()
  else: 
    func114()

def func115():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

    Você inicialmente estava prestes a realizar seu plano, você tinha pulado e estava a centímetros do peito do Orc. Quando de repente ele desvia, e ainda no ar, você é atingindo por uma marretada no peito que te mata

    Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func116():
  tatico = input("""
  Você Logo se afasta, você precisava pensar rápido no que fazer, você não tinha progredido nada.

  Digite [1] para continuar da mesma forma
  Digite [2] para Ser mais rápido
  Digite [3] para Ser mais tático
  """)
  system('clear')

  if tatico == '1':
    func118()
  elif tatico == '2':
    func119()
  elif tatico == '3':
    func120()
  else:
    func116()

def func117():
  input("""
  ██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

      
  Você consegue o atacar, mas, diferentemente do que você pensava, isso não parou o ataque em primeiro lugar. Você morre com uma enorme marretada na cabeça enquanto o Orc continua vivo, mesmo que ferido.

  Aperte "enter" para jogar de novo 
  """)
  system('clear')
  func1()

def func118():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     


    Ele logo avança com sua enorme marreta, você tenta manter um equilíbrio de velocidade e estabilidade, mas, você percebe algo. Você não era tão melhor que seu adversário
    Ele também era Rápido. Ele também tinha habilidade. E ele era mais forte. E por essa diferença de força, você acabou perdendo essa disputa, e acabou perdendo a vida.

    Aperte "enter" para jogar de novo 
  """)
  system('clear')
  func1()

def func119():
  cortar = input("""
  Ele avança com sua marreta, e agora com sua escolha, você avança em direção a ele com maior velocidade fazendo um rastro de poeira. E quando ele vai atacar você, seu olho de repente brilha azul relâmpago...
  Você consegue rapidamente fazer vários cortes partes diferentes do Orc, e ainda aparece atras do mesmo. Ele olha ao redor e percebe oque você fez e fica surpreso, mas de repente um grande sorriso é encontrado em sua cara.
  Ele estava animado que alguém poderia o ferir daquele jeito. Ele logo pega sua marreta e a modifica com... magia? Sua marreta logo aparece maior, a cabeça dela parecia estar queimando e com detalhes vermelhos. Os dois lados tinham aumentado de nivel. E em um grande "Azul contra Vermelho", a batalha se reinicia. Você avança em grande velocidade com usa espada incrível em direção ao grande Orc, sua espada estava emitindo faíscas, parece que você evoluiu durante a luta. Em uma grande velocidade, você já chega há poucos metros do Orc. 

  Digite [1] para Tentar cortar a cabeça dele em alta velocidade
  Digite [2] para Tentar estocar seu peito em grande velocidade
  """)
  system('clear')

  if cortar == '1':
    func121()
  elif cortar == '2':
    func122()
  else:
    func119()


def func120():
  ser_mais_tatico = input("""
  Ele avança com sua enorme marreta, e agora com sua mudança, você se estabiliza no chão e apenas espera. Agora você iria usar sua habilidade de espada ao máximo. E quando ele vai atacar você, seu olho de repente brilha vermelho fogo...
  Você consegue cortar a marreta momentos antes dela te esmagar, na verdade, aparece um grande corte no peito do mesmo. Ele olha para sua marreta, e logo olha para seu peito e fica surpreso, mas de repente um grande sorriso é encontrado em sua cara.
  Ele estava animado que alguém poderia o ferir daquele jeito. Ele logo arremessa para longe o resto de sua marreta e logo se encorpa e aparece detalhes azuis em sua pele, de suas feridas sai fumaça, ele parecia... maior. Os dois lados tinham aumentado de nivel. E em um grande "Vermelho contra Azul", a batalha se reinicia. Ele avança em direção a você amassando o chão enquanto anda, mostrando o quão forte ele agora estava, parece que ele evoluiu durante a luta. Você continua parado esperando ele chegar mais perto. 
  Você espera, espera, E...

  Digite [1] para Tentar Defletir o soco
  Digite [2] para Tentar Esquivar do soco
  """)
  system('clear')

  if ser_mais_tatico == '1':
    func125()
  elif ser_mais_tatico == '2':
    func126()
  else: 
    func120()


def func121():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     


  Ele com sua mais nova marreta evoluída te joga ainda no ar para o chão. para logo te matar esmagando sua cabeça.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()
  

def func122():
  antes = input("""
  Você fica perto de ataca-lo na barriga, apenas para Orc tentar te atacar com sua marreta, você, por estar mais distante, consegue desviar. Depois de desviar do ataque do Orc, você consegue, rapidamente, dar uma estocada na costela, o ferindo gravemente. Você tira sua espada. da costela do Orc, e vê um grande buraco cheio de sangue. Ele parecia muito mais furioso do que antes, e logo depois de você recuar, ele avança em você com sua marreta brilhando cor vermelha. Você se prepara, entrando e posição com sua espada de relâmpagos contra o Orc.

  Digite [1] para desviar 
  Digite [2] para atacar antes 
  """)
  system('clear')

  if antes == '1':
    func123()
  elif antes == '2':
    func124()
  else:
    func122()

def func123():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     


  Ele já aprendeu como você desvia. E sabendo disso ele ataca, mas não termina o ataque na primeira tentativa, e sim continua o ataque. Te matando esmagado.

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()
  
def func124():
  input("""
████████ ██████  ██    ██ ███████     
   ██    ██   ██ ██    ██ ██          
   ██    ██████  ██    ██ █████       
   ██    ██   ██ ██    ██ ██          
   ██    ██   ██  ██████  ███████     

███████ ██ ███    ██  █████  ██      
██      ██ ████   ██ ██   ██ ██      
█████   ██ ██ ██  ██ ███████ ██      
██      ██ ██  ██ ██ ██   ██ ██      
██      ██ ██   ████ ██   ██ ███████ 

██      ██  ██████  ██   ██ ████████ ███    ██ ██ ███    ██  ██████      
██      ██ ██       ██   ██    ██    ████   ██ ██ ████   ██ ██           
██      ██ ██   ███ ███████    ██    ██ ██  ██ ██ ██ ██  ██ ██   ███     
██      ██ ██    ██ ██   ██    ██    ██  ██ ██ ██ ██  ██ ██ ██    ██     
███████ ██  ██████  ██   ██    ██    ██   ████ ██ ██   ████  ██████      

██████  ██       █████  ██████  ███████ 
██   ██ ██      ██   ██ ██   ██ ██      
██████  ██      ███████ ██   ██ █████   
██   ██ ██      ██   ██ ██   ██ ██      
██████  ███████ ██   ██ ██████  ███████ 
                                    
  Com sua velocidade e emitindo faíscas, você corta o peito do Orc para logo mudar de posição e fazer cortes nas pernas e nas costas, deslizando, deixando faíscas no caminho, para que quase como um teleporte, você também aparece de novo na frente do Orc, assustado com tamanha velocidade. E em uma velocidade comparada a um trovão, você corta a cabeça do Orc.

  Parabéns, você conseguiu. 
  Você finalmente conseguiu sua vingança, e logo depois de um pequeno churrasco com sua amiga Elfa, você volta para a cidade e reencontra seu mestre, que te recepciona felizmente, e você,   com sua mais nova habilidade de velocidade, vira o melhor espadachim reino, sendo conhecido como o "Relâmpago que corta", ou simplesmente: 

  "O Relâmpago Cortante"

  Aperte "enter" para jogar de novo 
  """)
  system('clear')
  func1()

def func125():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░     

      
  Você não conseguiria defletir ele nem normalmente, imagina com ele assim... Ele quebra sua espada e no caminho, da um soco que te mata de primeira
  
  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func126():
  desviar_lateral = input("""
  Você consegue desviar lateralmente. Depois de cancelar o ataque de seu adversário, ele baixa a guarda, se tornando um alvo fácil para sua espada que saia fumaça, que corta  boa parte da lateral do Orc, e esse corte, diferente do esperado por ele, era um corte relativamente fundo. Ele fica mais puto ainda, e de suas feridas, mais fumaça sai ainda. Ele grita alto e vai para cima de você, mas agora com muito mais velocidade do que antes.

  O que você faz?

  Digite [1] para atacar antes
  Digite [2] para desviar dele 
  """)
  system('clear')

  if desviar_lateral == '1':
    func127()
  elif desviar_lateral == '2':
    func128()
  else:
    func126()

def func127():
  input("""
██▒   █▓ ▒█████   ▄████▄  ▓█████     ███▄ ▄███▓ ▒█████   ██▀███   ██▀███  ▓█████  █    ██ 
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██  ▓██▒
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▒██░
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓▓█  ░██░
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒▒█████▓ 
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░   ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░░▒░ ░ ░ 
     ░░  ░ ░ ░ ▒  ░           ░      ░      ░   ░ ░ ░ ▒    ░░   ░   ░░   ░    ░    ░░░ ░ ░ 
      ░      ░ ░  ░ ░         ░  ░          ░       ░ ░     ░        ░        ░  ░   ░   


  Ele estava muito mais rápido que o normal, e quando você ainda estava pensando em como ataca-lo, ele aparece na sua frente e te soca com grande força, que te mata.
  
  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()

def func128():
  input("""
████████ ██████  ██    ██ ███████     
   ██    ██   ██ ██    ██ ██          
   ██    ██████  ██    ██ █████       
   ██    ██   ██ ██    ██ ██          
   ██    ██   ██  ██████  ███████   

███████ ██ ███    ██  █████  ██      
██      ██ ████   ██ ██   ██ ██      
█████   ██ ██ ██  ██ ███████ ██      
██      ██ ██  ██ ██ ██   ██ ██      
██      ██ ██   ████ ██   ██ ███████ 

███████ ██       █████  ███    ███ ███████     
██      ██      ██   ██ ████  ████ ██          
█████   ██      ███████ ██ ████ ██ █████       
██      ██      ██   ██ ██  ██  ██ ██          
██      ███████ ██   ██ ██      ██ ███████    

███████ ██     ██  ██████  ██████  ██████  
██      ██     ██ ██    ██ ██   ██ ██   ██ 
███████ ██  █  ██ ██    ██ ██████  ██   ██ 
     ██ ██ ███ ██ ██    ██ ██   ██ ██   ██ 
███████  ███ ███   ██████  ██   ██ ██████  


  Depois de desviar de um soco, você logo tem, que desviar de mais um, e mais um, e quando o Orc pareceu estar se recuperando do cansaço, você, com seus olhos brilhando vermelho e sua espada pegando fogo, enfia precisamente sua espada no coração do Orc. Você tira sua espada e vê o sangue na sua espada, e enquanto o Orc estava caindo pois... seu coração havia sido perfurado, você o decapita. 
  
  Parabéns, você conseguiu. 
  Você finalmente conseguiu sua vingança, e logo depois de um pequeno churrasco com sua amiga Elfa, você volta para a cidade e reencontra seu mestre, que te recepciona felizmente, e você, com sua mais nova habilidade de precisão e desvio, vira o melhor espadachim reino, sendo conhecido como o "A erupção de um vulcão em apenas um golpe", ou simplesmente:"O Incêndio Focalizado"

  Aperte "enter" para jogar de novo
  """)
  system('clear')
  func1()


func1()