funcionarios={}

aux= int(input("se deseja cadastrar funcionario entre com 1, se não quiser digite 2:"))
while (aux==1):
  matricula=str(input("entre com a matricula do funcionario:"))
  nome= str(input("entre com o nome do funcionario:"))
  aux= int(input("se deseja cadastrar outro funcionario entre com 1, se não quiser digite 2:"))
  if (aux==2):
    print("você não quer cadastrar funcionarios!")
    break 
 
def adicionarFuncionario(matricula, nome):
  funcionarios[matricula]= nome
  return funcionarios

def buscarFuncionario(matricula):
  matricula=str(input("entre com a matricula do funcionario para buscar:"))
  if matricula in funcionarios:
    print("ele está na lista de funcionarios")
  else:
    print("ele não está na lista de funcionarios")
    

def exibirFuncionarios(funcionarios):
  for x in funcionarios.items():
    print(x)
    
adicionarFuncionario(matricula,nome)
buscarFuncionario(matricula)
exibirFuncionarios(funcionarios)