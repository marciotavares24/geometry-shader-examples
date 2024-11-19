#version 330 core
// What the geometry shader receives? (points, lines, triangles)
layout (triangles) in;
// What the geometry shader sends? (points, line_strip, triangle_strip)
// What we want to send? How many vertices?
layout (triangle_strip, max_vertices = 3) out;


// Output color to the next shader
out vec4 g_color;


void main()
{
    // The color will be white to all the vertices
    g_color = vec4(1, 1, 1, 1); 

    // Emit the vertices received
    for (int i = 0; i < 3; i++)
    {
        gl_Position = gl_in[i].gl_Position;
        EmitVertex();
    }

    // What we need to do?
    // Emit the triangle vertices
    // Emit the first vertex again to close the triangle

    // Emit the primitive
    EndPrimitive();
}  
