pontos = 0
print ("=== QUIZ DE CONSCIENTIZAÇÃO EM SEGURANÇA ===")
resposta1 = input ("""Você recebeu um e-mail da diretoria pedindo para clicar em um link urgente de troca de senha. O que você faz?
a) Clicar
b) Reportar ao time de TI
c) Só ignorar o e-mail 
Reposta: """).strip().lower()
if resposta1 == "b":
    print("Acertou!")
    pontos = pontos + 1 #Ganha 1 ponto
else:
    print ("Errou!")

resposta2 = input ("""Você encontra um pendrive perdido no estacionamento ou na recepção da empresa. O que faz?
a) Conectar no computador para ver de quem é
b) Deixar onde está
c) Entregar no setor de TI ou Segurança 
Resposta: """).strip().lower()

if resposta2 == "c":
    print("Acertou!")
    pontos = pontos + 1 #Ganha 1 ponto
else: 
    print ("Errou!")

resposta3 = input ("""Um colega do seu setor pede sua senha do sistema para fechar um relatório urgente enquanto você está no almoço. Você? 
a) Nega o acesso e avisa que senhas são pessoais e intransferíveis
b) Passa a senha, afinal é sua colega de equipe
c) Anota em um papel e deixa na mesa dela 
Resposta: """).strip().lower()
if resposta3 == "a":
    print ("Acertou!")
    pontos = pontos + 1 #Ganha 1 ponto
else:
    print ("Errou!")

print ("=== FIM DO QUIZ! ===")
print (f"Você acertou {pontos} de 3 perguntas")
if pontos == 3:
    print ("Arrasou! Gabaritou!")
elif pontos == 2:
    print ("Tá tudo bem, errar faz parte...")
else:
    print ("Hmm... melhor tentar novamente, não?")
