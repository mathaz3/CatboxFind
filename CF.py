from random import choice
from string import ascii_lowercase,digits
from os import system

#cria arquivo links_encontrados.txt caso nao exista
try:
    with open("links_encontrados.txt","x") as links_encontrados:
        pass
except FileExistsError:
    pass

def tentativa():
    global formatos

    varia = ""
    varia += choice(ascii_lowercase+digits)
    varia += choice(ascii_lowercase+digits)
    varia += choice(ascii_lowercase+digits)
    varia += choice(ascii_lowercase+digits)
    varia += choice(ascii_lowercase+digits)
    varia += choice(ascii_lowercase+digits)

    for formato in formatos:
        url = f"https://files.catbox.moe/{varia}.{formato}"
        print(f"testando {url}")
        system(f"wget {url}")
        


formatos = input("quais formatos procurar(separados por virgula)?: ").split(",")
if formatos == [""]:
    formatos = ["jpg","png","gif","mp4","avi","txt"]

n_vezes = int(input("tentar quantas vezes?: "))

for vezes in range(n_vezes):
    tentativa()