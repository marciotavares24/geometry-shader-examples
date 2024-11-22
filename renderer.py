from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram
import pygame as pg
import numpy as np
import glm

from geometric_object import GeometricObject

class Camera:
    def __init__(self, position=[0, 0, -40]):
        self.position = position
        self.fovy = 45
        self.near_plane = 0.1
        self.far_plane = 500

        self.changed = True


class Renderer:
    def __init__(self, camera=None, width=800, height=600):
        self.window_size = (width, height)

        # Shader program and objects to render
        self.shader_programs = []
        self.objects: list[GeometricObject] = []

        # Camera and Projection/View matrices
        self.camera = camera if camera else Camera()
        self.projection = np.identity(4, np.float32)
        self.view = np.identity(4, np.float32)

        # Flag to check if projection/view matrices have changed
        self.changed = True

    def init_pygame_and_opengl(self):
        # Initialize pygame and create window
        pg.init()
        pg.display.set_caption("OpenGL Geometry Shader Examples")
        pg.display.set_mode(self.window_size, pg.DOUBLEBUF | pg.OPENGL | pg.RESIZABLE | pg.BLEND_ALPHA_SDL2)

        # Fix for Apple Silicon (Metal)
        # pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        # pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        # pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        # OpenGL settings
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


    def init_shaders(self, vertex_path, fragment_path, geometry_paths = []):
        # Read shader code from files
        vertex_code = self.read_shader(vertex_path)
        fragment_code = self.read_shader(fragment_path)
        geometry_code = [self.read_shader(geometry_path) for geometry_path in geometry_paths]

        # Compile shaders
        vertex_shader = compileShader(vertex_code, GL_VERTEX_SHADER)
        fragment_shader = compileShader(fragment_code, GL_FRAGMENT_SHADER)
        geometry_shaders = [compileShader(geometry_code, GL_GEOMETRY_SHADER) for geometry_code in geometry_code]

        # Check if shaders compiled successfully
        self.check_shader_compilation(vertex_shader, "VERTEX")
        self.check_shader_compilation(fragment_shader, "FRAGMENT")
        for geometry_shader in geometry_shaders:
            self.check_shader_compilation(geometry_shader, "GEOMETRY")

        # Create shader program
        # If geometry shaders are present, compile program with them (one for each)
        shader_programs = []
        for geometry_shader in geometry_shaders:
            shader_program = compileProgram(vertex_shader, geometry_shader, fragment_shader)
            shader_programs.append(shader_program)

        # Otherwise, compile program with vertex and fragment shaders only
        if not geometry_shaders:
            shader_program = compileProgram(vertex_shader, fragment_shader)
            shader_programs.append(shader_program)

        # Check if program linked successfully
        for shader_program in shader_programs:
            self.check_program_link(shader_program)
        
        # Add shader program to the list
        self.shader_programs += shader_programs

    def read_shader(self, filepath):
        with open(filepath, 'r') as file:
            return file.read()

    def check_shader_compilation(self, shader, shader_type):
        if not glGetShaderiv(shader, GL_COMPILE_STATUS):
            error = glGetShaderInfoLog(shader).decode()
            raise RuntimeError(f"Shader compilation failed ({shader_type}):\n{error}")
    
    def check_program_link(self, program):
        if not glGetProgramiv(program, GL_LINK_STATUS):
            error = glGetProgramInfoLog(program).decode()
            raise RuntimeError(f"Program linking failed:\n{error}")
        
    
    def add_object(self, obj: GeometricObject):
        # Set VBO for the object and add it to the list
        obj.set_vbo()
        self.objects.append(obj)

    def rem_object(self, obj: GeometricObject):
        # Remove object from the list and clean it up
        self.objects.remove(obj)
        obj.cleanup()


    def compute_projection_view_matrix(self):
        width, height = self.window_size

        # Calculate projection and view matrices based on camera properties
        self.projection = glm.perspective(self.camera.fovy, width / height, self.camera.near_plane, self.camera.far_plane)
        self.view = np.identity(4, np.float32)
        self.view = glm.translate(self.view, self.camera.position)

    def send_uniforms_to_shader(self, shader_program):
        # Send projection and view matrices to the shader through uniforms
        projection_loc = glGetUniformLocation(shader_program, "u_proj")
        view_loc = glGetUniformLocation(shader_program, "u_view")
        glUniformMatrix4fv(projection_loc, 1, GL_TRUE, np.array(self.projection, dtype=np.float32))
        glUniformMatrix4fv(view_loc, 1, GL_TRUE, np.array(self.view, dtype=np.float32))

        # Send time to the shader through a uniform
        time = pg.time.get_ticks() / 1000
        time_loc = glGetUniformLocation(shader_program, "u_time")
        glUniform1f(time_loc, time)


    def render(self):
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Check if projection/view matrices have changed and update them
        if self.camera.changed:
            self.compute_projection_view_matrix()
            self.changed = False
        
        # Support multiple shader programs for rendering
        for shader_program in self.shader_programs:
            glUseProgram(shader_program)

            # Send data through uniforms
            self.send_uniforms_to_shader(shader_program)

            # Render all objects
            for obj in self.objects:
                obj.render(shader_program)

        # Swap pygame buffers
        pg.display.flip()

    def process_events(self):
        # Check if window was closed (stop the loop)
        for event in pg.event.get():
            # Check if window was closed
            if event.type == pg.QUIT:
                return False
            
            # Check if window was resized
            if event.type == pg.VIDEORESIZE:
                self.window_size = event.size
                self.changed = True
        
        # Get pressed keys
        keys = pg.key.get_pressed()
        
        # Check if ESC key was pressed to close the window (stop the loop)
        if keys[pg.K_ESCAPE]:
            return False

        # Continue the loop
        return True

    def cleanup(self):
        # Clean up objects
        for obj in self.objects:
            obj.cleanup()

        # Clean up shader programs
        for shader_program in self.shader_programs:
            glDeleteProgram(shader_program)

        # Quit pygame
        pg.quit()