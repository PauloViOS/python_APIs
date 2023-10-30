import socket

# A implementação de um server é, a princípio, igual a de um client.
# Também usa um socket com as mesmas configurações.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Ao invés de usar um método send, usamod um bind, que vai unir o serviço
# com uma porta tcp e uma interface de rede
server.bind(("localhost", 9000))
# A partir do momento que o serviço está conectado à porta, um descritor
# do seocket é criado no linux. Precisamos então chamar um método listen, 
# que vai fazer com que o socket passe a ouvir conexões externas.
server.listen()

# Vamos manter o servdor aberto para requisições enquanto não ocorrer um
# erro. Assim, podemos definir que com qualquer exceção, inclusive
# um Ctrl + C, o servidor seja interrompido.
try:
    # mantendo o servidor sempre aberto para requisições
    while True:
        # Vamos aceitar qualquer requisição. O método nos retorna uma
        # tupla com dados sobre o client e seu endereço
        client, address = server.accept()
        
        # Request
        # Leremos payloads com até 5k bytes. O payload é
        # todo o corpo da requisição, desde o verbo até o fim.
        data = client.recv(5000).decode()
        print(f"{data=}")

        # Response
        # se usássemos o send, teríamos que enviar separadamente um
        # aviso de que a conexão está começando, depois os cabeçalhos
        # e depois o restante
        # Com o sendall podemos enviar tudo junto
        client.sendall(
            "HTTP/1.0 200 OK\r\n\r\n<html><body>Hello</dody></html>\r\n\r\n".encode()
        )
        # por fim, vamos dar um shutdown pq cada request tem um tempo
        # de vida limitado. O client faz uma request e obtém um response.
        # Caso queira fazer uma nova request, deve criar uma nova instância.
        # O shutdown deve receber um signal, que nesse caso será SHUT_WR
        client.shutdown(socket.SHUT_WR)

except Exception:
    server.close()


# Esse servidor aceita qualquer requisição de qualquer rota que
# o client pedir. Em um servidor real deveria haver um parse,
# depois uma busca do rescurso pedido, etc
# Os frameworks abstraem essa parte de nós


# O python já tem um servidor embutido o http.server
# Para rodá-lo, basta fazer python -m http.server --directory {nome do diretório a ser servido}
# Experimente fazer isso e abrir no browser localhost:8000
# Se houver um arquivo index.html na pasta servida, ele será carregado
# sem necessidade de espscificar seu caminho. Caso contrário, o servidor
# listará os arquivos contidos na pasta

# Um servidor muito utilizado é o Nginx
# Podemos rodá-lo a partir de um container docker
# Para fazer isso, rodamos
# docker run --name docker-nginx -p 8000:80 -d -v "$PWD":/usr/share/nginx/html nginx
# Isso rodará o container com nginx dentro. Podemos acessar o nosso site através de localhost:8000
# da mesma forma, mas agora o nginx está interceptando essa request