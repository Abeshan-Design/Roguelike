from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor, Item
from components.consumable import HealingConsumable
from components.inventory import Inventory

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=3, power=5),
    inventory=Inventory(capacity=26),
)

slime = Actor(
    char="s",
    color=(0, 255, 0),
    name="Slime",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=2),
    inventory=Inventory(capacity=0),
)
goblin = Actor(
    char="g",
    color=(150, 75, 0),
    name="Goblin",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=15, defense=1, power=5),
    inventory=Inventory(capacity=0),
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=HealingConsumable(amount=4),
)