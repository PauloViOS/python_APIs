#!/usr/bin/env python3.11
import cgi
form = cgi.FieldStorage()
nome = form.getvalue("nome")
mensagem = form.getvalue("mensagem")

# Um dos problemas do cgi é que, ao apontar para esse
# arquivo, ele está o expondo para o mundo sem
# proteção alguma e expondo seu código-fonte! Esse é
# um dos motivos de protocolos adicionais terem sido
# implementados por cima dele

# O script precisa de um shebang para indicar que interpretador deve executar o script
# Aqui vai ser o próprio interpretador que estivermos usando, mas em um servidor que tenha um Apache ou um NGinx é bom que isso seja especificado

# Além disso, ele também precisa de permissão de execução
# rodar um chmod +x cgi-bin/envia.py

# aqui podemos fazer qualquer tipo de validação das infos do form
# O importante é que daqui para frente as mensagens sejam criadas em formato de stream
# ou seja, não será criada uma string html gigantesca. O cgi trabalha recebendo um iterável.
# O cgi substituirá o standard output pelo seu stream de dados, fazendo com que as mensagens impressas por um print sejam mostradas no navegador

# Vamos enviar o conteúdo da resposta em diversos prints separados para emular o comportamento padrão do cgi
# É montada uma response em pedaços iteráveis que são consumidos um de cada vez
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Enviado</title>")
print("</head>")
print("<body>")
print("<h1>Enviado com sucesso!</h1>")
print(f"<h2>{nome} - {mensagem}</h2>")
print("</body>")
print("</html>")

# Ao iniciar o servidor, devemos colocar a flag --cgi para indicar que estamos usando esse protocolo