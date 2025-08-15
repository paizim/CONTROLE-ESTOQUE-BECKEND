import sqlite3

class Gestao:
    def _init_(self, banco):
        self.conn = sqlite3.connect(banco)
        self.criar_tabela_estoque()
    def criar_tabela_estoque(self):
        cursor = self.conn.cursor()
        cursor.execute('''
             CREATE TABLE IF NOT EXISTS estoque(
                 id INTEGER  PRIMARY  KEY,
                 produto TEXT,
                 quantidade  INTEGER
             )       
        ''')
        self.conn.commit()
    def selecionar_produto(self, produto, quantidade):
        cursor = self.conn.cursor() 
        cursor.execute(
            "INSERT INTO estoque (produto, quantidade) VALUES (?,?)", (produto, quantidade))
        self.conn.commit()
    
    def remover_produto(self, produto, quantidade):
         cursor = self.conn.cursor() 
         cursor.execute(
             "SELECT quantidade FROM estoque WHERE produto=? WHERE produto=?",(produto,))
         resultado = cursor.fetchone()
         if resultado:
             estoque_atual = resultado[0]
             if estoque_atual >= quantidade:
                 cursor.execute("UPDATE estoque SET quantidade=? WHERE produto=?",
                                (estoque_atual - quantidade,produto))
                 self.conn.commit()
             else:
                 print(f"Quantidade insulficiente de {produto} em estoque.")
         else:
            print(f"{produto} não encontrado no estoque.")
    def consultar_estoque(self, produto):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT quantidade FROM estoque WHERE produto=?",(produto,))
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else: 
            return 0
    
    def listar_produtos(self):
       cursor = self.conn.cursor()
       cursor.execute("SELECT produto FROM estoque")
       produto = cursor.fetchall()
       return [produto[0] for produto in produto]
   
sistema = Gestao("estoque.db")

sistema.adicionar_produto("Camisa",30)
sistema.adicionar_produto("Bermuda",50)
sistema.adicionar_produto("Calça",20)

estoque_camisa = sistema.consultar_estoque("Camisa")
print(f"Quantidade de camisas no estoque: {estoque_camisa}")

sistema.remover_produto("Calça",10)

produto_em_estoque = sistema.listar_produtos()
print(f"Produtos em estoque: {produto_em_estoque}")
        
    
                 
        