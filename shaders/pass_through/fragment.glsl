#version 330 core
// Interpolated color from the previous shader
// 
// Initial state: Color from the vertex shader
// in vec4 v_color;
// 
// Solution: Color from the geometry shader
in vec4 g_color;

// Color of the fragment
out vec4 f_color;


void main()
{
    // Initial state: Color from the vertex shader
    // f_color = v_color;
    

    // Solution: Color from the geometry shader
    f_color = g_color;
}
