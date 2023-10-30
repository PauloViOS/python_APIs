# Server side rendering
# É simplesmente a capacidade de gerar o html que
# vai ser trafegado via HTTP de forma dinâmica usando
# as features da linguagem sendo utilizada

# carregar os dados
dados = [
    {"nome": "Paulo", "cidade": "Taboão"},
    {"nome": "Julyane", "cidade": "Friburgo"}
]

# processar os dados
template = """\
<html>
    <body>
        <ul>
            <li> Nome: {dados[nome]} </li>
            <li> Cidade: {dados[cidade]} </li>
        </ul>
    </body>
</html>
"""

# renderizar
for item in dados:
    print(template.format(dados=item))