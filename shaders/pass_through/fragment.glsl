#version 330 core
// Interpolated color from the previous shader
// What is the previous shader? (Remember the pipeline)
// Make sure the names match!
in vec4 v_color;

// Color of the fragment
out vec4 f_color;


void main()
{
    f_color = v_color;
}
