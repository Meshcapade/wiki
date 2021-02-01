# SMPL

 Skinned Multi-Person Linear model (SMPL) possibly makes the human body model as simple and standard as possible. A key component of this model is that the pose blend shapes are formulated as a linear function of the elements of the part rotation matrices. On top of that, with the low polygon count, a simple vertex topology (for both men and women models), a clean quad structure, and a standard rig, SMPL makes a realistic learned model accessible to animators as well as computer vision researchers. SMPL decomposes body shape into identity-dependent shape and non-rigid pose-dependent parameters based on a vertex-based skinning approach that uses corrective blend shapes (blend shape represented as a vector of concatenated vertex offsets). That means, SMPL model can realistically represent a wide range of human body shapes, can be posed with natural pose-dependent deformations, exhibits soft-tissue dynamics, is efficient to animate, and is compatible with existing rendering engines. 

# Getting Started with SMPL in Python

## Loading SMPL models

Once you have the required dependencies set up, and have obtained the model license, this script demonstrates a few basic functions to help users get started with using
the SMPL model. The code shows how to:

- Load the SMPL model
- Edit pose & shape parameters of the model to create a new body in a new pose
- Save the resulting body as a mesh in .OBJ format

```python
from psbody.smpl import load_model
from psbody.mesh import Mesh
import numpy as np
## Load SMPL model (here we load the female model)
## Get the online version of the SMPL model from 'Python Downloads'
## section of http://smpl.is.tue.mpg.de/downloads
model = load_model('../models/basicModel_f_lbs_10_207_0_v1.0.0.pkl')
## Assign random pose and shape parameters
model.pose[:] = np.random.rand(model.pose.size) * .2
model.betas[:] = np.random.rand(model.betas.size) * .03
## Write to an .obj file
outmesh_path = '/tmp/hello_smpl.obj'
mesh = Mesh(v=model.r, f=model.f)
mesh.write_obj(outmesh_path)
## Print message
print '..Output mesh saved to: ', outmesh_path
mesh.show()

```

## Rendering SMPL models 

This script demonstrates loading the smpl model and rendering it using OpenDR
to render and OpenCV to display (or alternatively matplotlib can also be used
for display, as shown in commented code below).

This code shows how to:

- Load the SMPL model
- Edit pose & shape parameters of the model to create a new body in a new pose
- Create an OpenDR scene (with a basic renderer, camera & light)
- Render the scene using OpenCV / matplotlib


```python
from psbody.smpl import load_model
from psbody.mesh import Mesh
import numpy as np
from opendr.renderer import ColoredRenderer
from opendr.lighting import LambertianPointLight
from opendr.camera import ProjectPoints
## Load SMPL model (here we load the female model)
## Get the online version of the SMPL model from 'Python Downloads'
section of http://smpl.is.tue.mpg.de/downloads

model = load_model('../models/basicModel_f_lbs_10_207_0_v1.0.0.pkl')
## Assign random pose and shape parameters
model.pose[:] = np.random.rand(model.pose.size) * .2
model.betas[:] = np.random.rand(model.betas.size) * .03
outmesh_path = '/tmp/hello_smpl.obj'
mesh = Mesh(v=model.r, f=model.f)
mesh.write_obj(outmesh_path)
## Create OpenDR renderer
rn = ColoredRenderer()
## Assign attributes to renderer
w, h = (640, 480)
rn.camera = ProjectPoints(v=model, rt=np.zeros(3), t=np.array([0, 0, 2.]),
f=np.array([w,w])/2., c=np.array([w,h])/2., k=np.zeros(5))
rn.frustum = {'near': 1., 'far': 10., 'width': w, 'height': h}
rn.set(v=model, f=model.f, bgcolor=np.zeros(3))
## Construct point light source
rn.vc = LambertianPointLight(
f=model.f,
v=rn.v,
num_verts=len(model),
light_pos=np.array([-1000,-1000,-2000]),
vc=np.ones_like(model)*.9,
light_color=np.array([1., 1., 1.]))
## Show it using OpenCV
import cv2
cv2.imshow('render_SMPL', rn.r)
print ('..Print any key while on the display window')
cv2.waitKey(0)
cv2.destroyAllWindows()
## Could also use matplotlib to display
# import matplotlib.pyplot as plt
# plt.ion()
# plt.imshow(rn.r)
# plt.show()
# import pdb; pdb.set_trace()

```

## Accessing Shape and Pose Blendshapes in SMPL

```python

from psbody.smpl import load_model
from psbody.mesh import Mesh

# Get the online version of the SMPL model from 'Python Downloads' section
of http://smpl.is.tue.mpg.de/downloads
model_path = '../models/basicModel_f_lbs_10_207_0_v1.0.0.pkl'
model = load_model(model_path)
# Number of betas present in the online model (FBX model should have only
10 betas too)
num_betas = 10
# Access the numpy array of the shape-blendshape offsets
# model.shapedirs is a chumpy object; model.shapedirs.T.r accesses the
transpose of the numpy
# array inside the chumpy object
shape_blends = model.shapedirs.T.r[:num_betas]
# Access the numpy array of the pose-blendshape offsets
# model.posedirs is a chumpy object; model.posedirs.T.r accesses the
transpose of the numpy
# array inside the chumpy object
pose_blends = model.posedirs.T.r
# Create a mesh of the model in the default pose & shape
mesh = Mesh(v=model.r, f=model.f)
# Store the vertics of the default mesh as 'rest_v'
# (save a copy otherwise changes to the model will change the rest_v)
rest_v = model.r.copy()
# Loop through the 10 Shape Blendshapes
for beta_idx, blend_offset in enumerate(shape_blends):
# Update the vertices of 'mesh' to create a new mesh for current
blendshape
mesh.v = rest_v + blend_offset.T
# Initialize the node / object for all blendshapes
if beta_idx == 0:
print "Initialize the blendshapes node"
blendshapes_node = "bl_node" # <-- initialize me
# Add current mesh as a new blendshape to blendshapes_node.
# Set name of the new blendshape as 'bl_shapeXX' where XX is the
beta_idx
print "Create the blendshape for beta#: %02d with current mesh." %
beta_idx
print "Set weight / influence of blendshape to 0"
# Loop through the 207 Pose Blendshapes
for theta_idx, blend_offset in enumerate(pose_blends):
# Update the vertices of 'mesh' to create a new mesh for current
blendshape
mesh.v = rest_v + blend_offset.T
# Initialize the node / object for all blendshapes here in case Shape
Blendshapes are not created here
if theta_idx == 0 and blendshapes_node is None:
print "Initialize the blendshapes node"
blendshapes_node = "bl_node" # <-- initialize me
# Add current mesh as a new blendshape to blendshapes_node.
# Set name of the new blendshape as 'bl_poseXXX' where XX is the
theta_idx
print "Create the blendshape for beta#: %02d with current mesh." %
theta_idx
print "Set weight / influence of blendshape to 0"
mesh.show()

```

## Accessing Joints and Skin-Weights in SMPL

```python

from psbody.smpl import load_model
import numpy as np
# Get the online version of the SMPL model from 'Python Downloads' section
of http://smpl.is.tue.mpg.de/downloads
model_path = '../models/basicModel_f_lbs_10_207_0_v1.0.0.pkl'
model = load_model(model_path)
# Dictionary of joint index-to-human readable name. In the FBX file we
will need
# to give each joint a human readable name
J_names = {
0: 'Pelvis',
1: 'L_Hip',
4: 'L_Knee',
7: 'L_Ankle',
10: 'L_Foot',
2: 'R_Hip',
5: 'R_Knee',
8: 'R_Ankle',
11: 'R_Foot',
3: 'Spine1',
6: 'Spine2',
9: 'Spine3',
12: 'Neck',
15: 'Head',
13: 'L_Collar',
16: 'L_Shoulder',
18: 'L_Elbow',
20: 'L_Wrist',
22: 'L_Hand',
14: 'R_Collar',
17: 'R_Shoulder',
19: 'R_Elbow',
21: 'R_Wrist',
23: 'R_Hand',
}
# Root joint is the world origin for the skeleton structure. It should be
placed at the world origin,
# or at the central pivot point of the 3D Mesh from the model
rootJoint = 'root'
# model.kintree_table is a numpy array of size [2x24] showing the joint
heirarchy.
# Row 1 (parent list) : has indices of all the parent joints
# Row 2 (children list) : has indices of the corresponding child joints
# Note: first element of childrens list is the root joint. The
corresponding first
# element in the parents' list is a junk value because root joint has no
parent
jnt_tree = model.kintree_table
# Accessing the 3D locations of the joints of the model
# model.Jtr is a chumpy object; model.Jtr.r accesses the numpy array
inside the chumpy object
# Note: Here's another way to get the joint locations of the model.
# Here model.r are the mesh vertices of the model
# joints_xyz = model.J_regressor.dot(np.asarray(model.r))
joints_xyz = model.Jtr.r
# Looping through the parent list of the joint tree
for tree_node, parent in enumerate(jnt_tree[0]):
# Get index of child for current parent
child = model.kintree_table[1][tree_node]
# Get 3D location of parent joint
child_xyz = joints_xyz[tree_node]
if tree_node == 0:
print "%02d: At root joint --> " % tree_node,
else:
print "%02d: At parent:%s joint --> " % (tree_node, J_names
[parent]),
print 'create child: %s joint, ' % J_names[child],
print 'at [%f, %f, %f]', child_xyz[0], child_xyz[1], child_xyz[2]
# Accessing the blend-skinning weights of the model:
# model.weights is a chumpy object; model.weights.r accesses the numpy
array inside the chumpy object
skin_weights = model.weights.r
# Accessing skin weights
for vert_idx, weights in enumerate(skin_weights):
# Iterate joint-tree through the J_names dict
for joint_idx, jnt_name in J_names.iteritems():
if jnt_name == rootJoint:
print "Set 0 weight for root joint"
else:
# Get the idx of the joint with jnt_name from J_names dict
# --> since J_names is a dict, it is not necessary that
J_names.keys() is sorted
jidx = [key for key in J_names.keys() if J_names[key] ==
jnt_name]
print "Set skin weight for vertex: %04d, joint: %02d = %f" %
(vert_idx, joint_idx, weights[jidx])

```


# Add-Ons

## Body Analyzer

This module is provided as part of the SMPL Model commercial-use license, that allows users to generate body measurements from SMPL Model parameters.

For a sample JSON parameters of the form: 

```javascript
{
    "gender": "female",
    "betas": [
        -0.20257675474352643,
        1.7663544013631842,
        -1.100909894145452,
        0.44980986193988604,
        -2.2654927235359867,
        -0.9260961794138639,
        1.3301724865309084,
        -0.934662226574417,
        -1.7932090551894748,
        -0.7541093980126984
    ]
}

```

The expected output would look something like this:

```javascript
{
    "units": "cm", 
    "gender": "female", 
    "measurements": {
        "Foot length": 24.23, 
        "Neck circumference at base": 48.54, 
        "Ankle circumference": 25.44, 
        "Arm length (spine to wrist)": 76.87, 
        "Crotch length": 65.3, 
        "Inseam": 65.38, 
        "Arm length (shoulder to wrist)": 55.93, 
        "Arm circumference at scye": 45.62, 
        "Waist circumference (preferred)": 95.7, 
        "Waist height (preferred)": 88.24, 
        "Chest circumference at maximum": 108.98, 
        "Shoulder breadth": 47.76, 
        "Hip circumference": 100.07, 
        "Hip height": 73.48, 
        "Arm length (shoulder to elbow)": 30.26, 
        "Chest circumference at scye": 105.15, 
        "Height": 158.58, 
        "Thigh circumference": 57.32
    }
}

```


## Body Visualizer

This module is provided as part of the SMPL Model commercial-use license, that allows users to create SMPL Bodies from measurements.

For an example JSON of body measurements,

```javascript
{
    "units": "cm",
    "gender": "female",
    "measurements":{
        "Height": 164.85,
        "Shoulder breadth": 38.40,
        "Arm length (spine to wrist)": 77.75,
        "Chest circumference at maximum": 78.36,
        "Waist circumference (preferred)": 60.13,
        "Hip circumference": 82.71,
        "Inseam": 57.94
    }
}

```


The expected output **would include an OBJ file of the model** along with SMPL Model parameters (betas).

```javascript
{
    "gender": "female", 
    "betas": [
        -0.8713609990668445, 
        0.9542418436130167, 
        2.4368221963992096, 
        -5.940590742754617, 
        -0.26275727515031755, 
        -0.37683598257258855, 
        -0.5029624233628813, 
        -1.617564036294166, 
        -1.1000115141726954, 
        -1.1537028551105963, 
        0.1273105130994583, 
        1.3253468192408706, 
        0.6093107737930582, 
        -0.6070853263225156, 
        -0.430696620043946, 
        -0.8998815442883839,
        ... 
        // more betas.
    ]
}

```


# Source Code

- [Public Repository for Non-Commerical Scientific Research Purposes](https://smpl.is.tue.mpg.de/)

- [Commericial License: Model](#)

- [Commericial License: Body](#)


# Resources

[Paper](http://files.is.tue.mpg.de/black/papers/SMPL2015.pdf)


[Project Video](https://youtu.be/JchovWRhrBs)

