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

> What exactly is the API?

The API is a digital human cloud platform for creating animation-ready avatars from scans, hand-measurements, and more. You can find out more details about it [here](https://meshcapade.com/infopages/api.html).

> How can I license the API?

We offer different pricing options and packages for the API. For more information, please check our licensing page here. If you have higher volumes of data, please contact us on info@meshcapade.com.

> What am I allowed to do with the generated avatars? Can I share it with my users?

The output files are free for all uses under SMPL Body license, please contact us on info@meshcapade.com.

> How is security being handled for the API?

You can review our Privacy Policy [here](https://info.meshcapade.com/faqs/api-privacy-policy).

> Is your API available as an offline solution/SDK?

Yes. Contact us at info@meshcapade.com.

> Is your API available on a mobile application?

Yes. Contact us at info@meshcapade.com.

> Is there a trial for the API?

When you choose the pay as you go option, you receive 10 Free credits on initial sign up that you can use to try out the API.

> Is there a sample output for the API?

Yes, we have some sample outputs for our bodies-from-scans and bodies-from-measurements API. Please  contact us on info@meshcapade.com to share these sample files with you.


## MOCAP

> How does MoSH work with IMU data?

Short answer: IMU mocap isn't ideal but if you have the 3D marker trajectories from the IMU system, how about you guys send us a sample of the data and we'll test how well it works.
 
Long answer: MoSH is designed to work with optical mocap. It uses the 3D location of the optical markers to fit the SMPL model into each frame of data. The problem with IMU based mocap systems is that you might get the 3D locations of the markers, but there is a general drift associated with IMUs that can cause huge errors over time. Therefore, usually the best option to fit SMPL to IMU is to use any of the IMU based works (e.g. deep initial poser - this is a bit old, but I'm sure there are newer methods out there as well). At Meshcapade we don't have a license for any of these IMU based works though since most are exclusively for academic use only. But we can still try to use Mosh with certain stronger constraints to make it work in spite of the drift and noise in the 3D marker locations from IMU. But we can't guarantee how well it will work  but happy to give it a try.
 
Here is a sample file that shows the format for marker data that the mosh code expects: 
 - [Npz format](https://drive.google.com/file/d/11tEf-WMwhpWI0fokznz3AqhTPz93S1z6/view?usp=sharing)
 - [C3d formt](https://drive.google.com/file/d/1yMon2dTiQO-mP2a4_XpYQ_skWjgxOO0h/view?usp=sharing)
 
 
## SMPL - Technical Details

> How do I convert between SMPL and SMPL-X (and STAR)? 


>  What is PA-MPJPE?  What is Procrustes?


> When do I need to use a joint regressor and why?


> How do I add soft-tissue dynamics to SMPL?


> How do I get a gender neutral model?


> How do I get SMPL with 300 shape components?


> How do I get just the face (or hand) vertices in SMPL-X?


> How do I get the joints out of SMPL?


> How do I visualize SMPL in Blender?


> How do I sample body shapes?

> How do I use the shape prior as a loss? 

> How does VPoser work?

> How do I convert SMPL part rotations to other formats?

> How do I get parameters for the forward pass of SMPL/SMPLX from full-pose?

> I want to test for interpenetration?

> I ran SMPLify and the body shape is not right. What happened?

> Is there a library of example SMPL (SMPL-X) poses?


> Can I get the SMPL training data?


> How can I train my own SMPL model?

> I want to pose SMPL myself.  How can I do it?

> How do I generate animations in FBX format?




