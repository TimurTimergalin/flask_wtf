from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def base(title):
    if not title:
        title = 'title'
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    eng_train = '..' + url_for('static', filename='img/eng_train.jpg')
    print(eng_train)
    sci_simul = '..' + url_for('static', filename='img/sci_simul.png')
    print(sci_simul)
    return render_template('training.html', prof=prof.lower(), eng_train=eng_train, sci_simul=sci_simul)


@app.route('/list_prof/<lst>')
def list_prof(lst):
    prof_list = ['инженер-исследователь',
                 'пилот',
                 'строитель',
                 'экзобиолог',
                 'врач',
                 'инженер по терраформированию',
                 'климатолог',
                 'специалист по радиационной защите',
                 'астрогеолог',
                 'гляциолог',
                 'инженер жизнеобеспечения',
                 'метеоролог',
                 'оператор марсохода',
                 'киберинженер',
                 'штурман',
                 'пилот дронов']
    return render_template('list_prof.html', lst=lst, prof_list=prof_list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    kwargs = {
        'title': 'Отправленная форма',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': True,
        'css_link': url_for('static', filename='css/auto_answer.css')
    }
    return render_template('auto_answer.html', **kwargs)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')