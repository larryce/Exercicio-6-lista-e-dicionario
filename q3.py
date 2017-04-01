
def cadastrarProduto(produtos, produto, preco):
  produtos[produto]=preco
  return produtos
def exibirProdutos(produtos):
  for x in produtos.items():
   print(x)

def removerProduto (produtos, produtorem):
  produtorem= str(input("entre com o produto a ser removido:"))
  del produtos[produtorem]

def exibirCaroProduto (produtos):
  #Exibir produto mais caro dos produtos cadastrados
  print (max(produtos, key=produtos.get()))

def exibirbaratoProduto (produtos):
  #Exibir produto mais barato dos produtos cadastrados
  print (min(produtos, key=produtos.get()))
 
def main(args=none):
  #metodo principal
  produtos={}
  produtorem= 0
  lista=[]
  aux= int(input("entre com 1 para adicionar produtos e 2 se você nao quiser cadastrar:"))
  while (aux==1):
    produto=str(input("entre com o nome do produto:"))
    preco= float(input("entre com o preço do produto:"))
    lista.append(produto)
    aux= int(input("se deseja adicionar outro produto entre com 1, se não quiser digite 2:"))
    if (aux==2):
      print("você não quer adicionar mais produtos!")
      break
  cadastrarProduto(produtos, produto, preco)
  exibirProdutos(produtos)
  removerProduto (produtos, produtorem)
  exibirCaroProduto(produtos)
  exibirbaratoProduto(produtos)
  if __name__=="__main__":
    main()