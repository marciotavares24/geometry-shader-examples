#version 330 core
// What the geometry shader receives? (points, lines, triangles)
layout (points) in;
// What the geometry shader sends? (points, line_strip, triangle_strip)
//
// Initial state: Sends points
// layout (points) out;
// 
// Solution: Sends a triangle strip with 5 vertices
layout (triangle_strip, max_vertices = 5) out;


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
    // Initial state: Sends point
    // Emit the point and end the primitive
    // gl_Position = gl_in[0].gl_Position;
    // g_color = v_color[0];
    // EmitVertex();
    // EndPrimitive();
    

    // Solution: Sends a triangle strip with 5 vertices
    // Get the position and color of the point
    vec4 vertex_position = gl_in[0].gl_Position;
    g_color = v_color[0];

    // Create the house vertices using the house positions
    for (int i = 0; i < 5; i++)
    {
        gl_Position = vertex_position + vec4(HOUSE_POSITIONS[i], 0.0, 0.0);
        EmitVertex();
    }

    // Emit the triangle strip
    EndPrimitive();
}  
