# ecotrack-backend
# 💧 EcoTrack - Gestão de Postos de Água (Back-end)

Um sistema de gerenciamento Back-end executado via interface de linha de comando (CLI), desenvolvido para monitorar o cadastro e o status de funcionamento de postos de água. 

Este projeto foi construído para demonstrar habilidades sólidas na criação de rotinas **CRUD** completas, integração de Python com bancos de dados relacionais e aplicação de boas práticas de segurança e arquitetura de código.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Banco de Dados:** MySQL
* **Biblioteca de Integração:** `mysql-connector-python`

## ⚙️ Funcionalidades (CRUD)
O sistema conta com um menu interativo no terminal que permite:
1. **Read (Ler):** Listar todos os postos de água cadastrados no banco de dados.
2. **Create (Cadastrar):** Inserir novos postos informando Nome, Endereço e Status (Ativo/Inativo).
3. **Update (Atualizar):** Modificar o status de funcionamento de um posto específico utilizando seu ID.
4. **Delete (Deletar):** Excluir permanentemente o registro de um posto do banco de dados.

## 🚀 Destaques Técnicos e Boas Práticas
* **Segurança contra SQL Injection:** Utilização de parâmetros (`%s`) nas queries SQL em vez de concatenação direta de strings.
* **Arquitetura DRY (Don't Repeat Yourself):** Centralização da conexão com o banco de dados em uma única função modular (`conectar_banco`), facilitando a manutenção e a escalabilidade.
* **Gerenciamento de Memória e Exceções:** Uso de blocos `try`, `except` e `finally` para garantir que as conexões e cursores do banco de dados sejam fechados corretamente, evitando vazamento de memória e travamentos.
* **Setup Automatizado:** O script inclui a função `configurar_banco()` que cria automaticamente o banco de dados `ecotrack` e a tabela `postos_de_agua` caso eles ainda não existam.

## 🗄️ Estrutura do Banco de Dados
A tabela principal (`postos_de_agua`) possui a seguinte estrutura:
* `id` (INT, Primary Key, Auto Increment)
* `nome` (VARCHAR 100, Not Null)
* `endereco` (VARCHAR 200, Not Null)
* `status_funcionamento` (TINYINT, Not Null, Default 1)

## 💻 Como Executar o Projeto

1. Certifique-se de ter o **Python** e um servidor **MySQL** (como XAMPP, WAMP ou MySQL Server) instalados na sua máquina.
2. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/ecotrack.git](https://github.com/SEU-USUARIO/ecotrack.git)
