precision mediump float;
uniform sampler2D texture;
uniform vec3 DiffuseColour;
varying vec3 P;
varying vec3 T;
varying vec3 C;
varying vec3 N;
varying vec3 L;

void main() {
    vec3 l = normalize(L);
    vec3 n = normalize(N);
    float ambient = 0.5;
    float diffuse = 0.5*dot(l,n)+ambient;
    float alpha = texture2D(texture, vec2(T.s, T.t)).a;
    vec3 col = texture2D(texture, vec2(T.s, T.t)).xyz;
    gl_FragColor = vec4(col*C*diffuse*alpha*alpha, alpha);
}
