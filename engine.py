from typing import Iterable, Any
from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov
from entity import Entity
from input_handlers import EventHandler
from game_map import GameMap

class Engine:
    def __init__(self, event_handler: EventHandler, game_map: GameMap, player: Entity):
        
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player
        self.update_fov()
    
    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)
            self.update_fov()

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)
        

        context.present(console)
        console.clear()

    def update_fov(self) -> None:
        self.game_map.visible[:] = compute_fov(self.game_map.tiles['transparent'],(self.player.x, self.player.y), radius = 4)
        self.game_map.explored |= self.game_map.visible
