# CF.py - busca com padrões randômicos por arquivos no site/prefixo https://files.catbox.moe/
pequeno script escrito em python que procura por arquivos na URL com prefixo https://files.catbox.moe/
## descrição
usando combinações randômicas baseados em um padrão(RE:[a-z0-9]{6} ou string de 6 caracteres usando letras minúsculas do alfabeto e números de 0 à 9) o script tenta combinações de URL e formato de arquivos com o WGET, quando a URL é válida o arquivo é baixado.
## requisitos
ter python3 e WGET em um terminal
## execução
```bash
python3 CF.py
```
## funcionou com sucesso em:
[Termux](https://github.com/termux/termux-app) e terminais Linux
## problemas ainda não resolvidos
por algum motivo, no windows mesmo possuindo o WGET no cmd, os arquivos são encontrados mas não baixados
