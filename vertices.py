from geometric_object import GeometricObject

# Points vertices
points = [
    # [x, y, z, nx, ny, nz, r, g, b, a]
    # left column (red, green, blue)
    [1, -1, 0, 0, 0, 1, 1, 0, 0, 1],
    [1,  0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1,  1, 0, 0, 0, 1, 0, 0, 1, 1],
    
    # right column (blue, green, red)
    [-1, -1, 0, 0, 0, 1, 0, 0, 1, 1],
    [-1,  0, 0, 0, 0, 1, 0, 1, 0, 1],
    [-1,  1, 0, 0, 0, 1, 1, 0, 0, 1],
]

# Star vertices
star_lines = [
    # [x, y, z, nx, ny, nz, r, g, b, a]
    # bottom left -> top
    [-0.75, -1, 0, 0, 0, 1, 1, 1, 0, 1],
    [    0,  1, 0, 0, 0, 1, 1, 1, 0, 1],

    # top -> bottom right
    [   0,  1, 0, 0, 0, 1, 1, 1, 0, 1],
    [0.75, -1, 0, 0, 0, 1, 1, 1, 0, 1],

    # bottom right -> left
    [0.75,   -1, 0, 0, 0, 1, 1, 1, 0, 1],
    [  -1, 0.25, 0, 0, 0, 1, 1, 1, 0, 1],

    # left -> right
    [-1, 0.25, 0, 0, 0, 1, 1, 1, 0, 1],
    [ 1, 0.25, 0, 0, 0, 1, 1, 1, 0, 1],

    # right -> bottom left
    [    1, 0.25, 0, 0, 0, 1, 1, 1, 0, 1],
    [-0.75,   -1, 0, 0, 0, 1, 1, 1, 0, 1],
]

# Cube vertices
cube = [
    # [x, y, z, nx, ny, nz, r, g, b, a]
    # front face = color red + normal pointing towards the camera
    [-1, -1, 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1, -1, 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1,  1, 1, 0, 0, 1, 1, 0, 0, 1],

    [ 1,  1, 1, 0, 0, 1, 1, 0, 0, 1],
    [-1,  1, 1, 0, 0, 1, 1, 0, 0, 1],
    [-1, -1, 1, 0, 0, 1, 1, 0, 0, 1],

    # top face = color yellow (red + green) + normal pointing upwards
    [-1, 1,  1, 0, 1, 0, 1, 1, 0, 1],
    [ 1, 1,  1, 0, 1, 0, 1, 1, 0, 1],
    [ 1, 1, -1, 0, 1, 0, 1, 1, 0, 1],

    [ 1, 1, -1, 0, 1, 0, 1, 1, 0, 1],
    [-1, 1, -1, 0, 1, 0, 1, 1, 0, 1],
    [-1, 1,  1, 0, 1, 0, 1, 1, 0, 1],

    # bottom face = color purple (red + blue) + normal pointing downwards
    [-1, -1, -1, 0, -1, 0, 1, 0, 1, 1],
    [ 1, -1, -1, 0, -1, 0, 1, 0, 1, 1],
    [ 1, -1,  1, 0, -1, 0, 1, 0, 1, 1],

    [ 1, -1,  1, 0, -1, 0, 1, 0, 1, 1],
    [-1, -1,  1, 0, -1, 0, 1, 0, 1, 1],
    [-1, -1, -1, 0, -1, 0, 1, 0, 1, 1],  

    # left face = color blue + normal pointing left
    [-1,  1,  1, -1, 0, 0, 0, 0, 1, 1],
    [-1, -1, -1, -1, 0, 0, 0, 0, 1, 1],
    [-1, -1,  1, -1, 0, 0, 0, 0, 1, 1],

    [-1,  1,  1, -1, 0, 0, 0, 0, 1, 1],
    [-1,  1, -1, -1, 0, 0, 0, 0, 1, 1],
    [-1, -1, -1, -1, 0, 0, 0, 0, 1, 1],

    # right face = color green + normal pointing right
    [1,  1, -1, 1, 0, 0, 0, 1, 0, 1],
    [1, -1,  1, 1, 0, 0, 0, 1, 0, 1],
    [1, -1, -1, 1, 0, 0, 0, 1, 0, 1],

    [1,  1, -1, 1, 0, 0, 0, 1, 0, 1],
    [1,  1,  1, 1, 0, 0, 0, 1, 0, 1],
    [1, -1,  1, 1, 0, 0, 0, 1, 0, 1],  

    # back face = color cyan (green + blue) + normal pointing away from the camera
    [-1,  1, -1, 0, 0, -1, 0, 1, 1, 1],
    [ 1, -1, -1, 0, 0, -1, 0, 1, 1, 1],
    [-1, -1, -1, 0, 0, -1, 0, 1, 1, 1],

    [-1,  1, -1, 0, 0, -1, 0, 1, 1, 1],
    [ 1,  1, -1, 0, 0, -1, 0, 1, 1, 1],
    [ 1, -1, -1, 0, 0, -1, 0, 1, 1, 1]
]

# Sphere vertices (from an .obj file)
sphere = GeometricObject.vertices_from_obj("objects/sphere.obj", color=[0, 1, 0, 0.75])

# Skull vertices (from an .obj file)
skull = GeometricObject.vertices_from_obj("objects/skull.obj", color=[1, 0, 0, 0.75])
