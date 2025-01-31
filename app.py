import json
from flask import Flask, render_template
from operator import itemgetter

app = Flask(__name__)


@app.route('/')
def index():
    with open('map_areas.json', 'r') as f:
        data_areas = json.loads(f.read())
    return render_template('index.html', data_areas=data_areas)


@app.route('/crafting')
def crafting():
    with open('crafting_items.json', 'r') as f:
        json_data_items = json.load(f)
    with open('crafting_items.json', 'r') as f:
        raw_data_items = f.read()

        data_items = dict(sorted((json.loads(raw_data_items)).items(), key=itemgetter(1)))

    with open('crafting_recipes.json', 'r') as f:
        raw_data_recipes = f.read()
    with open('crafting_recipes.json', 'r') as f:
        json_data_recipes = json.load(f)
        data_recipes = json.loads(raw_data_recipes)

    return render_template('crafting.html', data_items=data_items, data_recipes=data_recipes, json_data_items=json_data_items, json_data_recipes=json_data_recipes)


@app.route('/tips')
def tips():
    tips_dict = dict()
    with open('static/text/tips.txt', 'r') as f:
        got_name = False
        tip_text = ''
        tip_name = ''

        for line in f:
            if not got_name:  # Если для текущей подсказки еще нет имени
                tip_name = line[:-1]
                got_name = True

            else:
                if line and (line != '\n'):  # Если имя уже есть - считываем строки до пустой строки или конца файла
                    tip_text += (line[:-1] + ' ')
                else:
                    tips_dict[tip_name] = tip_text
                    tip_text = ''
                    got_name = False

        tips_dict[tip_name] = tip_text

    return render_template('tips.html', tips_dict=tips_dict)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/builds')
def builds():
    return render_template('builds.html')




if __name__ == '__main__':
    app.run()
