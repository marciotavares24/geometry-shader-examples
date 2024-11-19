#version 330 core
// What the geometry shader receives? (points, lines, triangles)
layout (triangles) in;
// What the geometry shader sends? (points, line_strip, triangle_strip)
layout (triangle_strip, max_vertices = 3) out;


// Uniform for the projection matrix and time
uniform mat4 u_proj;
uniform float u_time;


// Normals and positions from the previous shader (both in view space)
in vec3 v_normal[];
in vec4 v_position[];

// Colors from the previous shader
in vec4 v_color[];

// Output color to the next shader
out vec4 g_color;


// Define how much and how fast the triangle will move
const float EXPLODE_MAGNITUDE = 3.5;
const float EXPLODE_SPEED = 1;


void main()
{
    // Normalized sin wave and direction length for the movement
    float normalized_sin = sin(u_time * EXPLODE_SPEED) * 0.5 + 0.5;
    float direction_len = normalized_sin * EXPLODE_MAGNITUDE;

    // For each vertex received (3 vertices)
    for (int i = 0; i < 3; i++)
    {
        // For now, just emit the vertex...
        // Emit the vertex received
        gl_Position = gl_in[i].gl_Position;
        g_color = v_color[i];
        EmitVertex();


        // What we need to do?
        // Get normal and position (view space)
        // Emit the vertex moved (apply the projection matrix)
    }

    // Emit the triangle
    EndPrimitive();
}  
