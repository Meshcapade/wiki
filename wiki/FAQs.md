# FAQs

## Scan Alignment

>  My Scan alignment doesn't look right, what went wrong?

#### Problems with Internal Geometry

The scan alignment process is designed to work with 3D meshes acquired through 3D scanning process. 

Scans from a 3D scanner can be noisy, this noise is expected and our scan alignment process can handle these. 

However, the 3D scans are expected to only contain an outer surface of the body, and no internal surfaces. Generally when artists create 3D body models in some 3D animation program, they might create additional geometry on the inside of the body surface, e.g.
An artist might create internal geometry for eyes and mouth for the face, as shown below:

![Face Holes](https://digidoppel.com/img/yes-no.png)

Or there the limbs and neck joints might be created as separate geometry objects, so they will have additional geometry where the limb closes off in the 3D model. 
These internal geometry pieces have to be removed before they can be sent for processing on digidoppel.

## Digidoppel API

## MOCAP

> How does MoSH work with IMU data?

Short answer: IMU mocap isn't ideal but if you have the 3D marker trajectories from the IMU system, how about you guys send us a sample of the data and we'll test how well it works.
 
Long answer: MoSH is designed to work with optical mocap. It uses the 3D location of the optical markers to fit the SMPL model into each frame of data. The problem with IMU based mocap systems is that you might get the 3D locations of the markers, but there is a general drift associated with IMUs that can cause huge errors over time. Therefore, usually the best option to fit SMPL to IMU is to use any of the IMU based works (e.g. deep initial poser - this is a bit old, but I'm sure there are newer methods out there as well). At Meshcapade we don't have a license for any of these IMU based works though since most are exclusively for academic use only. But we can still try to use Mosh with certain stronger constraints to make it work in spite of the drift and noise in the 3D marker locations from IMU. But we can't guarantee how well it will work  but happy to give it a try.
 
Here is a sample file that shows the format for marker data that the mosh code expects: 
 - [Npz format](https://drive.google.com/file/d/11tEf-WMwhpWI0fokznz3AqhTPz93S1z6/view?usp=sharing)
 - [C3d formt](https://drive.google.com/file/d/1yMon2dTiQO-mP2a4_XpYQ_skWjgxOO0h/view?usp=sharing)
 
