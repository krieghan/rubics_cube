import optparse

from rubics_cube import canvas

def run():
    world = canvas.RubicsCubeWorld(height=100000,
                               width=100000)
    escape_canvas = canvas.EscapeCanvas(world=world)
    escape_canvas.start()


if __name__ == "__main__":
    run()

