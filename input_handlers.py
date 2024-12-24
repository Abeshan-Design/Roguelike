from typing import Optional
import tcod.event
from actions import Action, Escape, Movement



class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_UP:
            action = Movement(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = Movement(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = Movement(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = Movement(dx=1, dy=0)
        elif key == tcod.event.K_ESCAPE:
            action = Escape()


        return action