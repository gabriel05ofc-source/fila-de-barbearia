from collections import deque


servicos = {
    1: ("Corte de Cabelo", 30.0),
    2: ("Barba", 20.0),
    3: ("Sobrancelha", 10.0),
    4: ("Pigmentação", 25.0)
}


fila = deque()

clientes_atendidos = 0
qtd_servicos = 0
valor_faturado = 0

while True:
    print("\n=== BARBEARIA ===")
    print("1 - Adicionar cliente")
    print("2 - Atender próximo cliente")
    print("3 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")

        servicos_cliente = []

        while True:
            print("\nServiços disponíveis:")
            for codigo, (nome_servico, preco) in servicos.items():
                print(f"{codigo} - {nome_servico} (R$ {preco:.2f})")

            escolha = int(input("Escolha um serviço: "))

            if escolha in servicos:
                servicos_cliente.append(escolha)

            continuar = input("Adicionar outro serviço? (s/n): ").lower()
            if continuar != "s":
                break

        fila.append((nome, servicos_cliente))
        print(f"\nCliente {nome} adicionado à fila!")

    elif opcao == "2":
        if not fila:
            print("\nNenhum cliente na fila.")
        else:
            nome, servicos_cliente = fila.popleft()

            total_cliente = 0

            print(f"\nAtendendo: {nome}")
            print("Serviços:")

            for codigo in servicos_cliente:
                nome_servico, preco = servicos[codigo]
                print(f"- {nome_servico}: R$ {preco:.2f}")
                total_cliente += preco
                qtd_servicos += 1

            print(f"Total do cliente: R$ {total_cliente:.2f}")

            clientes_atendidos += 1
            valor_faturado += total_cliente

    elif opcao == "3":
        print("\n=== RELATÓRIO FINAL ===")
        print(f"Clientes atendidos: {clientes_atendidos}")
        print(f"Quantidade de serviços realizados: {qtd_servicos}")
        print(f"Valor faturado: R$ {valor_faturado:.2f}")
        break

    else:
        print("Opção inválida!")