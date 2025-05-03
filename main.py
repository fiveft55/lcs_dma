from __future__ import annotations

import tcod.context
import tcod.tileset


def main() -> None:
    # creating a window and loading tileset
    font_tileset = tcod.tileset.load_tilesheet(
        "data/alloy_curses.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
        )
    tcod.tileset.procedural_block_elements(tileset=font_tileset)
    with tcod.context.new(tileset=font_tileset) as context:
        pass # opening a window here


if __name__ == "__main__":
    main()