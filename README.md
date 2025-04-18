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
## estatísticas dos arquivos encontrados
UNIVERSO: 170
|TIPO|QUANTIDADE|PORCENTAGEM|
|:-:|:-:|:-:|
|memes|3|1.76%|
|porno|30|17.65%|
|gore|4|2.35%|
|porno ilegal|1|0.59%|
|criminoso|1|0.59%|
|outros|131|77.06%|

gore:pode se referir tanto ao gore em si como com conteúdo violento
porno ilegal: se refere à pornografia ilegal(cp, necrofilia, estupro, etc.) encontrada
criminoso: se refere à conteúdo proveniente de atividades criminosas(clonagem de cartão, neonazismo, hacking, etc.)
outros: se refere à conteúdo que não se encaixa em nenhuma categoria anterior(elementos de página, imagens aleatórias sem contexto, fanarts, etc.)
