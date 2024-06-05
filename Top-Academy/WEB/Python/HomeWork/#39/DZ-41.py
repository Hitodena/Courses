from jinja2 import Template

menu = [
    {"id": "index", "title": "Главная"},
    {"id": "news", "title": "Новости"},
    {"id": "about", "title": "О компании"},
    {"id": "shop", "title": "Магазин"},
    {"id": "contacts", "title": "Контакты"}
]

link = """
<ul>
    {% for el in menu %}
        {% if el.title == "Главная" -%}
            <li><a href="/{{ el.id }}" class="active">{{ el.title }}</a></li>
        {% else -%}
            <li><a href="/{{ el.id }}">{{ el.title }}</a></li>
        {% endif -%}
    {% endfor %}
</ul>
"""
tm = Template(link)
msg = tm.render(menu=menu)

print(msg)
