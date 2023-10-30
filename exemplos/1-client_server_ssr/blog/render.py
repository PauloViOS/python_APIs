from database import conn
from pathlib import Path

# O objetivo dessa técnica é não precisar gerar todos os htmls que serão
# servidos, mas sim definir um template a partir do qual os htmls de cada página
# serão serão gerados. Isso "automatiza" a criação de páginas, uma vez que apenas
# precisamos fornecer os dados com os quais queremos gerar uma página

# 1 - Obtém os dados
cursor = conn.cursor()
fields = ("id", "title", "content", "author")
results = cursor.execute("SELECT * FROM post;")
posts = [dict(zip(fields, post)) for post in results]

# 2 - Cria a pasta de destino do site
site_dir = Path("site")
site_dir.mkdir(exist_ok=True)

# 3 - Cria uma função para gerar a URL com slug
def get_post_url(post):
    slug = post["title"].lower().replace(" ", "-")
    return f"{slug}.html"

# 4 - Renderiza a página index.html
index_template = Path("list.template.html").read_text()
index_page = site_dir / Path("index.html")
post_list = [
    f"<li><a href='{get_post_url(post)}'>{post['title']}</a></li>"
    for post in posts
]
index_page.write_text(
    index_template.format(post_list="\n".join(post_list))
)

# 5 - Renderizar as páginas do blog
for post in posts:
    post_template = Path("post.template.html").read_text()
    post_page = site_dir / Path(get_post_url(post))
    post_page.write_text(
        post_template.format(post=post)
    )

conn.close()

print("Site created!")
