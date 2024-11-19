#version 330 core
// What the geometry shader receives? (points, lines, triangles)
layout (triangles) in;
// What the geometry shader sends? (points, line_strip, triangle_strip)
// What we want to send? How many vertices?
layout (triangle_strip, max_vertices = 3) out;


// Uniform for the projection matrix
uniform mat4 u_proj;


// Normals and positions from the previous shader (both in view space)
in vec3 v_normal[];
in vec4 v_position[];

// Output color to the next shader
out vec4 g_color;


// Define how much the normal will be extended
const float NORMAL_MAGNITUDE = 0.8;


void main()
{
    // The color will be pink to all the vertices
    g_color = vec4(1, 0, 1, 1);

    // For each vertex received (3 vertices)
    for (int i = 0; i < 3; i++)
    {
        // Emit the vertex
        gl_Position = gl_in[i].gl_Position;
        EmitVertex();

        // What we need to do?
        // Get normal and position (view space)
        // Emit the vertex in the direction of the normal (apply the projection matrix)
        // End the primitive
    }

    // Emit the triangle
    EndPrimitive();
}  
