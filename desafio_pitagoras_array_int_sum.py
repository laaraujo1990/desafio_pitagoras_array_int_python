# Teste tecnico pitagoras - Leonardo Araujo
#

t = int(input("Informe a quantidade de numeros: "))
i = 0
vet = [] 
while i < t:
    n = int(input("Informe o numero: "))
    vet.append(n)
    i += 1
maior = max(vet)
menor = min(vet)
total_maior = sum(vet) - menor
total_menor = sum(vet) - maior
print(total_menor, total_maior)
