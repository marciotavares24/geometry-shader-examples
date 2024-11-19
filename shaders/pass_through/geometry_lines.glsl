#version 330 core
// What the geometry shader receives? (points, lines, triangles)
layout (lines) in;
// What the geometry shader sends? (points, line_strip, triangle_strip)
layout (line_strip, max_vertices = 2) out;

// Colors from the previous shader
in vec4 v_color[];

// Output color to the next shader
out vec4 g_color;


void main()
{
    // For each vertex received (2 = 1 line)
    for (int i = 0; i < 2; i++)
    {
        // Pass the position and color
        gl_Position = gl_in[i].gl_Position;
        g_color = v_color[i];

        // Emit the vertex
        EmitVertex();
    }

    // Emit the line strip
    EndPrimitive();
}  
