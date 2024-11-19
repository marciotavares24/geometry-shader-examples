# Geometry Shader Examples in OpenGL
Here we have some scripts to show what we can do with geometry shaders in OpenGL.

## Structure
The project is divided into 2 folders and 4 scripts:
- `objects/`: Contains the objects in obj format.
- `shaders/`: Contains the shaders used in the project, each one in a different folder.
    - `basic/`: Contains the basic shaders to render the objects.
    - `pass_through/`: Contains the shaders of the pass-through example, where the different geometry shaders just pass the vertices through.
    - `houses/`: Contains the shaders of the houses example, where the geometry shader creates a house for each vertex.
    - `wireframe/`: Contains the shaders of the wireframe example, where the geometry shader creates a wireframe of the object.
    - `normals/`: Contains the shaders of the normals example, where the geometry shader creates lines that represent the normals of the object vertices.
    - `explode/`: Contains the shaders of the explode example, where the geometry shader moves the vertices of the object in the direction of the normal.
    - `pyramids/`: Contains the shaders of the pyramids example, where the geometry shader creates a pyramid for each triangle of the object.
- `vertices.py`: Contains the vertices of the objects that will be rendered (points, star_lines, cube, sphere and skull).
- `geometric_object.py`: Contains the class that represents the geometric objects. It has methods needed to send information to the GPU and render the specific object.
- `renderer.py`: Contains the class that represents the renderer. It has methods to initialize the window, the shaders, add/remove objects and render them.
- `main.py`: Contains the main script that will run the project. Has a function to each example.

## How to run the script
To run the script, you need to have some modules installed.
```bash
pip install -r requirements.txt
```

Then, you can run the script with the following command:
```bash
python main.py <example>
```

Where `<example>` is the name (or number) of the example you want to run. The available examples are:
- `1` / `pass_through` (default)
- `2` / `houses`
- `3` / `wireframe`
- `4` / `normals`
- `5` / `explode`
- `6` / `pyramids`

## What files to look at?
Fill free to look and modify any file you want.

To complete the examples you can look at the following files:
- Everything in the `shaders/` folder (especially the geometry shaders)
- `main.py` to see how the examples are called, change the objects or even to change what shaders are used in each example.

# That's it!
I hope you enjoy solving the examples and learn something new with them.
