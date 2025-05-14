from __future__ import annotations

import attrs
import tcod.console
import tcod.context
import tcod.event
import tcod.tileset


@attrs.define()
class ExampleState:
    """Example state with a hard-coded player position."""

    player_x: int
    """Player X position, left-most position is zero."""
    player_y: int
    """Player Y position, top-most position is zero."""

    def on_draw(self, console: tcod.console.Console) -> None:
        """Draw the player glyph."""
        console.print(self.player_x, self.player_y, "@")


def main() -> None:
    # creating a window and loading tileset
    font_tileset = tcod.tileset.load_tilesheet(
        "data/alloy_curses.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
        )
    tcod.tileset.procedural_block_elements(tileset=font_tileset)
    
    # setting window console
    console = tcod.console.Console(64, 48)
    # console.print(0, 0, "Hello World") # x, y, text
    state = ExampleState(player_x=console.width // 2, player_y=console.height // 2)
    
    with tcod.context.new(console = console , tileset=font_tileset) as context:
        while True: # main loop
            console.clear()  # Clear the console before any drawing
            state.on_draw(console)  # Draw the current state
            context.present(console)  # Display the console on the window
            # context.present(console)
            for event in tcod.event.wait():
                print(event)
            
            # demo check
            if isinstance(event, tcod.event.Quit):
                raise SystemExit
            
        pass # end window here


if __name__ == "__main__":
    main()