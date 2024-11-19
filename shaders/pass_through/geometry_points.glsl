#version 330 core
// What the geometry shader receives? (points, lines, triangles)
layout (points) in;
// What the geometry shader sends? (points, line_strip, triangle_strip)
layout (points) out;

// Colors from the previous shader
in vec4 v_color[];

// Output color to the next shader
out vec4 g_color;


void main()
{
    // Pass the position and color of the point received
    gl_Position = gl_in[0].gl_Position;
    g_color = v_color[0];

    // Emit the point and end the primitive
    EmitVertex();
    EndPrimitive();
}  
