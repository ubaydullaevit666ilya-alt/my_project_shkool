import os

def create_project_structure():
    # 1. Создаем папки
    os.makedirs("templates", exist_ok=True)
    os.makedirs("static/css", exist_ok=True)

    # 2. Создаем файлы шаблонов (HTML)
    
    base_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Моя Школа Программирования{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <h1><a href="/">Моя Школа Программирования</a></h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2026 | Создано с помощью Gemini Code Assist</p>
    </footer>
</body>
</html>"""

    index_html = """{% extends "base.html" %}

{% block title %}Все уроки{% endblock %}

{% block content %}
    <h2>Список доступных уроков</h2>
    <ul class="lesson-list">
        {% for id, lesson in lessons.items() %}
            <li><a href="{{ url_for('lesson', lesson_id=id) }}">{{ lesson.title }}</a> <span class="author">(от {{ lesson.author }})</span></li>
        {% endfor %}
    </ul>
{% endblock %}"""

    lesson_html = """{% extends "base.html" %}

{% block title %}{{ lesson.title }}{% endblock %}

{% block content %}
    <h2>{{ lesson.title }}</h2>
    <p class="author">Автор: {{ lesson.author }}</p>
    <div class="lesson-content">{{ lesson.content }}</div>
{% endblock %}"""

    # 3. Создаем файл стилей (CSS)
    style_css = """body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    background-color: #f4f4f4;
    color: #333;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1rem 0;
    text-align: center;
}

header a {
    color: #fff;
    text-decoration: none;
}

main {
    max-width: 800px;
    margin: 2rem auto;
    padding: 0 2rem;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    padding: 20px;
}

.lesson-list li {
    list-style: none;
    padding: 10px;
    border-bottom: 1px solid #eee;
}

footer {
    text-align: center;
    margin-top: 2rem;
    color: #777;
}"""

    # Записываем файлы
    with open("templates/base.html", "w", encoding="utf-8") as f:
        f.write(base_html)
    
    with open("templates/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    with open("templates/lesson.html", "w", encoding="utf-8") as f:
        f.write(lesson_html)

    with open("static/css/style.css", "w", encoding="utf-8") as f:
        f.write(style_css)

    print("Успешно! Папки созданы, файлы разложены по местам.")

if __name__ == "__main__":
    create_project_structure()