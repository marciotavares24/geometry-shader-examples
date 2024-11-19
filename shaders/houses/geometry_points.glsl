#version 330 core
// What the geometry shader receives? (points, lines, triangles)
layout (points) in;
// What the geometry shader sends? (points, line_strip, triangle_strip)
// What we want to send? How many vertices?
layout (points) out;


// Colors from the previous shader
in vec4 v_color[];

// Output color to the next shader
out vec4 g_color;


// House positions
const vec2 HOUSE_POSITIONS[5] = vec2[5](
    vec2(-1, -1),
    vec2( 1, -1),
    vec2(-1,  1),
    vec2( 1,  1),
    vec2( 0,  2)
);


void main()
{
    // For now just send the vertex...
    // Emit the point and end the primitive
    gl_Position = gl_in[0].gl_Position;
    g_color = v_color[0];
    EmitVertex();
    EndPrimitive();
    

    // What we need to do?
    // Get the position and color of the point
    // Create the house vertices using the house positions
    // Emit the primitive
}  
