precision mediump float;
uniform sampler2D texture;
uniform vec3 DiffuseColour;
varying vec3 P;
varying vec3 T;
varying vec3 C;
varying vec3 N;
varying vec3 V;
varying vec3 L;

void main() {
    vec3 l = normalize(L);
    vec3 n = normalize(N);
    vec3 v = normalize(V);
    float ambient = 0.5;
    float diffuse = 0.5*clamp(dot(n,l),0.0,1.0)+ambient;
    float specular = 0.0;
    if (diffuse>0.0) {
        specular = max(0.0,pow(max(0.0, dot(reflect(-l, n), v)), 6.0));
    }
    float alpha = texture2D(texture, vec2(T.s, T.t)).a;
    vec3 col = texture2D(texture, vec2(T.s, T.t)).xyz;
    vec3 speccol = vec3(1,1,0.5)*0.75*specular;
    gl_FragColor = vec4((col*C*diffuse*alpha*alpha)+speccol, alpha);
}
