#version 330 core
// What the geometry shader receives? (points, lines, triangles)
layout (triangles) in;
// What the geometry shader sends? (points, line_strip, triangle_strip)
//
// Initial state: Sends the same triangle
// layout (triangle_strip, max_vertices = 3) out;
// 
// Solution: Sends triangles to form a pyramid
layout (triangle_strip, max_vertices = 5) out;


// Uniform for the projection matrix
uniform mat4 u_proj;


// Normals from the previous shader (view space)
in vec3 v_normal[];

// Color from the previous shader
in vec4 v_color[];

// Output color to the next shader
out vec4 g_color;


vec4 get_triangle_normal()
{
    // Get the normals of the triangle vertices (view space)
    vec3 normal0 = v_normal[0];
    vec3 normal1 = v_normal[1];
    vec3 normal2 = v_normal[2];

    // Calculate the average normal and apply the projection matrix
    vec3 normal = (normal0 + normal1 + normal2) / 3;
    return u_proj * vec4(normal, 0);
}


// Define how high the pyramid will be
const float PYRAMID_HEIGHT = 2.5;

vec4 get_pyramid_top()
{
    // Get the positions of the triangle vertices (clip space)
    vec4 position0 = gl_in[0].gl_Position;
    vec4 position1 = gl_in[1].gl_Position;
    vec4 position2 = gl_in[2].gl_Position;

    // Calculate the middle point and get the normal of the triangle
    vec4 middle = (position0 + position1 + position2) / 3;
    vec4 normal = get_triangle_normal();

    // Calculate the top position of the pyramid
    return middle + normal * PYRAMID_HEIGHT;
}

vec4 get_pyramid_top_color()
{
    // Calculate the average color of the triangle vertices
    return (v_color[0] + v_color[1] + v_color[2]) / 3;
}


void main()
{
    // Emit the vertices of the base triangle
    for (int i = 0; i < 3; i++)
    {
        gl_Position = gl_in[i].gl_Position;
        g_color = v_color[i];
        EmitVertex();
    }


    // Solution: Emit the top vertex and the first vertex again
    // Emit the top vertex
    gl_Position = get_pyramid_top();
    g_color = get_pyramid_top_color();
    EmitVertex();

    // Emit the first vertex again to close the triangle strip
    gl_Position = gl_in[0].gl_Position;
    g_color = v_color[0];
    EmitVertex();


    // Emit the triangle strip
    EndPrimitive();
}  
