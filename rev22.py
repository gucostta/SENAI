"""
22. O cardápio de uma lanchonete é o seguinte:
Especificação Código Preço
Cachorro Quente 100 R$ 1,20
Bauru Simples 101 R$ 1,30
Bauru com ovo 102 R$ 1,50
Hambúrguer 103 R$ 1,20
Cheeseburguer 104 R$ 1,30
Refrigerante 105 R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do
pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

# Definir o cardápio como um dicionário onde as chaves são os códigos e os valores são listas [item, preço]
cardapio = {
    100: ["Cachorro Quente", 1.20],
    101: ["Bauru Simples", 1.30],
    102: ["Bauru com Ovo", 1.50],
    103: ["Hambúrguer", 1.20],
    104: ["Cheeseburguer", 1.30],
    105: ["Refrigerante", 1.00]
}

# Inicializar variáveis para o total do pedido
total_pedido = 0

# Ler os pedidos até que o cliente deseje encerrar
while True:
    # Solicitar ao cliente que informe o código do item e a quantidade desejada
    codigo = int(input("Digite o código do item (-1 para encerrar o pedido): "))
    
    # Verificar se o cliente deseja encerrar o pedido
    if codigo == -1:
        break
    
    # Verificar se o código do item é válido
    if codigo in cardapio:
        quantidade = int(input("Digite a quantidade desejada: "))
        item, preco = cardapio[codigo]
        
        # Calcular o valor a ser pago pelo item e atualizar o total do pedido
        valor_item = preco * quantidade
        total_pedido += valor_item
        
        # Exibir o valor a ser pago pelo item
        print(f"Item: {item}, Quantidade: {quantidade}, Valor a ser pago: R$ {valor_item:.2f}")
    else:
        print("Código inválido. Por favor, digite um código válido.")

# Exibir o total geral do pedido
print(f"Total do pedido: R$ {total_pedido:.2f}")
