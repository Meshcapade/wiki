# Meshcapade Wiki

Welcome to Meshcapade Wiki! 

## SMPL

SMPL, our core technology, is a realistic 3D model of the human body that is based on skinning and blend shapes and is learned from thousands of 3D body scans. [Learn more about SMPL](/wiki/SMPL).

### Getting started with SMPL in Python

Details about setting up SMPL in Python is available [here](/wiki/SMPL#getting-started-with-smpl-in-python). Note that you would need an SMPL-Model license to run this code.

[More about SMPL add-ons is available here](/wiki/SMPL#add-ons).

### Sample Textures

[Download sample textures for SMPL body model here!](https://github.com/Meshcapade/SMPL_texture_samples/archive/main.zip)

### Maya/Blender Plug-ins

Maya/Blender Plug-ins makes it easier to run SMPL FBX models.
Find the newest version to download [here](https://github.com/Meshcapade/SMPL_maya_plugin/releases).

The script displays a UI to apply SMPL's shape and pose blendshapes and to adjust the skeleton to new body shapes.
Load this plugin into Maya. It will create a window with 3 options:

1. Apply Pose Blend Shapes to Current Frame: 
	If you repose the model in Maya, then click this to 
	compute and apply the pose blend shapes in the current frame. 
    You can als ochoose whether or not to set the keyframes for the 
    pose blendshapes. Check the 'Reset Keyframes' checkbox if you 
    would like to lock blendShape values at given frame by setting 
    a keyframe. 


2. Apply Pose Blend Shapes to Frames in above Range: 
	Specify a range of frames in an animation and then compute/apply 
	the pose blendshapes for all the frames in range. Check the 
    'Reset Keyframes' checkbox if you would like to lock blendShape 
    values at given frame range by setting a keyframe at each frame in the 
    given range.
    
3. Set Mesh to Bind-Pose & Recompute Skeleton: 
	When you edit the shape blend shapes to change body shape the 
	skeleton will no longer be correct.  Click first button to set the 
    mesh into the bind-pose. Next, click this to 'Recompute Skeleton' 
    to recompute the skeleton rig to match the new body shape.

Always make sure to cilck on the mesh in the 3D view to select it before 
using any of the functions in the plugin. Select only the mesh of the model 
you want to update and then click the appropriate button on the UI.

[How to use Meshcapade's SMPL Maya plugin for applying shape-corrective shapes](https://www.youtube.com/watch?v=uL_HuU8hUtc)

[How to use Meshcapade's SMPL Maya plugin for automating pose-corrective shapes](https://www.youtube.com/watch?v=LU4pq1HhxXc)


**Current versions supported:**

Mac OSX: Maya 2014+
Windows: Maya 2014+


**Dependencies**:

Numpy is required for running this script. Numpy is a python module that
can be installed following the instructions given here:
http://docs.scipy.org/doc/numpy/user/install.html

or here:
http://blog.animateshmanimate.com/post/115538511578/python-numpy-and-maya-osx-and-windows

Please make sure you have numpy installed on your computer and accessible through Maya's python.
We are working towards removing this dependency. 

# Other Models

- [SMPL-X](/wiki/SMPLX)
- [STAR](/wiki/STAR)
- [SMIL](/wiki/SMIL)
- [VIBE](/wiki/VIBE)

# Licenses

Request a License for [Commericial](#), [Research](#), [Trail](#) or for [Non-Commerical Scientific Research Purposes](#).
