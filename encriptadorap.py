#importar as bibliotecas
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
#Revela palavra


def encriptar():

    palavra=input("Digite a palavra:")
    if palavra == '':
        print("Digite alguma coisa")
    else:
       #gerar chave de forma aletoria 
        chave=get_random_bytes(16)
        chavebase32=base64.b32encode(chave)
        #Garanta que a palavra tera somente 16 bits
        conv=palavra+'*'*(16-len(palavra)%16)
        #Prepare a cifra que será usada para a criptografia
        cifra=AES.new(chave,AES.MODE_ECB)
        #Converta a saida do texto para base64 codificação 32 bits e criptografe a palavra
        print("Criptografando texto...")
        saida = base64.b32encode(cifra.encrypt(conv))
        print("Texto Criptografado!")
        #Imprima a palavra encriptada
        #print(saida)
        #print("Chave:",chavebase32)
        #gerar aquivo
        print("Gerando arquivo...")
        nomearquivo="card.enc"
        arquivosaida=open(nomearquivo,'wb')
        arquivosaida.write(saida)
        arquivosaida.close()
        print("Arquivo Criptografado gerado!")
        #gerar arquivo da chave
        print("Gerando arquivo da chave....")
        nomearquivokey="key.cert"
        arquivokey=open(nomearquivokey,'wb')
        arquivokey.write(chavebase32)
        arquivokey.close()
        print("Arquivo chave gerado com sucesso!",nomearquivokey)
        exit()

def verificamidia():
    pipe=os.popen("lsblk -o MOUNTPOINT |grep media")
    path=pipe.read()
    pipe.close()
    while path == "":
         verificamidia()
    else:
        encriptar()
        print("pen drive montado")

#def copiakey():
    






#---------------------TESTES -----------------------
verificamidia()
#encriptar()
