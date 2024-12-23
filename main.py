import tcod


def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Rogue Adventures",
        vsync=True,
    ) as context:
    
if __name__ == "__main__":
    main()