import pygame as pg
import sys

from renderer import *
from geometric_object import *
import vertices

# Create a GeometricObject with the vertices
points = GeometricObject(vertices.points, GeometricType.POINTS, scale=[5, 5, 5])
star_lines = GeometricObject(vertices.star_lines, GeometricType.LINES, scale=[5, 5, 5])
cube = GeometricObject(vertices.cube, rotation=[45, 45, 0], scale=[1.5, 1.5, 1.5])
sphere = GeometricObject(vertices.sphere, position=[5, 5, 5], scale=[1.5, 1.5, 1.5])
skull = GeometricObject(vertices.skull, position=[-5, -5, -5], rotation=[-45, -45, 0], scale=[0.15, 0.15, 0.15])


# Use the geometry shader to pass through the outputs of the vertex shader to the fragment shader
def pass_through():
    # Shaders to use
    shaders_list = [(
        "shaders/basic/vertex.glsl", "shaders/pass_through/fragment.glsl",
        # Add the geometry shaders here (empty list to not use any)
        []
    )]

    # Objects to render (switch between them)
    object_list = [
        points,
        star_lines,
        cube,
        sphere,
        skull,
    ]

    return shaders_list, object_list


# Use the geometry shader to render 2D houses using points as input
def houses():
    # Shaders to use
    shaders_list = [(
        "shaders/basic/vertex.glsl", "shaders/basic/fragment_from_geometry.glsl",
        ["shaders/houses/geometry_points.glsl"]
    )]

    # Objects to render
    object_list = [points]

    return shaders_list, object_list


# Use the geometry shader to render the objects as wireframes
def wireframe():
    # Shaders to use
    shaders_list = [(
        "shaders/basic/vertex.glsl", "shaders/basic/fragment_from_geometry.glsl",
        ["shaders/wireframe/geometry_triangles.glsl"]
    )]

    # Objects to render (switch between them)
    object_list = [
        cube,
        # sphere,
        # skull,
    ]

    return shaders_list, object_list


# Use the geometry shader to render the normals of the objects
def normals():
    # Shaders to use (can comment the basic shader to see only the normals)
    shaders_list = [
        # Responsable for rendering the object
        ("shaders/basic/vertex.glsl", "shaders/basic/fragment_from_vertex.glsl", []),
        # Responsable for rendering the normals of the object
        (
            "shaders/basic/vertex.glsl", "shaders/basic/fragment_from_geometry.glsl",
            ["shaders/normals/geometry_triangles.glsl"]
        ),
    ]

    # Objects to render (switch between them)
    object_list = [
        cube,
        # sphere,
        # skull,
    ]

    return shaders_list, object_list


# Use the geometry shader to render a exploded object (aka moving the vertices along the normals)
def explode():
    # Shaders to use
    shaders_list = [(
        "shaders/basic/vertex.glsl", "shaders/basic/fragment_from_geometry.glsl",
        ["shaders/explode/geometry_triangles.glsl"]
    )]

    # Objects to render (switch between them)
    object_list = [
        cube,
        # sphere,
        # skull,
    ]

    return shaders_list, object_list


# Use the geometry shader to render every triangle as a pyramid
def pyramids():
    # Shaders to use
    shaders_list = [(
        "shaders/basic/vertex.glsl", "shaders/basic/fragment_from_geometry.glsl",
        ["shaders/pyramids/geometry_triangles.glsl"]
    )]

    # Objects to render
    object_list = [cube]

    return shaders_list, object_list


if __name__ == "__main__":
    # Map the examples names to the functions that run them
    example_map = {
        "pass_through": pass_through,
        "houses": houses,
        "wireframe": wireframe,
        "normals": normals,
        "explode": explode,
        "pyramids": pyramids,
        "1": pass_through,
        "2": houses,
        "3": wireframe,
        "4": normals,
        "5": explode,
        "6": pyramids,
    }

    # Parse argument to choose the example to run
    if len(sys.argv) >= 2:
        example = sys.argv[1].lower()
        example_to_run = example_map.get(example)

        # Check if the example is valid
        if example_to_run is None:
            print(f"\nInvalid example: {example}")

            # Print the available examples
            example_names = [key for key in example_map.keys() if not key.isnumeric()]
            print(f"Examples: {', '.join(example_names)}")
            sys.exit(1)
    else:
        # Default example
        example_to_run = pass_through


    # Create Camera
    camera = Camera([0, 0, -20])

    # Create a renderer and initialize pygame and OpenGL
    renderer = Renderer(camera)
    renderer.init_pygame_and_opengl()


    # Get shaders and objects to render
    shaders_list, object_list = example_to_run()

    # Initialize shaders
    for shaders in shaders_list:
        renderer.init_shaders(*shaders)

    # Add objects to the renderer
    for obj in object_list:
        renderer.add_object(obj)


    # Main loop
    clock = pg.time.Clock()
    running = True
    while running:
        clock.tick(60)
        running = renderer.process_events()
        renderer.render()

    # Clean up and quit
    renderer.cleanup()
