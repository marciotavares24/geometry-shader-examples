#version 330 core
// Interpolated color from the geometry shader
in vec4 g_color;

// Color of the fragment
out vec4 f_color;


void main()
{
    f_color = g_color;
}
