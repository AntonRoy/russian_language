from flask import *
import os
import random
app = Flask(__name__)
tech = ['Абсцисса,', 'Аддитивность,', 'Логистическая регрессия,', 'Линейная регрессия,', 'Аксонометрия,', 'Асимптота,', 'Бином,', 'Деференты,', 'Дистрибутивность,', 'Дифференциал,', 'Скаляр,', 'Итерация,', 'Логарифм,', 'Мультипликативность,Нормаль,', 'Нормальное распределение,', 'Рекуррентный,', 'Квантовая механика,', 'Нейтрон,', 'Спектр,', 'Фаза,', 'Фотон,', 'Векторный потенциал,', 'Пассивная инертность,', 'Производная,']
gum = ['Антитеза,', 'Хронотоп,', 'Аспект,', 'Дескрипция,', 'Эпитет,', 'Метафора,', 'Гиперболa,', 'Лингвистика,', 'Морфология,', ',Риторика,', 'Просвещение,', 'Романтизм,', 'Борроко,', 'Возрождение,', 'аллод,', 'оммаж,', 'социализация,', 'индустриализация,', 'геронтократия,', 'нуменклатура,']

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        try:
            type = request.form['tg']
            cmt1 = request.form['cmt1']
            cmt2 = request.form['cmt2']
        except:
            return render_template("main.html",
                                   error="Пожалуйста, заполните форму полностью!=)",
                                   tech=random.choice(tech)[:-1],
                                   gum=random.choice(gum)[:-1])
        if (not cmt1) or (not cmt2):
            return render_template("main.html",
                                   error="Пожалуйста, заполните форму полностью!=)",
                                   tech=random.choice(tech)[:-1],
                                   gum=random.choice(gum)[:-1])
        read = open("DATA.txt", "r")
        previous_data = read.read()
        read.close()
        fout = open("DATA.txt", "w")
        fout.write(previous_data + "\n{0} {1} {2}".format(type, cmt1, cmt2))
        fout.close()
        return render_template("thanks.html")
    return render_template("main.html", tech=random.choice(tech)[:-1], gum=random.choice(gum)[:-1])
app.secret_key = os.urandom(24)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)