import tcod
import copy
from engine import Engine
from input_handlers import EventHandler
from entity import Entity
from procgen import generate_dungeon
import entity_factories


def main() -> None:
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45
    room_max_size = 12
    room_min_size = 5
    max_rooms = 20
    max_mons_in_room = 2

    tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    player = copy.deepcopy(entity_factories.player)
  
    game_map = generate_dungeon(max_rooms=max_rooms, room_min_size=room_min_size, room_max_size=room_max_size, map_width=map_width, map_height=map_height, max_mons_in_room=max_mons_in_room, player=player)
    engine = Engine(event_handler = event_handler, game_map = game_map, player = player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Rogue Adventures",
        vsync=True,
    ) as context:
        
        root_console = tcod.console.Console(screen_width, screen_height, order='F')
        while True:
            engine.render(console = root_console, context = context)
            events = tcod.event.wait()
            engine.handle_events(events)

    
if __name__ == "__main__":
    main()