from __future__ import annotations

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset


def main() -> None:
    # creating a window and loading tileset
    font_tileset = tcod.tileset.load_tilesheet(
        "data/alloy_curses.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
        )
    tcod.tileset.procedural_block_elements(tileset=font_tileset)
    
    # setting window console
    console = tcod.console.Console(80, 50)
    console.print(0, 0, "Hello World") # x, y, text
    
    with tcod.context.new(tileset=font_tileset) as context:
        while True: # main loop
            context.present(console)
            for event in tcod.event.wait():
                print(event)
            
            # demo check
            if isinstance(event, tcod.event.Quit):
                raise SystemExit
            
        pass # end window here


if __name__ == "__main__":
    main()