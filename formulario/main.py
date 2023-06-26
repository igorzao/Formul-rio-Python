import tkinter as tk
from tkinter import ttk
import csv


def salvar_dados():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    data_nascimento = entry_data.get()
    estado = combo_estado.get()

    # Verificar se algum campo está vazio
    if not nome or not email or not telefone or not data_nascimento or not estado:
        exibir_mensagem_erro("Erro, preencha todos os espaços!")
        return

    if "@" not in email:
        exibir_mensagem_erro("E-mail inválido!")
        return

    # Remover espaços em branco do número de telefone
    telefone = telefone.replace(" ", "")

    if not (telefone.isdigit() or (telefone[:2].isdigit() and len(telefone) == 12)):
        exibir_mensagem_erro("Telefone inválido!")
        return

    with open('dados.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, email, telefone, data_nascimento, estado])

    # Limpar os campos após salvar os dados
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_data.delete(0, tk.END)
    combo_estado.set('')

    exibir_mensagem_sucesso("Formulário preenchido com sucesso")


def exibir_mensagem_erro(mensagem):
    label_mensagem["text"] = "Erro: " + mensagem
    label_mensagem["fg"] = "red"


def exibir_mensagem_sucesso(mensagem):
    label_mensagem["text"] = mensagem
    label_mensagem["fg"] = "green"


def validar_telefone(event):
    telefone = entry_telefone.get()
    if not telefone.isdigit():
        exibir_mensagem_erro("Telefone inválido. Use apenas números.")
        return False
    return True


def capitalizar_primeira_letra(event):
    nome = entry_nome.get()
    if nome:
        nome_formatado = nome.capitalize()
        if nome != nome_formatado:
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, nome_formatado)


def validar_telefone(event):
    entrada = entry_telefone.get()
    if not entrada.isdigit():
        entry_telefone.delete(len(entrada) - 1, tk.END)


def validar_data(event):
    entrada = entry_data.get()
    if not entrada.replace('/', '').isdigit():
        entry_data.delete(len(entrada) - 1, tk.END)
    entry_data.delete(10, tk.END)  # Limitar o número máximo de caracteres da data


def aplicar_mascara_data(event):
    data = entry_data.get()
    if len(data) == 2 or len(data) == 5:
        entry_data.insert(tk.END, '/')
    if len(data) > 10:
        entry_data.delete(10, tk.END)


# Definir tamanho da janela e margens
largura_janela = 400
altura_janela = 400
margem_esquerda = 20
margem_direita = 20
margem_inferior = 45

# Calcula a largura total da janela considerando as margens
largura_total = largura_janela + margem_esquerda + margem_direita

# Calcula a altura total da janela considerando as margens
altura_total = altura_janela + margem_inferior


# Criar janela principal
janela = tk.Tk()
janela.title("Formulário Offline")
janela.configure(background="white")  # Definir o background como branco

# Definir tamanho da janela e posição inicial
posicao_x = int(janela.winfo_screenwidth() / 2 - largura_total / 2)
posicao_y = int(janela.winfo_screenheight() / 2 - altura_total / 2)
janela.geometry(f"{largura_total}x{altura_total}+{posicao_x}+{posicao_y}")


# Criar título do formulário
titulo = tk.Label(janela, text="Formulário", bg="white", fg="black", font=("Arial", 24, "bold"))
titulo.pack()

# Criar um espaço vazio abaixo do título
espaco_vazio = tk.Frame(janela, height=10, bg="white")
espaco_vazio.pack()

# Criar os rótulos e campos de entrada
label_nome = tk.Label(janela, text="Nome:", bg="white", fg="black", font=("Arial", 10, "bold"))
label_nome.pack()
entry_nome = tk.Entry(janela, justify="center")
entry_nome.pack()
entry_nome.config(highlightbackground="black", highlightthickness=2)  # Adicionar borda preta e aumentar a espessura
espaco_vazio = tk.Frame(janela, height=10, bg="white")
espaco_vazio.pack()
# Adicionar evento de capitalização da primeira letra
entry_nome.bind('<KeyRelease>', capitalizar_primeira_letra)

label_email = tk.Label(janela, text="E-mail:", bg="white", fg="black", font=("Arial", 10, "bold"))
label_email.pack()
entry_email = tk.Entry(janela, justify="center")
entry_email.pack()
entry_email.config(highlightbackground="black", highlightthickness=2)  # Adicionar borda preta e aumentar a espessura
espaco_vazio = tk.Frame(janela, height=10, bg="white")
espaco_vazio.pack()

label_telefone = tk.Label(janela, text="Telefone:", bg="white", fg="black", font=("Arial", 10, "bold"))
label_telefone.pack()
entry_telefone = tk.Entry(janela, justify="center")
entry_telefone.pack()
entry_telefone.config(highlightbackground="black", highlightthickness=2)  # Adicionar borda preta e aumentar a espessura
espaco_vazio = tk.Frame(janela, height=10, bg="white")
espaco_vazio.pack()

label_data = tk.Label(janela, text="Data de Nascimento:", bg="white", fg="black", font=("Arial", 10, "bold"))
label_data.pack()
entry_data = tk.Entry(janela, justify="center")
entry_data.pack()
entry_data.config(highlightbackground="black", highlightthickness=2)  # Adicionar borda preta e aumentar a espessura
espaco_vazio = tk.Frame(janela, height=10, bg="white")
espaco_vazio.pack()


# Aplicar máscara de data manualmente
entry_telefone.bind('<KeyRelease>', validar_telefone)
entry_data.bind('<KeyRelease>', validar_data)
entry_data.bind('<KeyRelease>', aplicar_mascara_data)

label_estado = tk.Label(janela, text="Estado:", bg="white", fg="black", font=("Arial", 10, "bold"))
label_estado.pack()


def selecionar_estado(event):
    combo_estado.selection_clear()
    combo_estado.selection_set(combo_estado.current())
    combo_estado.focus_set()


# Criar combobox para selecionar o estado
combo_estado = ttk.Combobox(janela, values=[
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
    'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC',
    'SP', 'SE', 'TO'
], background="white", foreground="black", state='readonly')
combo_estado.pack()

# Definir valor inicial como vazio
combo_estado.set('')

# Adicionar evento de seleção do estado
combo_estado.bind('<<ComboboxSelected>>', selecionar_estado)

# Estilo personalizado para a caixa de seleção de estados
style = ttk.Style(janela)
style.theme_create("custom_style", parent="alt", settings={
    "TCombobox": {
        "configure": {
            "selectbackground": "white",
            "fieldbackground": "white",
            "background": "white"
        },
        "map": {
            "background": [("readonly", "white")]
        }
    },
    "Custom.TCombobox": {
        "configure": {
            "bordercolor": "black",
            "borderwidth": 2
        }
    }
})
style.theme_use("custom_style")

# Espaço
espaco_vazio = tk.Frame(janela, height=10, bg="white")
espaco_vazio.pack()
espaco_vazio = tk.Frame(janela, height=10, bg="white")
espaco_vazio.pack()

# Criar rótulo para os termos
label_termos = tk.Label(janela, text="Você concorda com a LGPD da empresa?", bg="white", fg="black", font=("Arial", 10, "bold"))
label_termos.pack()

# Criar Checkbutton para aceitar os termos
aceitar_termos = tk.BooleanVar()
check_termos = tk.Checkbutton(janela, text="Sim", variable=aceitar_termos, bg="white")
check_termos.pack()


def verificar_termos():
    if aceitar_termos.get():
        salvar_dados()
    else:
        exibir_mensagem_erro("Aceite o Termo para finalizar o formulário!")


# Criar um espaço vazio acima do botão de salvar
espaco_vazio = tk.Frame(janela, height=10, bg="white")
espaco_vazio.pack()
espaco_vazio = tk.Frame(janela, height=10, bg="white")
espaco_vazio.pack()

# Criar botão de salvar
botao_salvar = tk.Button(janela, text="Salvar", command=verificar_termos, bg="white", fg="black")
botao_salvar.pack()

# Criar label para exibir mensagens
label_mensagem = tk.Label(janela, text="", bg="white", fg="black")
label_mensagem.pack()

# Definir limite máximo de caracteres para o campo de telefone
vcmd = (janela.register(lambda s: len(s) <= 12), '%P')
entry_telefone.config(validate="key", validatecommand=vcmd)

# CSS python
janela.configure(background="white")

# Iniciar a execução da interface gráfica
janela.mainloop()
