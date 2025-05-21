# Programa para registrar notas de uma turma
notas = []
print("Registro de Notas da Turma")
print("Digite 'fim' para terminar e calcular a média")

while True:
    entrada = input("Digite uma nota (0 a 10): ")
    
    if entrada.lower() == 'fim':
        break  # Sai do loop quando digitar 'fim'
    
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
            print(f"Nota {nota} adicionada.")
        else:
            print("Nota inválida! Deve ser entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia da turma: {media:.2f}")
    print(f"Total de notas registradas: {len(notas)}")
else:
    print("Nenhuma nota válida foi registrada.")