from OpenGL.GL import *
import OpenGL.error
import numpy as np
import glm
import pywavefront as wf

from enum import Enum

class GeometricType(Enum):
    TRIANGLES = GL_TRIANGLES
    POINTS = GL_POINTS
    LINES = GL_LINES

class GeometricObject:
    def __init__(self, vertices, geometry_type=GeometricType.TRIANGLES, position=[0, 0, 0], rotation=[0, 0, 0], scale=[1, 1, 1]):
        # vertices = list of [x, y, z, nx, ny, nz, r, g, b, a] for each vertex
        # geometry_type = type of geometry to render (default is TRIANGLES) 
        self.vertices = np.array(vertices, dtype=np.float32)
        self.geometry_type = geometry_type
        self.vbo = None

        # Transformation properties and model matrix
        self.position = position
        self.rotation = rotation
        self.scaling = scale
        self.model = np.identity(4, np.float32)

        # Flag to check if object has changed
        self.changed = True


    def set_vbo(self):
        # Create VBO and send data to GPU
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, 4 * self.vertices.size, self.vertices, GL_STATIC_DRAW)
    
    def compute_model_matrix(self):
        self.model = np.identity(4, np.float32)

        # Calculate the model matrix based on position, rotation, and scale properties
        self.model = glm.translate(self.model, glm.vec3(self.position))
        self.model = glm.rotate(self.model, glm.radians(self.rotation[0]), glm.vec3(1, 0, 0))
        self.model = glm.rotate(self.model, glm.radians(self.rotation[1]), glm.vec3(0, 1, 0))
        self.model = glm.rotate(self.model, glm.radians(self.rotation[2]), glm.vec3(0, 0, 1))
        self.model = glm.scale(self.model, glm.vec3(self.scaling))
    

    def send_uniforms_to_shader(self, shader_program):
        # Send model matrix to the shader through a uniform
        model_loc = glGetUniformLocation(shader_program, "u_model")
        glUniformMatrix4fv(model_loc, 1, GL_TRUE, np.array(self.model, dtype=np.float32))


    def render(self, shader_program):
        # Check if object has changed and update model matrix
        if self.changed:
            self.compute_model_matrix()
            self.changed = False

        # Send data through uniforms
        self.send_uniforms_to_shader(shader_program)

        # Bind VBO and set where are the vertices, normals and colors in the buffer
        # vertices = [[x, y, z, nx, ny, nz, r, g, b, a], ...]
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        # position and normal are 3 floats each, and color is 4 floats
        # We have 10 floats per vertex and each float is 4 bytes - so our stride is 10 * 4
        # The position starts at the first float (0), the normal at the fourth float (3 * 4), and the color at the seventh float (6 * 4)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 10 * 4, ctypes.c_void_p(0))
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 10 * 4, ctypes.c_void_p(3 * 4))
        glVertexAttribPointer(2, 4, GL_FLOAT, GL_FALSE, 10 * 4, ctypes.c_void_p(6 * 4))
        
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glEnableVertexAttribArray(2)

        # Draw the object using the geometry shader program
        try:
            gl_type = self.geometry_type.value
            glDrawArrays(gl_type, 0, self.vertices.size)
        except OpenGL.error.GLError:
            # Ignore errors (e.g., if the geometry shader expects a different type of geometry than the object has)
            pass
    
    def cleanup(self):
        # Delete VBO
        if self.vbo:
            glDeleteBuffers(1, [self.vbo])


    @staticmethod
    def vertices_from_obj(model_path, color):
        # Load the model and get the data from the first mesh
        model = wf.Wavefront(model_path, create_materials=True, collect_faces=True)
        mesh = model.mesh_list[0]

        # Get the vertices data from the first material
        vertices_data = mesh.materials[0].vertices
        vertices_data_len = len(vertices_data)

        # Create the vertices list with the format [x, y, z, nx, ny, nz, r, g, b, a] for each vertex
        # From the vertices_data that has the format [u, v, nx, ny, nz, x, y, z, ...]
        vertices = []
        for vertex_num in range(0, vertices_data_len, 8):
            # Get the position (x, y, z) and normal (nx, ny, nz) from the vertices_data
            position = vertices_data[vertex_num + 5:vertex_num + 8]
            normal = vertices_data[vertex_num + 2:vertex_num + 5]

            # Append the vertex with the position, normal, and color that was passed as an argument
            vertices.append(position + normal + color)

        return vertices
