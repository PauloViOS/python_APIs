import socket
#############################################################
###### EXEMPLO USANDO UMA CONEXÃO A UM SERVIDOR EXTERNO #####
#############################################################
# # definindo um socket com ipv4 configurado para stream de texto
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # abrindo socket para ouvir conexões definindo o domínio e a porta (80 é padrão para web)
# client.connect(("example.com", 80))

# # cria a requisição definindo o verbo, a URL e o protocolo
# # Deixa linhas em branco no fim pq é o padrão
# # Encode no final para transformar de UTF-8 para bytes
# cmd = "GET http://example.com/index.html HTTP/1.0\r\n\r\n".encode()

# # Manda o comando para o servidor
# client.send(cmd)

# while True:
#     # Faz com que sejam lidos apenas 512 bytes por vez
#     data = client.recv(512)
#     if len(data) < 1:
#         break
#     # Transforma de bytes para UTF-8 e junta os chunks
#     print(data.decode(), end="")

# client.close()

#########################################################################
###### EXEMPLO USANDO UMA CONEXÃO AO SERVIDOR DEFINIDO EM SERVER.PY #####
#########################################################################
# definindo um socket com ipv4 configurado para stream de texto
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# abrindo socket para ouvir conexões definindo o domínio e a porta (80 é padrão para web)
client.connect(("localhost", 9000))

# cria a requisição definindo o verbo, a URL e o protocolo
# Deixa linhas em branco no fim pq é o padrão
# Encode no final para transformar de UTF-8 para bytes
cmd = "GET http://localhost/index.html HTTP/1.0\r\n\r\n".encode()

# Manda o comando para o servidor
client.send(cmd)

while True:
    # Faz com que sejam lidos apenas 512 bytes por vez
    data = client.recv(512)
    if len(data) < 1:
        break
    # Transforma de bytes para UTF-8 e junta os chunks
    print(data.decode(), end="")

client.close()