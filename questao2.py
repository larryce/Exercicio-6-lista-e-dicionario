funcionarios={}

aux= int(input("se deseja cadastrar funcionario entre com 1, se n�o quiser digite 2:"))
while (aux==1):
  matricula=str(input("entre com a matricula do funcionario:"))
  nome= str(input("entre com o nome do funcionario:"))
  aux= int(input("se deseja cadastrar outro funcionario entre com 1, se n�o quiser digite 2:"))
  if (aux==2):
    print("voc� n�o quer cadastrar funcionarios!")
    break 
 
def adicionarFuncionario(matricula, nome):
  funcionarios[matricula]= nome
  return funcionarios

def buscarFuncionario(matricula):
  matricula=str(input("entre com a matricula do funcionario para buscar:"))
  if matricula in funcionarios:
    print("ele est� na lista de funcionarios")
  else:
    print("ele n�o est� na lista de funcionarios")
    

def exibirFuncionarios(funcionarios):
  for x in funcionarios.items():
    print(x)
    
adicionarFuncionario(matricula,nome)
buscarFuncionario(matricula)
exibirFuncionarios(funcionarios)