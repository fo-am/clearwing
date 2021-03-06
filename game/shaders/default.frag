precision mediump float;
uniform sampler2D texture;
uniform vec3 DiffuseColour;
uniform float opacity;
uniform float ambient;
varying vec3 P;
varying vec3 T;
varying vec3 C;
varying vec3 N;
varying vec3 L;

void main() {
    vec3 l = normalize(L);
    vec3 n = normalize(N);
    float diffuse = (1.0-ambient)*dot(l,n)+ambient;
    float alpha = texture2D(texture, vec2(T.s, T.t)).a*opacity;
    vec3 col = texture2D(texture, vec2(T.s, T.t)).xyz*1.5;
    gl_FragColor = vec4(col*C*diffuse, alpha);
}
