def leiaInt():
    # Função que irá ler um número inteiro. Irá resultar em uma mensagem de erro, caso o valor digitado seja igual ou menor que 0 ou não seja um número.
    while True:
        try:
            num = int(input('Sua opção: '))
        except:
            print('ERRO! Por favor digite uma opção válida')
            print('-' * 50)
        else:
            if num <= 0 or num > 2:
                print('ERRO! Por favor digite uma opção válida')
                print('-' * 50)
            else:
                return num


def climaLocal():
    # Função principal
    # Importação da biblioteca requests, e a deep translator(que será usada para tradução).
    import requests
    from deep_translator import GoogleTranslator
    # Diciónario que será usado para guandar as informações do tempo.
    info = {}
    api_key = 'be6876afdb1a13c0782837ced4927809'
    # Utilizando a função de tradução para traduzir do inglês para o português
    tradutor = GoogleTranslator(source='en', target='pt')
    print('-' * 50)
    # Variável que irá receber o local digitado.
    local = str(
        input('Qual localização desejar cosultar o clima? ').strip().upper())
    # Requisitando as informações do clima de uma API.
    requisicao = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={local}&appid={api_key}')
    # Transformador ela em um diciónario
    requisicao_dic = requisicao.json()
    # Salvando todas as informações em um dicionário
    try:
        info['Temperatura'] = round(requisicao_dic['main']['temp'] - 273.15)
        info['Sensação Térmica'] = round(
            requisicao_dic['main']['feels_like'] - 273.15)
        info['Umidade'] = requisicao_dic['main']['humidity']
        info['Condição do Tempo'] = tradutor.translate(
            requisicao_dic['weather'][0]['description'])
    except:
        # Caso o local não exista ou não seja encontrado, irá ser exibido uma mensagem de erro.
        print('ERRO! LOCAL NÃO ENCONTRADO')
    else:
        # Apresentação de todas as informações.
        print('-' * 50)
        print(f'CLIMA ATUAL DE {local}'.center(50))
        print('-' * 50)
        for c, v in info.items():
            if c in 'Condição do Tempo':
                print(f'{c}: {v.title()}')
            elif c in 'Umidade':
                print(f'{c}: {v}%')
            else:
                print(f'{c}: {v}°C')


def menu():
    # Menu
    import clima
    opcoes = ['Consultar clima', 'Sair']
    while True:
        print('-' * 50)
        print('ClimaPy'.center(50))
        print('-' * 50)
        for i, op in enumerate(opcoes):
            print(f'{i + 1}. {op}')
        print('-' * 50)
        # Chamando a função que ler um número inteiro.
        res = clima.leiaInt()
        if res == 1:
            # Chamando a função principal do sistema.
            clima.climaLocal()
        elif res == 2:
            print('-' * 50)
            print('OBRIGADO POR USAR O CLIMAPY'.center(50))
            print('-' * 50)
            break
