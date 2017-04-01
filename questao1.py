dicionario={}
p=0
diassemana=7
continuar='s'
while (continuar=='s'):
  aux=int(input("entre com 1 para continuar e 2 para sair:"))
  if (aux==1):
    continuar='s'
  while p<diassemana:
    posicaochave=int(input("entre com a posicao:"))
    diavalor=str(input("entre com o dia da semana:"))
    aux=int(input("entre com 1 para continuar e 2 para sair:"))
    if (aux==2):
      continuar='a'
      break
      p+=1
    if (aux==2):
      continuar='a'
      break
          

def adicionardia(dicionario,diavalor,posicaochave):
  dicionario[posicaochave]=diavalor
def exibirdias(diavalor):
  for posicaochave,diavalor in dicionario.items():
    print(dicionario.items())
    
adicionardia(dicionario,diavalor,posicaochave)
exibirdias(diavalor)