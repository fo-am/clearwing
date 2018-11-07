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

    "textures/newplants/a1.png",
    "textures/newplants/a2.png",
    "textures/newplants/b1.png",
    "textures/newplants/b2.png",
    "textures/newplants/c1.png",
    "textures/newplants/c2.png",
    "textures/newplants/d1.png",
    "textures/newplants/d2.png",
    "textures/newplants/e1.png",
    "textures/newplants/e2.png",
    "textures/newplants/f1.png",
    "textures/newplants/f2.png",
    "textures/newplants/g1.png",
    "textures/newplants/g2.png",
    "textures/newplants/h1.png",
    "textures/newplants/h2.png",
 
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

    "textures/pink-b.png",
    "textures/pink-w-0.png",
    "textures/purple-b.png",
    "textures/purple-w-0.png",
    "textures/blue-b.png",
    "textures/blue-w-0.png",
    "textures/transparent-b.png",
    "textures/transparent-w-0.png",
    "textures/bck1-b.png",
    "textures/bck1-w-0.png",
    "textures/bck2-b.png",
    "textures/bck2-w-0.png",
    "textures/bck3-b.png",
    "textures/bck3-w-0.png",

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
