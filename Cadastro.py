import customtkinter as ctk
import os
import sys

def get_database_path():
    #Instalar na pasta do .exe
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, "clientes.txt")

def show_error(error_code):
    error_window = ctk.CTkToplevel(janela)
    error_window.title("Erro")
    error_window.geometry("300x150")
    
    error_window.transient(janela)
    error_window.grab_set()
    error_window.attributes('-topmost', True)
    
    label = ctk.CTkLabel(error_window, text=f"Erro: {error_code}", font=("Arial", 14))
    label.pack(pady=20, padx=20)
    button = ctk.CTkButton(error_window, text="OK", command=error_window.destroy,
                             fg_color="#FF0000", text_color="white")
    button.pack(pady=10)

def gerar_id_cliente():
    count = 0
    file_path = get_database_path()
    try:
        with open(file_path, "r") as arquivo:
            for linha in arquivo:
                if linha.startswith("ID:"):
                    count += 1
    except FileNotFoundError:
        #Se não estir um banco de dados criarei um :)
        with open(file_path, "w") as arquivo:
            arquivo.write("")
    return count + 1

def salvar_cliente():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()
    cpf = entry_cpf.get().strip()
    estado = entry_estado.get().strip()
    cidade = entry_cidade.get().strip()
    bairro = entry_bairro.get().strip()
    endereco = entry_endereco.get().strip()

    if not nome or not email or not telefone or not cpf or not estado or not cidade or not bairro or not endereco:
        show_error("ERRO 001")  #Preencha tudo
        return
    
    file_path = get_database_path()
    
    #Verifica se o cliente já existe no arquivo
    cliente_existe = False
    try:
        with open(file_path, "r") as arquivo:
            conteudo = arquivo.read()
            if f"Nome: {nome}" in conteudo and f"Email: {email}" in conteudo:
                cliente_existe = True
    except FileNotFoundError:
        pass

    if cliente_existe:
        show_error("ERRO 2")  #Mesma pessoa
        return

    #ID do cliente
    id_cliente = gerar_id_cliente()
    
    #Banco de Dados
    with open(file_path, "a") as arquivo:
        arquivo.write(f"ID: {id_cliente}\n")
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Email: {email}\n")
        arquivo.write(f"Telefone: {telefone}\n")
        arquivo.write(f"CPF: {cpf}\n")
        arquivo.write(f"Estado: {estado}\n")
        arquivo.write(f"Cidade: {estado}\n")
        arquivo.write(f"Bairro: {bairro}\n")
        arquivo.write(f"Endereço: {endereco}\n")
        arquivo.write("-" * 40 + "\n")
    
    print(f"Cliente {id_cliente} salvo: {nome}, {email}, {telefone}, {endereco}")

#Interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

janela = ctk.CTk()
janela.title("Cadastro de Clientes")
janela.geometry("630x250")

frame = ctk.CTkFrame(janela)
frame.pack(pady=20, padx=20, fill="both", expand=True)

#Nome
label_nome = ctk.CTkLabel(frame, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nome = ctk.CTkEntry(frame, width=200)
entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="w")

#Email
label_email = ctk.CTkLabel(frame, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_email = ctk.CTkEntry(frame, width=200)
entry_email.grid(row=1, column=1, padx=10, pady=5, sticky="w")

#Telefone
label_telefone = ctk.CTkLabel(frame, text="Telefone:")
label_telefone.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_telefone = ctk.CTkEntry(frame, width=200)
entry_telefone.grid(row=2, column=1, padx=10, pady=5, sticky="w")

#CPF
label_cpf = ctk.CTkLabel(frame, text="CPF:")
label_cpf.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_cpf = ctk.CTkEntry(frame, width=200)
entry_cpf.grid(row=3, column=1, padx=10, pady=5, sticky="w")

#Estado
label_estado = ctk.CTkLabel(frame, text="Estado:")
label_estado.grid(row=0, column=3, padx=10, pady=5, sticky="e")
entry_estado = ctk.CTkEntry(frame, width=200)
entry_estado.grid(row=0, column=4, padx=10, pady=5, sticky="w")
#Cidade

label_cidade = ctk.CTkLabel(frame, text="Cidade:")
label_cidade.grid(row=1, column=3, padx=10, pady=5, sticky="e")
entry_cidade = ctk.CTkEntry(frame, width=200)
entry_cidade.grid(row=1, column=4, padx=10, pady=5, sticky="w")

#Bairro
label_bairro = ctk.CTkLabel(frame, text="Bairro:")
label_bairro.grid(row=2, column=3, padx=10, pady=5, sticky="e")
entry_bairro = ctk.CTkEntry(frame, width=200)
entry_bairro.grid(row=2, column=4, padx=10, pady=5, sticky="w")

#Endereço
label_endereco = ctk.CTkLabel(frame, text="Endereço:")
label_endereco.grid(row=3, column=3, padx=10, pady=5, sticky="e")
entry_endereco = ctk.CTkEntry(frame, width=200)
entry_endereco.grid(row=3, column=4, padx=10, pady=5, sticky="w")



#Save
botao_salvar = ctk.CTkButton(frame, text="Salvar", command=salvar_cliente)
botao_salvar.grid(row=4, column=0, columnspan=5, pady=20, sticky="ew")

janela.mainloop()
print("Aplicativo Fechado")
