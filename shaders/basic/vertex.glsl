#version 330 core
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec4 color;


// Uniforms for the MVP matrices
uniform mat4 u_model;
uniform mat4 u_view;
uniform mat4 u_proj;


// Output color to the next shader
out vec4 v_color;

// Output normal and position to the next shader (both in view space)
out vec3 v_normal;
out vec4 v_position;


void main()
{
    // Output vertex position in view and clip space
    v_position = u_view * u_model * vec4(position, 1.0);
    gl_Position = u_proj * v_position;

    // Output color
    v_color = color;

    // Output normal in view space
    mat3 normal_matrix = transpose(inverse(mat3(u_view * u_model)));
    v_normal = normalize(normal_matrix * normal);
}
