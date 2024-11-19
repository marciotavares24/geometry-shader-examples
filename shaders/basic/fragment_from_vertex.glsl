#version 330 core
// Interpolated color from the vertex shader
in vec4 v_color;

// Color of the fragment
out vec4 f_color;


void main()
{
    f_color = v_color;
}
