<h1> Meshcapade Wiki </h1>

Welcome to Meshcapade Wiki! 

Meshcapade is revolutionizing the world of human body modeling, sizing, and animation. We employ state of the art statistical models that encode realistic body shapes, sizes, and motions. 

This wiki is dedicated to providing more in-depth knowledge about our parametric models, body and shape estimation technologies and our automated processing services.


Automated Processing Platform: [digidoppel](https://digidoppel.com/)
-----------------------------------------------------------
`digidoppel` is a one-stop-shop - where  users can input their complex data from many different sources ranging from expensive high-end 3D scanning systems, to even photos/videos from anyone's smartphone, and instantly receive an accurate 3D avatar. This avatar can easily be imported it into a vast array of commercial tools, ranging from apparel design and animation to even generating AI training data
 
    * Avatars from 3D scans (scan alignment)
    * Avatars from measurements
    * Avatars from RGB-D (Lidar, Kinect, RealSense)
    * Avatars from images/video


Parametric Models
-----------------

### What is a parametric model?
To understand humans and their behavior we utilize 3D parametric models of the body and its movement. Such models facilitate reasoning about the different ways in which we all interact with the world around us, such as human-object interaction, human-to-human contact, effects of compression due to external forces, as well as posture, gait and emotion related effects. These models allow us to explain the relationship of the 3D body to the 3D world around us. We learn realistic 3D models of the human body that can be parametrized according to shape or pose independently.  Specifically, we factorize the changes in the body due to body shape differences from the changes due to pose using thousands of high resolution 3D scans.  

Among these methods the [SMPL Model](./wiki/SMPL.md) has become the standard for research on human body shape and pose. This model is especially helpful for research because the model's body shape and pose parameters can be easily optimized to fit the model to data from many different sources, e.g. 3D scans, RGB-D, MOCAP and videos, and at the same time the model output itself can be easily used in any standard 3D graphics software for animation, gaming or visualization. Going beyond SMPL, we also have **MANO**, a 3D hand model learned from around 2000 hand scans of different people in many poses. and **FLAME** which uses a novel dataset of 4D facial sequences to capture realistic 3D head shape, jaw articulation, eye movement, blinking, and facial expressions. Combining all these parametic models into a single full body, face and hand model, is **SMPL-X** . Finally, the latest iteration in the SMPL model family is **STAR**, which introduces a new parametrization for the SMPL model, making it more compact and even easier to use for AI-based pipelines, while retaining all the useful usability features as the earlier models. 

More details about all the parametrics models within the "SMPL family" are available on the [SMPL wiki](./wiki/SMPL.md).

### Human Body Models
The human body is certainly central to our lives and is commonly depicted in images and video. We are developing the world's most realistic models of the body by learning their shape and how they move from data.  Our goal is to make 3D models of the body look and move in ways that make them indistinguishable from real humans.  Such virtual humans can be used in special effects and will play an important role in emerging virtual reality systems. They can also be used in computer vision to generate training data for learning methods or can be fit directly to sensor data. What makes this hard is that the human body is highly articulated, deforms with kinematic changes, and exhibits large shape variability across subjects. 

#### 1. Hand Model
*MANO* is created from the SMPL hand topology, and has analogous components to those in SMPL: a template shape, kinematic tree, shape and pose blend shapes, blend weights and a joint regressor.

#### 2. Face Model
*FLAME* adapts the SMPL body model formulation to create a statistical head model that is significantly more accurate and expressive than existing head and face models, while remaining compatible with standard graphics software. In contrast to existing models, FLAME explicitly models head pose and eyeball rotation. 

#### 3. Infant Model
*SMIL* learns a statistical for 3D shape and 3D pose estimation of infants. It is the first work on learning a statistical 3D body model from lowquality, incomplete RGB-D data of freely moving humans. 


### Animal Models
The detection, tracking, and analysis of animals has many applications in biology, neuroscience, ecology, farming, and entertainment. Despite the wide applicability, the computer vision community has focused more heavily on modeling humans, estimating human pose, and analyzing human behavior. Can we take the best practices learned from the analysis of humans and apply these directly to animals? To address this, the *SMAL* model takes the approach for 3D human pose and shape modeling and extends it to modeling animals.


Body & Pose Estimation Methods
------------------------

We influence the world around us through our bodies. We express our emotions through our facial expressions and body posture. We manipulate and change the world with our hands. For computers to be full partners with humans, they have to see us and understand our behavior. They have to recognize our facial expressions, our gestures, our movements and our actions. This means that we need robust algorithms and expressive representation that can capture human pose, motion, and behavior.

Representing and extracting 3D body shape and pose has not been the dominant paradigm in the field but this is now changing. The introduction of our SMPL body model helped change this. SMPL is accurate, easy to use, compatible with game engines, differentiable, and is now widely used both in research and industry. It can be easily fit to image data "top down" or integrated into the end-to-end training of neural networks.

In the last few years many publications have shown how to fit SMPL to image data and how to train deep networks end-to-end to extract full-body shape and pose from single images or video. The ultimate goal in this space is to understand behavior. To do so we first want to capture it at scale. This means robustly and efficiently tracking human behavior in natural settings and relating that behavior to the 3D world around the person.

More details about shape and pose estimation methods designed to work around SMPL are available on the [Body & Pose wiki](./wiki/body_and_pose.md).
