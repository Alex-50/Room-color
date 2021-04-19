from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/table/<sex>/<int:age>')
def index(sex, age):
    return render_template("index.html", title="Цвет каюты", sex=sex, age=age)


if __name__ == '__main__':
    app.run()
