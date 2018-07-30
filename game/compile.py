import json
import base64

# stuff all the scheme code into the ditto js file
# so that it can be loaded locally
 
# more time and I would go through searching for loads to
# do this automatically - todo

resources = [ 
    "flx/scm/base.jscm",
    "flx/scm/maths.jscm",
    "flx/scm/glsl.jscm",
    "flx/scm/state.jscm",
    "flx/scm/pdata.jscm",
    "flx/scm/scenegraph.jscm",
    "flx/scm/primitive.jscm",
    "flx/scm/data.jscm",
    "flx/scm/shaders.jscm",
    "flx/scm/renderer.jscm",
    "flx/scm/instanceprim.jscm",
    "flx/scm/polyprim.jscm",
    "flx/scm/geometry.jscm",
    "flx/scm/texture.jscm",
    "flx/scm/meshcache.jscm",
    "flx/scm/shadercache.jscm",
    "flx/scm/fluxus.jscm",
    
    "flx/scm/canvas.jscm",
    "flx/scm/canvas-widgets.jscm",
    
    "shaders/default.vert",
    "shaders/default.frag",
    "shaders/leaf.vert",
    "shaders/leaf.frag",
    "shaders/unlit.vert",
    "shaders/unlit.frag",

    "textures/white.png",
    "textures/butterfly.png",
    "textures/shrub.png",
    "textures/test.png",
    "textures/white.png",
    "textures/grass.png",
    "textures/test-grey.png", 
    "textures/tree.png",

    "textures/plants/1-1.png",

    "textures/plants/2-1.png",
    "textures/plants/2-2.png",
    "textures/plants/2-3.png",

    "textures/plants/3-1.png",
    "textures/plants/3-2.png",
    "textures/plants/3-3.png",
    "textures/plants/3-4.png",
    "textures/plants/3-5.png",

    "textures/plants/4-1.png",
    "textures/plants/4-2.png",
    "textures/plants/4-3.png",
    "textures/plants/4-4.png",

    "textures/plants/5-1.png",
    "textures/plants/5-2.png",
    "textures/plants/5-3.png",
    "textures/plants/5-4.png",
    "textures/plants/5-5.png",
    "textures/plants/5-6.png",
    "textures/plants/5-7.png",
    "textures/plants/5-8.png",
    "textures/plants/5-9.png",

    "textures/plants/eden1-1.png",
    
    "textures/plants/eden2-1.png",
    "textures/plants/eden2-2.png",
    "textures/plants/eden2-3.png",
    "textures/plants/eden2-4.png",
    "textures/plants/eden2-5.png",

    "textures/plants/eden3-1.png",
    "textures/plants/eden3-2.png",
    "textures/plants/eden3-3.png",

    "textures/plants/eden4-1.png",
    "textures/plants/eden4-2.png",
    "textures/plants/eden4-3.png",

    "textures/plants/eden5-1.png",
    "textures/plants/eden5-2.png",
    "textures/plants/eden5-3.png",

    "textures/plants/eden6-1.png",
    "textures/plants/eden6-2.png",

    "textures/plants/eden7-1.png",
    "textures/plants/eden7-2.png",
    "textures/plants/eden7-3.png",

    "textures/plants/stem 1.png",
    "textures/plants/stem 2.png",
    "textures/plants/stem 3.png",
    "textures/plants/stem 4.png",
    "textures/plants/stem 5.png",
    "textures/plants/stem 6.png",
    "textures/plants/stem 7.png",
    "textures/plants/stem 8.png",
    "textures/plants/stem 9.png",
    "textures/plants/stem 10.png",
    "textures/plants/stem 11.png",
 
    "textures/ceratinia-b.png",
    "textures/ceratinia-w-5.png",
    "textures/ceratinia-w-6.png",
    "textures/ceratinia-w-7.png",
    "textures/ceratinia-w-8.png",
    "textures/ceratinia-w-9.png",
    "textures/ceratinia-w-10.png",
    "textures/ceratinia-w-11.png",
    "textures/ceratinia-w-12.png",

    "textures/hypolaria-b.png",
    "textures/hypolaria-w-014.png",
    "textures/hypolaria-w-015.png",
    "textures/hypolaria-w-016.png",
    "textures/hypolaria-w-017.png",

    "textures/hypothyris-b.png",
    "textures/hypothyris-w-014.png",
    "textures/hypothyris-w-015.png",
    "textures/hypothyris-w-016.png",
    "textures/hypothyris-w-017.png",

    "textures/ithomia-b.png",
    "textures/ithomia-w-012.png",
    "textures/ithomia-w-013.png",

    "models/plane.obj",
    "models/lsys-plane2.obj",

    "scm/lsys.jscm",
    "scm/local-storage.jscm",
    "scm/admin.jscm",
    "scm/i18n.jscm",
    "scm/translations.jscm"
]

################################################

def load_from_file(fn):
    with open(fn, 'r') as myfile:
        return myfile.read()

def load_from_files(fnl):
    ret = ""
    for fn in fnl:
        ret+=load_from_file(fn)
    return ret

def base64_from_file(fn):
    with open(fn, "rb") as f:
        return base64.b64encode(f.read())
        
def insert_code(target_data,target,scm):
    scm = scm.replace("\n","\\n\\\n")
    scm = scm.replace("'","\\'")
    return target_data.replace(target,scm)

def build_resources(resource_files):
    res = {}
    for fn in resource_files:
        if fn.endswith(".png") or fn.endswith(".jpg"):
            res[fn]=base64_from_file(fn)
        else:
            res[fn]=load_from_file(fn)
    return json.dumps(res)

def comp(code,target,pre):
    pre_data=load_from_file(pre)
    target_data=pre_data
    target_data=insert_code(target_data,"{{SYNTAX}}",load_from_file("flx/scm/syntax.jscm"))
    target_data=insert_code(target_data,"{{CODE}}",load_from_files(code))
    target_data=insert_code(target_data,"{{RESOURCES}}",build_resources(resources))
    with open(target, 'w') as myfile:
        myfile.write(target_data)

###################################################

comp(["scm/game.jscm"], "index.html","index-pre.html")
comp(["scm/admin.jscm"], "admin.html","admin-pre.html")
