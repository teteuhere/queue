import queue

# Função para enfileirar letras em A e números em B
def enqueue_letters_and_numbers(queue_a, queue_b, value):
    if value.isalpha():
        queue_a.put(value)
    elif value.isdigit():
        queue_b.put(int(value))
    else:
        print("Valor inválido. Digite uma letra ou número.")

# Função para imprimir os valores de B seguidos pelos valores de A
def print_b_and_a(queue_b, queue_a):
    print("Valores de B:")
    while not queue_b.empty():
        value = queue_b.get()
        print(value)

    print("Valores de A:")
    while not queue_a.empty():
        value = queue_a.get()
        print(value)

def main():
    queue_a = queue.Queue()
    queue_b = queue.Queue()

    while True:
        print("1. Enfileirar letra em A e número em B")
        print("2. Imprimir Valores de B seguidos pelos de A")
        print("3. Encerrar")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            value = input("Digite uma letra ou número: ")
            enqueue_letters_and_numbers(queue_a, queue_b, value)
        elif choice == "2":
            print_b_and_a(queue_b, queue_a)
        elif choice == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
