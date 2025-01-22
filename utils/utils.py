import csv


def ler_csv(arquivo_csv):
    dados_csv = []

    try:
        with open(arquivo_csv, 'r', newline='', encoding='utf-8') as massa:
            tabela = csv.reader(massa, delimiter=';')
            next(tabela)
            for linha in tabela:
                dados_csv.append(linha)
                print(linha)
                print('AAAA')
        return dados_csv
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {arquivo_csv}")
    except Exception as fail:
        print(f"Erro ao ler o arquivo: {fail}")