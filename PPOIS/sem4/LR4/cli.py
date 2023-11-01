import random
from Models.Garden.field import Field, FieldAction
from Models.Garden.garden import BaseGarden
from Models.Plants.trees import OrangeTree, PearTree, Orange, Pear, Plum, PlumTree
from Models.Plants.vegetables import Tomato, Potato, Cucumber
from Controllers.print_garden import print_garden
from Models.Plants.seeds import PearSeed, PlumSeed, AppleSeed
from Models.serializers import write_state, load_state
from Views.arg_parser import parse

PLANT_COLLECTION = {
    'PearTree': PearTree,
    'AppleTree': OrangeTree,
    'Tomato': Tomato,
    'Cucumber': Cucumber,
    'Potato': Potato,
    'Apple': Orange,
    'Peach': Plum,
    'PearSeed': PearSeed,
    'PlumSeed': PlumSeed,
    'AppleSeed': AppleSeed,
    'Pear': Pear,
}

field_collection = [
    Field(OrangeTree()),
    Field(PearTree()),
    Field(Tomato()),
    Field(Potato()),
    Field(Cucumber()),
    Field(PlumTree()),
    Field(PlumSeed()),
    Field(PearSeed()),
    Field(AppleSeed()),
]


def main():
    args = parse()
    if args.init:
        garden = BaseGarden(random.choices(field_collection, k=5))
    else:
        garden = load_state()

    if args.show:
        print_garden(garden)
        raise SystemExit
    elif args.nextday:
        garden.next_day()
    elif args.hydrate:
        FieldAction(garden.fields[args.hydrate - 1]).hydrate_field()
    elif args.heal:
        FieldAction(garden.fields[args.heal - 1]).fertilizing()
    elif args.desinfect:
        FieldAction(garden.fields[args.desinfect - 1]).desinfect_plant()
    elif args.killplant:
        FieldAction(garden.fields[args.killplant - 1]).kill_plant()
    elif args.weeding and args.plant:
        plant = PLANT_COLLECTION.get(args.plant)
        FieldAction(garden.fields[args.weeding - 1]).weeding(plant())
    elif args.plant:
        plant = PLANT_COLLECTION.get(args.plant)()
        garden.fields.append(Field(plant))
        garden.fields[-1].weed = None
        garden.fields[-1].plant = plant

    print_garden(garden)
    write_state(garden)


if __name__ == '__main__':
    main()
