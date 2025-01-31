from PIL import Image
import json

'''/
with open('crafting_items.json', 'r') as f:
    raw_data = f.read()
    data = json.loads(raw_data)

common_item_colour = (36, 34, 33)
rare_item_colour = (102, 75, 28)

temp_image = Image.new(mode='RGB', size=(80, 80), color=common_item_colour)


for name in data.keys():
    temp_image.save('static/img/items/' + name + '_bg.png')

'''

