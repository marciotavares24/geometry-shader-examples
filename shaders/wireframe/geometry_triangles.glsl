#version 330 core
// What the geometry shader receives? (points, lines, triangles)
layout (triangles) in;
// What the geometry shader sends? (points, line_strip, triangle_strip)
//
// Initial state: Sends the same triangle
// layout (triangle_strip, max_vertices = 3) out;
// 
// Solution: Sends a line strip with 4 vertices (for the 3 lines needed)
layout (line_strip, max_vertices = 4) out;


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


    // Solution: Emit the first vertex again to close the line strip
    gl_Position = gl_in[0].gl_Position;
    EmitVertex();


    // Emit the primitive
    EndPrimitive();
}  
