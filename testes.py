import tkinter as tk

def mostrar_mensagem():
    produto = entry_produto.get()
    quantidade = entry_quantidade.get()
    # Lógica do seu sistema de vendas aqui
    mensagem = f"Venda registrada: Produto - {produto}, Quantidade - {quantidade}"
    label_resultado.config(text=mensagem)

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Vendas")

# Componentes da interface
label_produto = tk.Label(root, text="Produto:")
entry_produto = tk.Entry(root)

label_quantidade = tk.Label(root, text="Quantidade:")
entry_quantidade = tk.Entry(root)

botao_vender = tk.Button(root, text="Registrar Venda", command=mostrar_mensagem)
label_resultado = tk.Label(root, text="")

# Layout da interface
label_produto.grid(row=0, column=0)
entry_produto.grid(row=0, column=1)

label_quantidade.grid(row=1, column=0)
entry_quantidade.grid(row=1, column=1)

botao_vender.grid(row=2, column=0, columnspan=2)
label_resultado.grid(row=3, column=0, columnspan=2)

# Iniciar o loop de eventos
root.mainloop()
