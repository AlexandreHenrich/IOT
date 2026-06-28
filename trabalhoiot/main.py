import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector # Biblioteca do MySQL
from datetime import datetime

# Função para conectar no MySQL
def conectar():
 
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root", 
        database="TrabalhoIoT"
    )

def carregar_dispositivos():
    # Limpa a tabela (treeview) antes de carregar
    for linha in tree_dispositivos.get_children():
        tree_dispositivos.delete(linha)
        
    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Dispositivos")
        linhas = cursor.fetchall()
        for linha in linhas:
            tree_dispositivos.insert("", tk.END, values=linha)
        con.close()
    except Exception as e:
        messagebox.showerror("Erro", "Erro ao conectar no banco: " + str(e))

def atualizar_dashboard():
    try:
        con = conectar()
        cursor = con.cursor()
        
        # Pega os totais - usando fetchone()[0] pra pegar só o numero
        cursor.execute("SELECT COUNT(*) FROM Dispositivos")
        lbl_total.config(text="Total de Dispositivos: " + str(cursor.fetchone()[0]))
        
        cursor.execute("SELECT COUNT(*) FROM Dispositivos WHERE Status = 'Ativo'")
        lbl_ativos.config(text="Ativos: " + str(cursor.fetchone()[0]))
        
        cursor.execute("SELECT COUNT(*) FROM Dispositivos WHERE Status = 'Inativo'")
        lbl_inativos.config(text="Inativos: " + str(cursor.fetchone()[0]))
        
        cursor.execute("SELECT COUNT(*) FROM Leituras")
        lbl_leituras.config(text="Total de Leituras: " + str(cursor.fetchone()[0]))
        
        con.close()
    except:
        pass # Ignora o erro se o banco ainda não tiver online

def salvar_dispositivo():
    nome = txt_nome.get()
    tipo = txt_tipo.get()
    local = txt_local.get()
    data = txt_data.get()
    status = combo_status.get()
    
    if nome == "":
        messagebox.showwarning("Aviso", "Preenche o nome do dispositivo!")
        return

    try:
        con = conectar()
        cursor = con.cursor()
        # Inserindo os dados concatenando string
        sql = f"INSERT INTO Dispositivos (Nome, Tipo, Localizacao, DataInstalacao, Status) VALUES ('{nome}', '{tipo}', '{local}', '{data}', '{status}')"
        cursor.execute(sql)
        con.commit()
        con.close()
        
        messagebox.showinfo("Sucesso", "Dispositivo cadastrado!")
        carregar_dispositivos()
        atualizar_dashboard()
    except Exception as e:
        messagebox.showerror("Erro", "Deu ruim ao salvar: " + str(e))

def excluir_dispositivo():
    id_disp = txt_id_excluir.get()
    if id_disp != "":
        try:
            con = conectar()
            cursor = con.cursor()
            cursor.execute(f"DELETE FROM Dispositivos WHERE Id = {id_disp}")
            con.commit()
            con.close()
            
            messagebox.showinfo("Aviso", "Apagado!")
            carregar_dispositivos()
            atualizar_dashboard()
        except Exception as e:
            messagebox.showerror("Erro", "Erro ao excluir: " + str(e))
    else:
        messagebox.showwarning("Aviso", "Digita o ID para excluir.")

def registrar_leitura():
    id_disp = txt_id_leitura.get()
    valor = txt_valor.get().replace(",", ".") # Troca virgula por ponto pro banco não reclamar
    
    if id_disp == "" or valor == "":
        messagebox.showwarning("Aviso", "Preenche o ID e o valor!")
        return
        
    try:
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        con = conectar()
        cursor = con.cursor()
        sql = f"INSERT INTO Leituras (DispositivoId, DataHora, Valor) VALUES ({id_disp}, '{data_atual}', {valor})"
        cursor.execute(sql)
        con.commit()
        con.close()
        
        messagebox.showinfo("Sucesso", "Leitura simulada com sucesso!")
        atualizar_dashboard()
    except Exception as e:
        messagebox.showerror("Erro", "Erro ao ler sensor: " + str(e))

# ----- DESENHANDO A TELA (TKINTER) -----
janela = tk.Tk()
janela.title("Sistema IoT - Trabalho")
janela.geometry("800x650")

# ----- DASHBOARD -----
frame_dash = tk.LabelFrame(janela, text="Dashboard")
frame_dash.pack(fill="x", padx=10, pady=5)

lbl_total = tk.Label(frame_dash, text="Total de Dispositivos: 0")
lbl_total.grid(row=0, column=0, padx=10, pady=5)
lbl_ativos = tk.Label(frame_dash, text="Ativos: 0")
lbl_ativos.grid(row=0, column=1, padx=10, pady=5)
lbl_inativos = tk.Label(frame_dash, text="Inativos: 0")
lbl_inativos.grid(row=0, column=2, padx=10, pady=5)
lbl_leituras = tk.Label(frame_dash, text="Total de Leituras: 0")
lbl_leituras.grid(row=0, column=3, padx=10, pady=5)

# ----- CADASTRO -----
frame_cad = tk.LabelFrame(janela, text="Cadastrar Dispositivo")
frame_cad.pack(fill="x", padx=10, pady=5)

tk.Label(frame_cad, text="Nome:").grid(row=0, column=0)
txt_nome = tk.Entry(frame_cad)
txt_nome.grid(row=0, column=1)

tk.Label(frame_cad, text="Tipo:").grid(row=0, column=2)
txt_tipo = tk.Entry(frame_cad)
txt_tipo.grid(row=0, column=3)

tk.Label(frame_cad, text="Local:").grid(row=1, column=0)
txt_local = tk.Entry(frame_cad)
txt_local.grid(row=1, column=1)

tk.Label(frame_cad, text="Data:").grid(row=1, column=2)
txt_data = tk.Entry(frame_cad)
txt_data.grid(row=1, column=3)

tk.Label(frame_cad, text="Status:").grid(row=2, column=0)
combo_status = ttk.Combobox(frame_cad, values=["Ativo", "Inativo"])
combo_status.grid(row=2, column=1)

btn_salvar = tk.Button(frame_cad, text="Salvar", command=salvar_dispositivo)
btn_salvar.grid(row=2, column=3, pady=5)

# ----- EXCLUSÃO E SIMULAÇÃO -----
frame_acoes = tk.Frame(janela)
frame_acoes.pack(fill="x", padx=10, pady=5)

tk.Label(frame_acoes, text="ID p/ Excluir:").grid(row=0, column=0)
txt_id_excluir = tk.Entry(frame_acoes, width=5)
txt_id_excluir.grid(row=0, column=1)
btn_excluir = tk.Button(frame_acoes, text="Excluir", command=excluir_dispositivo)
btn_excluir.grid(row=0, column=2, padx=5)

tk.Label(frame_acoes, text="ID p/ Ler Sensor:").grid(row=0, column=3, padx=10)
txt_id_leitura = tk.Entry(frame_acoes, width=5)
txt_id_leitura.grid(row=0, column=4)
tk.Label(frame_acoes, text="Valor:").grid(row=0, column=5)
txt_valor = tk.Entry(frame_acoes, width=8)
txt_valor.grid(row=0, column=6)
btn_simular = tk.Button(frame_acoes, text="Registrar Leitura", command=registrar_leitura)
btn_simular.grid(row=0, column=7, padx=5)

# ----- TABELA (GRID) -----
colunas = ("ID", "Nome", "Tipo", "Local", "Data", "Status")
tree_dispositivos = ttk.Treeview(janela, columns=colunas, show="headings")
for col in colunas:
    tree_dispositivos.heading(col, text=col)
    tree_dispositivos.column(col, width=120)
tree_dispositivos.pack(fill="both", expand=True, padx=10, pady=10)

# Iniciando o programa
carregar_dispositivos()
atualizar_dashboard()

janela.mainloop()