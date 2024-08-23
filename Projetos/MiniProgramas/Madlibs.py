#Concatenação de Strings
#Criar uma String que seja "Se increva no canal do _____"
# nomeDoCanal = "" #Nome do canal

# print("Se inscreva no canal do " + nomeDoCanal)
# print("Se inscreva no canal do {}".format(nomeDoCanal))
# print(f"Se inscreva no canal do {nomeDoCanal}")

adj = input("Adjetivo: ")
verbo1 = input("Verbo 1: ")
verbo2 = input("Verbo 2: ")
pessoa_famosa = input("Nome: ")

madlib = f"Programação de Computadores é tão {adj}! Me deixa tão entusiasmado todo o tempo porque \
eu amo {verbo1}. Fique hidratado e {verbo2} como se você fosse {pessoa_famosa}!"

print(madlib)