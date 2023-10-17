def notas(*notas, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['média'] = sum(notas)/len(notas)
    
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    
    return r

# Solicitando ao usuário para inserir as notas
notas_alunos = [float(nota) for nota in input("Digite as notas dos alunos separadas por espaço: ").split()]
# Solicitando ao usuário para inserir a situação
sit_alunos = input("Deseja calcular a situação (s/n)? ").lower() == 's'

# Chamada da função com os parâmetros fornecidos pelo usuário
resp = notas(*notas_alunos, sit=sit_alunos)
print(resp)
