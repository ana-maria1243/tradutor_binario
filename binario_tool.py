
import sys

#Colocar primeiro a sequencia em lista


def traducao(numero:list) -> str:
    #Pegar o binario e converter para decimal
    lista_x = list(numero)
    n=0
    binario = 0
    soma_binario = 0

    for i in lista_x.__reversed__():
        if i == '1':
           binario = 1*(2**n)
        elif i == '0':
            binario = 0           
        else:
            print("Nao da certo")
        n += 1 
        soma_binario += binario  
     
        # consultando letra traduzida da tabela asc 
        letra_traduzida = chr(soma_binario)

    return(letra_traduzida)


def dividir_de_tras_para_frente(lista, tamanho=8):
  # Inverte a lista inteira
  invertida = lista[::-1]

  # Divide a lista invertida em blocos do tamanho desejado
  blocos = [invertida[i : i + tamanho] for i in range(0, len(invertida), tamanho)]

  # Inverte a ordem dos elementos de cada bloco e inverte a lista de blocos
  resultado = [bloco[::-1] for bloco in blocos][::-1]

  return resultado


def main():
    lista_letras = []
    texto_binario = sys.argv[1]
    lista = list(texto_binario)
    try:
        nova_lista = dividir_de_tras_para_frente(lista)
        for i in nova_lista:
            while len(i)<8:
               i.insert(0,'0')
            
            lista_letras.append(traducao(i))
            frase_traduzida = "".join(lista_letras)
        print("traducao= "+ frase_traduzida)

        
    except:
        print("nao da certo")    

main()

