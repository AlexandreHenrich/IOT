# IOT
# Sistema de Monitoramento de Dispositivos IoT

Este é um projeto acadêmico desenvolvido para a disciplina de [Nome da Disciplina], com o objetivo de criar um sistema de gerenciamento e monitoramento de dispositivos IoT simulados utilizando Python e MySQL.

## 🚀 Funcionalidades
- **Cadastro de Dispositivos:** Adição, edição e remoção de sensores no sistema.
- **Simulação de Leituras:** Registro de dados de sensores (temperatura, umidade, etc.) associados a um dispositivo específico.
- **Dashboard em Tempo Real:** Visualização do total de dispositivos ativos/inativos e contagem de leituras realizadas.
- **Relacionamento:** Banco de dados relacional que vincula dispositivos a seus históricos de medição.

## 🛠 Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Interface:** Tkinter (Interface Gráfica)
- **Banco de Dados:** MySQL
- **Conexão:** mysql-connector-python

## ⚙️ Como Configurar e Rodar

1. **Banco de Dados:**
   - Tenha o MySQL instalado e rodando em sua máquina.
   - Execute o script `script.sql` (disponível na pasta do projeto) no seu gerenciador de banco de dados (ex: MySQL Workbench).
   - Certifique-se de que o nome do banco seja `TrabalhoIoT`.

2. **Dependências:**
   - Certifique-se de ter o Python instalado.
   - Instale o conector do MySQL rodando o seguinte comando no seu terminal:
     ```bash
     pip install mysql-connector-python
     ```

3. **Executando o Sistema:**
   - Clone este repositório ou baixe os arquivos.
   - Abra o terminal na pasta do projeto.
   - Execute o comando:
     ```bash
     python main.py
     ```

## 📂 Estrutura do Projeto
- `main.py`: Código-fonte principal com a interface e a lógica de conexão.
- `script.sql`: Script contendo a estrutura das tabelas e dados de teste.
- `README.md`: Este arquivo de documentação.

---
Desenvolvido por: [Seu Nome]
