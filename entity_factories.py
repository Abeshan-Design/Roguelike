from entity import Entity

player = Entity(char="@", color=(255, 255, 255), name="Player", blocks_movement=True)

slime = Entity(char="s", color=(0, 255, 0), name="Slime", blocks_movement=True)
goblin = Entity(char="g", color=(150, 75, 0), name="Goblin", blocks_movement=True)