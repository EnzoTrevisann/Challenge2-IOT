import openai

# OPENAI API KEY
openai.api_key = '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'

# função que envia uma solicitação a API e recebe a resposta
def enviar_solicitacao(texto):
    resposta = openai.Completion.create(
        engine='text-davinci-003', # mecanismo de geração de texto a ser usado.
        prompt=texto,  # representa a pergunta/frase que você deseja usar para solicitar uma resposta do modelo.
        max_tokens=120,  # número máximo de caracteres
        n=1,  # número de respostas geradas.
        stop=None, # especifica um token de parada personalizado para interromper a geração do texto.
        temperature=0.7  # controla a aleatoriedade das respostas geradas.
    )
    return resposta.choices[0].text.strip()


# variável para controlar se é a primeira pergunta
primeira_pergunta = True

# loop principal do chatbot
while True:
    if primeira_pergunta:
        entrada = input("Usuário: ")
        primeira_pergunta = False
    else:
        entrada = input("Te ajudo em algo mais? ")

        if entrada.lower() == 'não' or entrada.lower() == 'nao':
            print(
                "Certo, se você tiver mais alguma dúvida, fique à vontade para perguntar.")
            break

    if entrada.lower() == 'sair':
        break

    resposta = enviar_solicitacao(entrada)
    print("Plusoft Chatbot: " + resposta)
