import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para atualizar o gráfico com base nos dados inseridos pelo usuário
def atualizar_grafico():
    notas_usuario = []
    
    for entry in entries:
        nota_texto = entry.get()
        
        # Verificar se a entrada é válida
        if nota_texto.strip():  # Verificar se a string não está vazia
            nota = int(nota_texto)
            notas_usuario.append(nota)
        else:
            # Tratar caso a entrada seja vazia
            notas_usuario.append(0)

    x = list(range(1, 9))
    y = notas_usuario

    # Limpar o conteúdo antigo do gráfico
    for widget in frame_grafico.winfo_children():
        widget.destroy()

    # Criar e exibir o novo gráfico
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_title('Notas de Matemática')
    ax.set_xlabel('Provas')
    ax.set_ylabel('Notas')

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Criar a janela principal
root = tk.Tk()
root.title("Visualização de Notas")

# Entradas para as notas
entries = []
for i in range(8):
    label = tk.Label(root, text=f"Nota Prova {i+1}:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

# Botão para atualizar o gráfico
btn_atualizar = tk.Button(root, text="Atualizar Gráfico", command=atualizar_grafico)
btn_atualizar.pack(pady=10)

# Frame para o gráfico
frame_grafico = tk.Frame(root)
frame_grafico.pack()

# Inicializar o gráfico
atualizar_grafico()

# Iniciar o loop principal da interface gráfica
root.mainloop()
