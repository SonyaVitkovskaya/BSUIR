import json
from Models.Plants.weed import Weed
from Models.Garden.field import  Field
from Models.Plants.seeds import PearSeed, PlumSeed, AppleSeed
from Models.Garden.garden import BaseGarden
from Models.Plants.vegetables import Tomato, Potato, Cucumber
from Models.Plants.trees import *

PLANT_COLLECTION = {
    'Pear Tree': PearTree,
    'Orange Tree': OrangeTree,
    'Plum Tree': PlumTree,
    'Tomato': Tomato,
    'Cucumber': Cucumber,
    'Potato': Potato,
    'Orange': Orange,
    'Peach': Plum,
    'PearSeed': PearSeed,
    'PlumSeed': PlumSeed,
    'AppleSeed': AppleSeed,
    'Pear': Pear,
}


def write_state(garden):
    data = {'weather': garden.WEATHER.__dict__, 'fields': field_serializer(garden.fields)}
    with open('./state.json', 'w') as f:
        json.dump(data, f, indent=4)


def field_serializer(field_list: list[Field]) -> list[dict]:
    data = []
    for i in range(len(field_list)):
        if field_list[i].plant and field_list[i].plant.dead:
            continue
        item = {'field_pk': i,
                'weed': bool(field_list[i].weed),
                'tree': True if hasattr(field_list[i].plant, 'fruit') else False,
                'seed': True if hasattr(field_list[i].plant, 'ready_plant') else False,
                }
        if not item['weed']:
            item.update({
                'plant': str(field_list[i].plant),
                'health': field_list[i].plant.health,
                'hydration_level': field_list[i].plant.hydration_level,
                'age': field_list[i].plant.age,
                'pests_damage': field_list[i].plant.pests.destruction_power,
                'illness_damage': field_list[i].plant.illness.destruction_power,
            })
            if item['tree'] and field_list[i].plant.fruit:
                item.update({'fruit': str(field_list[i].plant.fruit)})
            if item['seed'] and field_list[i].plant.ready_plant:
                item.update({'seed_plant': str(field_list[i].plant.ready_plant)})
        data.append(item)
    return data


def load_state():
    fields = []
    with open('./state.json', 'r') as f:
        data = json.load(f)
        for data_field in data['fields']:
            weed = Weed() if data_field.get('weed') else None
            if data_field.get('plant', False):
                print(data_field['plant'])
                Plant = PLANT_COLLECTION.get(data_field['plant'], None)
                plant = Plant(
                    age=data_field.get('age'),
                    health=data_field.get('health'),
                    hydration_level=data_field.get('hydration_level')
                )
                plant.pests.destruction_power = data_field.get('pests_damage')
                plant.illness.destruction_power = data_field.get('illness_damage')
                field = Field(plant)
                field.weed = weed
                field.plant = plant
                fruit = data_field.get('fruit', None)
                if fruit:
                    field.plant.fruit = PLANT_COLLECTION.get(fruit)()
                ready_plant = data_field.get('ready_plant', None)
                if ready_plant:
                    field.plant.ready_plant = PLANT_COLLECTION.get(ready_plant)()
            else:
                field = Field(None)
                field.weed = weed
            fields.append(field)

    garden = BaseGarden(fields)
    return garden
