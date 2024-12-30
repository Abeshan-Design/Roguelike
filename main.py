import tcod
import copy
from engine import Engine
from entity import Entity
from procgen import generate_dungeon
import entity_factories
import color

def main() -> None:
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 40
    room_max_size = 12
    room_min_size = 5
    max_rooms = 20
    max_mons_in_room = 2

    tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    player = copy.deepcopy(entity_factories.player)
    engine = Engine(player=player)
  
    engine.game_map = generate_dungeon(
        max_rooms=max_rooms, 
        room_min_size=room_min_size, 
        room_max_size=room_max_size, 
        map_width=map_width, 
        map_height=map_height,
        max_mons_in_room=max_mons_in_room, 
        engine=engine)
    engine.update_fov()
    engine.message_log.add_message(
        "Welcome to the dungeon! Attack enemies and become stronger", color.welcome_text)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Rogue Adventures",
        vsync=True,
    ) as context:
        
        root_console = tcod.console.Console(screen_width, screen_height, order='F')
        while True:
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)
            engine.event_handler.handle_events(context)
    
if __name__ == "__main__":
    main()