from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Таблица студентов</title>
</head>
<body>
    <h1>Список студентов</h1>

    <table border="1" cellpadding="10">
        <tr>
            <th>Имя</th>
            <th>Предмет</th>
            <th>Оценка</th>
        </tr>
        {% for student in students %}
        <tr>
            <td>{{ student.name }}</td>
            <td>{{ student.subject }}</td>
            <td>{{ student.grade }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/")
def index():
    students = [
        {"name": "Анна", "subject": "Математика", "grade": 5},
        {"name": "Иван", "subject": "Информатика", "grade": 4},
        {"name": "Мария", "subject": "Физика", "grade": 5},
        {"name": "Петр", "subject": "История", "grade": 3}
    ]
    return render_template_string(HTML, students=students)


if __name__ == "__main__":
    app.run(debug=True)
