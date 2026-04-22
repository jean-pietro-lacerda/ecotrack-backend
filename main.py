
import mysql.connector
from mysql.connector import Error
def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''# coloque a senha do seu banco de dados aqui
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar com o MySQL: {e}")
        return None

def configurar_banco():
    try:
        conexao = conectar_banco()
        if conexao and conexao.is_connected():
            cursor = conexao.cursor()

            cursor.execute("CREATE DATABASE IF NOT EXISTS ecotrack")

            conexao.database = 'ecotrack'

            tabela_sql = '''
                CREATE TABLE IF NOT EXISTS postos_de_agua (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nome VARCHAR(100) NOT NULL,
                    endereco VARCHAR(200) NOT NULL,
                    status_funcionamento TINYINT NOT NULL DEFAULT 1
                )
            '''
            cursor.execute(tabela_sql)
            print("Banco e tabela 'postos_de_agua' criados com sucesso!")

    except Error as e:
        print(f"Erro ao conectar com o MySQL: {e}")

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

def cadastra_posto(nome, endereco,status):
    try:
        conexao = conectar_banco()
        if conexao and conexao.is_connected():# se conectar faço isso ai
            cursor = conexao.cursor()

            conexao.database = 'ecotrack' # conectando com o banco de dados

            comando_sql = '''
            INSERT INTO postos_de_agua (nome, endereco, status_funcionamento)
            VALUES (%s, %s, %s)
            '''
            # jogando valores em uma lista
            valores = [nome, endereco, status]
            cursor.execute(comando_sql, valores)
            conexao.commit()# dou o commit pra salvar
            print("Posto salvo com sucesso.")
    except Exception as erro:
        print(f"Deu erro: {erro}")
    finally:
        cursor.close()
        conexao.close()

def ler_lista() -> str:
    try:
        conexao = conectar_banco()

        if conexao and conexao.is_connected():
            cursor = conexao.cursor()

            conexao.database = 'ecotrack' # conectando com o banco de dados

            comando_sql = '''
            SELECT * FROM postos_de_agua
            '''
            cursor.execute(comando_sql)
            list_result = cursor.fetchall()
            for c in list_result:
                print(c)
    except Exception as erro:
        print(f"Deu erro: {erro}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_dados(id_posto, novo_status):# somente o status se ta fucionando ou n
    try:
        conexao = conectar_banco()
        if conexao and conexao.is_connected():
            cursor = conexao.cursor()

            conexao.database = 'ecotrack' # conectando com o banco de dados
            comando_sql = '''
            UPDATE postos_de_agua SET status_funcionamento = %s WHERE id = %s
            '''
            valores =[novo_status, id_posto]
            cursor.execute(comando_sql, valores)
            conexao.commit()
    except Exception as erro:
        print(f"Deu erro: {erro}")
    finally:
        cursor.close()
        conexao.close()

def deletar_posto (id):
    try:
        conexao = conectar_banco()
        if conexao and conexao.is_connected():
            cursor = conexao.cursor()

            conexao.database = 'ecotrack' # conectando com o banco de dados
            comando_sql = '''
            DELETE FROM postos_de_agua WHERE id =%s
            '''
            valores = [id]
            cursor.execute(comando_sql, valores)
            conexao.commit()
    except Exception as erro:
        print(f"Deu erro: {erro}")
    finally:
        cursor.close()
        conexao.close()


# executa a função
if __name__ == '__main__':
    configurar_banco()
    while True:
        print("-"*25)
        print("Informe a Função que você deseja Usar \n Ler a tabela[1] \n Cadastrar novo posto [2] \n Atualizar dados de funcionamento [3] \n Deletar um Posto [4] \n Pra finalizar o programa [0]")
        print("-"*25)
        number = int(input())
        if (number == 1):
            ler_lista()
        elif (number == 2):
            nome = input("Nome do Posto: ")
            endereco = input("Endereço: ")
            status = int(input("Status: [ Ativo = 1], [Inativo = 0] : "))
            cadastra_posto(nome, endereco, status)
        elif (number == 3):
            valor_ID = input("Informe o ID do posto que você deseja mudar: ")
            sts_novo = input("Você deseja mudar pra qual status [1/0]: ")
            atualizar_dados(valor_ID, sts_novo)
        elif (number == 4):
            id = input(" linha da tabela você deseja excluir: ")
            deletar_posto(id)
        elif (number == 0):
            print("Finalizando o programa.....")
            break
        print("")











