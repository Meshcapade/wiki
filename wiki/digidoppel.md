# digidoppel

[digidoppel](https://digidoppel.com/) is our online platform which allows users to convert different kinds of inputs into realistic animation-ready 3D avatars. Users can use 3D scans or body measurements (more options for avatars from mocap, images & video coming soon!)

## Option 1: Avatars from Scans
On digidoppel, you can create an avatar using 3D scans. 

[![IMAGE_ALT](https://img.youtube.com/vi/0vRPJdf-RlQ/0.jpg)](https://www.youtube.com/watch?v=0vRPJdf-RlQ)

### Input files and mesh sizes
The platform accepts OBJ and PLY files as input. At the moment only static 3D scans can be processed automatically on the digidoppel platform, for 4D scans, please contact us at [support@meshcapade.com](mailto:support@meshcapade.com) with a small sample of your 4D data. 

We limit the input mesh size to under 1million vertices so please make sure your input file does not have more than 1M veritces when you upload the scan.

### Scans with textures
The digidoppel platform can automatically transfer the texture from a scan to the output we create. You can upload a scan with texture as a zipped file. Make sure the zipped file contains ONLY the scan and texture image file (there should be no hidden files in the zip archive).

The output created will include the processed mesh (in OBJ, FBX, etc. format you choose) + a texture file transformed to our body topology.


### Problems with Internal Geometry

The scan alignment process is designed to work with 3D meshes acquired through 3D scanning process. 

Scans from a 3D scanner can be noisy, this noise is expected and our scan alignment process can handle these. 

However, the 3D scans are expected to only contain an outer surface of the body, and no internal surfaces. Generally when artists create 3D body models in some 3D animation program, they might create additional geometry on the inside of the body surface, e.g.
An artist might create internal geometry for eyes and mouth for the face, as shown below:

![internal-geometry-problems](../assets/images_digidoppel/internal-geometry-problems.png)

Or there the limbs and neck joints might be created as separate geometry objects, so they will have additional geometry where the limb closes off in the 3D model. 
These internal geometry pieces have to be removed before they can be sent for processing on digidoppel.

### Problems with long hair

Input meshes with hair occluding the neck will not function well. Please make sure that hair is not falling onto the shoulders. It is best if it is tied up in a bun or in a haircap.


### Problems with loose clothing

Input meshes with clothing do function, but the tighter the clothing is, the better. Loose clothing or accessories may cause alignment to fail, take a very long time, or produce subpar results. Keep in mind that the training data was done on with models in tight-fitted clothing.

![clothing-problems](../assets/images_digidoppel/clothing-problems.png)


### Creating a thigh gap

For apparel simulation, often users want there to be a gap in the thigh area so that the vertices of the left and right thighs are not touching or intersecting. To help with this, we have created a 'thigh gap' option which allows users to create an artificial gap in the thigh area for OBJ output files. 

[![IMAGE_ALT](https://img.youtube.com/vi/Jurq4H5vxJs/0.jpg)](https://www.youtube.com/watch?v=Jurq4H5vxJs)



## Option 2: Avatars from measurements
On digidoppel, you can create an avatar using body measurements. Below is a list of body measurements that are currently available for use on the digidoppel platform:

[![IMAGE_ALT](https://img.youtube.com/vi/MZD4actpeDw/0.jpg)](https://www.youtube.com/watch?v=MZD4actpeDw)

### Measurements descriptions


| **Measurement**                 | **Description**                                       | **Preview** |
|---------------------------      |-------------------------------------------------------|-------------|
| Height                          | The line segment to the lowest center point to the highest on the mesh. |  <img src="../assets/images_digidoppel/measurements/BodyVis-Web-height.png" width="200" /> |
| Chest circumference at maximum  | The loop resulting from slicing a torso mesh segment transversally at a fixed "nipple level" vertex. |  <img src="../assets/images_digidoppel/measurements/BodyVis-Web-chest_max_girth.png" width="200" /> |
| Shoulder Breadth                | The length of the greatest extents within a defined "shoulder geometry" set of vertices from the sagittal axis. |  <img src="../assets/images_digidoppel/measurements/BodyVis-Web-shoulder_breadth.png" width="200" /> |
| Neck circumference at base      | The loop segment of edges across the cervicale landmark at the juncture of the neck and the shoulders of the mesh. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-neck_base_girth.png" width="200" /> |
| Arm length (spine to wrist)     | The line segment of edges of the mesh measured from cervicale through acromion to the wrist at the ulnar styloid landmark. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-armlength_spine_wrist.png" width="200" /> |
| Arm length (shoulder to wrist)  | The line segment of edges of the mesh measured by subtracting spine-shoulder length measurement from spine-wrist length measurement. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-armlength_shoulder_wrist.png" width="200" /> |
| Arm length (shoulder to elbow)  | The line segment of edges of the mesh measured by subtracting the spine-shoulder length measurement from the spine-elbow length measurement. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-armlength_shoulder_elbow.png" width="200" /> |
| Arm circumference at scye       | The loop resulting from slicing an arm segment with a sagittal plane at a fixed vertex for armpit. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-arm_scye_girth.png" width="200" /> |
| Waist Circumference       | Given the range of vertice roughly representing the region at and below the navel and above the hip bone, slice the mesh transversally at each of those specified points, and pick the SMALLEST slice for the waist measurement. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-waist_min_girth.png" width="200" /> |
| Waist Height              | The length from the bottom of the mesh up to the height of the waist circumference measurement. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-waist_height.png" width="200" /> |
| Hip circumference               | Given a range of vertices roughly representing the region at and below the navel and above the hip bone, slice the mesh transversally at each of those specified points, and pick the LARGEST slice for the hip measurement. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-hip_max_girth.png" width="200" /> |
| Hip Height                      | The length from the bottom of the mesh up to the height of the hip circumference measurement. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-hip_height.png" width="200" /> |
| Thigh Circumference       | Given a range of fixed thigh vertices, transversally slice the mesh at these locations and use the LARGEST slice. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-thigh_max_girth.png" width="200" /> |
| Inseam                          | The height measured from the bottom of the mesh to a specified crotch vertex. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-inseam.png" width="200" /> |
| Crotch length                   | The line segment of vertices from top of navel, down along a sagittal segment to the opposing side. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-crotch_length.png" width="200" /> |
| Foot Length                     | A line segment from the rearmost vertex on the foot to the foremost. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-foot_length.png" width="200" /> |
| Ankle circumference             | The loop resulting from slicing a leg segment with a transverse plane at a fixed vertex for ankle. | <img src="../assets/images_digidoppel/measurements/BodyVis-Web-ankle_girth.png" width="200" /> |




## Digidoppel FAQs

> What exactly is the API?

The API is a cloud platform for creating animation-ready avatars from scans, hand-measurements, and more. You can sign up for free [here](https://digidoppel.com/).

> What am I allowed to do with the generated avatars? Can I share it with my users?

The output files made available to users under the [SMPL Body license](https://smpl.is.tue.mpg.de/bodylicense.html). The output files created from digidoppel are free to share and use in research and commercial projects, with the exception of uses 

-	to generate defamatory, harassing, pornographic, obscene, or racist material whether commercial or not; or 
- for purposes of mass-surveillance or for creating a digital-double of any person in avatar or other form of digital replication without such person’s explicit consent.

> What are the usage rights and terms for the platform?

The platform is made available under the Terms of Service available [here](https://digidoppel.com/terms-of-service/#terms-go-3). 

> Are there any restrictions on what kind of usage is not allowed on the platform?

The platform must not be used to 
- Sublicense any APIs for use by a third party or create an API Client that substantially replicates or competes with the APIs.
- Attempt to interfere with the normal functioning of the APIs or the servers or networks providing the APIs.
- Attempt to use our APIs in a manner that exceeds or circumvents, rate limits or constitutes excessive or harmful usage.
- Attempt to access the APIs in a manner that compromises, circumvents, or tests the vulnerability of any of our security measures, except with express prior written approval by Meshcapade.
- Attempt toreverse engineer or extract source code, trade secrets, or know-how of our APIs.


> How is security being handled for the API?

You can review our Privacy Policy [here](https://info.meshcapade.com/faqs/api-privacy-policy).

> Is your API available as an offline solution/SDK?

Yes. Please contact us at [info@meshcapade.com](info@meshcapade.com) for help. 

> Is there a trial for the API?

You don't need a trial, sign is free and you receive 20 free credits at sign up. You can find out more about pricing here [https://digidoppel.com/pricing/](https://digidoppel.com/pricing/).


