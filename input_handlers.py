from typing import Optional
import tcod.event
from actions import Action, Escape, Movement



class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    