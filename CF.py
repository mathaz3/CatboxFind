from random import choice
from string import ascii_lowercase,digits
from os import system

def tentativa():
    global formatos

    # nao achei outra maneira de fazer isso, no futuro talvez eu melhore isso
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

print("tentar quantas vezes?: ")
opcao=int(input("1---limitadas | 2---infinitas\n---> "))
if opcao==1:
    n_vezes=int(input("numero de vezes: "))
    for vezes in range(n_vezes):
        tentativa()
elif opcao==2:
    while True:
        tentativa()
