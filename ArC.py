# -*- coding: utf-8 -*- #
# -*- Por favor tenha consideração e não edite e poste em outros locais dizendo que o código -*- #
# -*- é seu, obrigado! -*- #

import time
import os
import sys
try:
   from jspp import *
except:
    print("[x] Você não tem o package criado por JhinScripter necessário para rodar este código!")
    print("[+] Utilize: pip install jspp")
    sys.exit()

def ToS():
    print("[+] O script é para estudos e para facilitar seus estudos, portanto nós não nos responsabilizamos por")
    print("[+] utilização com mal intencionamento, responda a pergunta abaixo! \n")
    ToS = input("[!] Se você concorda com essas regras por favor digite \"Y\": ")
    return ToS.lower()

if ToS() in [ "Y" , "y" ]:
    print("[+] Obrigado continuaremos, aguarde inicializar o programa!")
    time.sleep(3)
    os.system("cls || clear")
    time.sleep(2)
    print("[+] Créditos para Jhin_Scripter pelo PKG jspp, obrigado!")
    print("[+] Créditos para WhoniX (EU) pelo script do python")
    print("[+] Aguarde o inicializamento do programa!")
    time.sleep(5)
    os.system("cls || clear")
    print("[+] Programa iniciado, podes usufruir-lo!")
    nome = input("[+] Digite o nome do arquivo á criar: ")
else:
    print("[x] - Que pena, não podemos continuar por aqui!")
    time.sleep(3)
    sys.exit()

texto = input("[+] Digite o texto que ficará dentro do arquivo: ")
simple_create_file(nome, texto)

def pergunta():
    pergunta = input("[!] Voce deseja alterar a data do arquivo? (Y/n):  ")
    return pergunta.lower()

if pergunta() in [ "Y", "y" ]:
    print("[+] Ok, aguarde um pouquinho para iniciar o programa!")
    ano = int(input("[+] Selecione o ano que desejas salvar o arquivo: "))
    mes = int(input("[+] Selecione o mes que desejas salvar o arquivo: "))
    dia = int(input("[+] Selecione o dia que desejas salvar o arquivo: "))
    hora = int(input("[+] Selecione a hora que desejas salvar o arquivo: "))
    minuto = int(input("[+] Selecione o minuto que desejas salvar o arquivo: "))
    segundo = int(input("[+] Selecione o segundo que desejas salvar o arquivo: "))
    change_file_date(nome, ano, mes, dia, hora, minuto, segundo)
elif pergunta() in [ "N", "n" ]:
    print("[+] Voce selecionou não, saindo do programa!")
    sys.exit()
else:
    print("[x] Use somente os parametros \"Y/n\" por favor!")
