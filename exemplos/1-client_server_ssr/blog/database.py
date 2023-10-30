# 1 - Conecta com o banco
from sqlite3 import connect

conn = connect("blog.db")
# Cursor é um objeto utiizado para navegar na tabela
cursor = conn.cursor()

# 2 - Define e cria a tabela
# Connection somente executa queries de DDL
conn.execute(
    """\
    CREATE TABLE if not exists post (
        id integer PRIMARY KEY AUTOINCREMENT,
        title varchar UNIQUE NOT NULL,
        content varchar NOT NULL,
        author varchar NOT NULL
    );
    """    
)

# 3 - Cria posts iniciais para popular banco
posts = [
    {
        "title": "Python é eleita a linguagem mais popular",
        "content": """\
        A linguagem Python foi eleita a linguagem mais popular pela revista
        tech masters e segue dominando o mundo
        """,
        "author": "Satoshi Namamoto"
    },
    {
        "title": "Como criar um blog usando Python",
        "content": """\
        Vamos aprender a criar um blog usando Python
        <pre> import make_a_blog </pre>
        """,
        "author": "Guido Van Rossum"
    }
]

# 4 - Insere os posts caso o banco esteja vazio
count = cursor.execute("SELECT * FROM post;").fetchall()
if not count :
    # Como vamos inserir dados na tabela (DML) a query é executada pelo cursor
    cursor.executemany(
        """\
        INSERT INTO post (title, content, author)
        VALUES (:title, :content, :author);
        """,
        posts
    )
    conn.commit()

# 5 - Verificando se deu certo
posts = conn.execute("SELECT * FROM post;").fetchall()
assert len(posts) >= 2
