# Parametric Models

## What is a parametric model?
To understand humans and their behavior we utilize 3D parametric models of the body and its movement. Such models facilitate reasoning about the different ways in which we all interact with the world around us, such as human-object interaction, human-to-human contact, effects of compression due to external forces, as well as posture, gait and emotion related effects. These models allow us to explain the relationship of the 3D body to the 3D world around us. We learn realistic 3D models of the human body that can be parametrized according to shape or pose independently.  Specifically, we factorize the changes in the body due to body shape differences from the changes due to pose using thousands of high resolution 3D scans.  

Among these methods the [SMPL Model](SMPL.md) has become the de facto standard for research on human body shape and pose. This model is especially helpful for research because the model's body shape and pose parameters can be easily optimized to fit the model to data from many different sources, e.g. 3D scans, RGB-D, MOCAP and videos, and at the same time the model output itself can be easily used in any standard 3D graphics software for animation, gaming or visualization. Going beyond SMPL, we also have **MANO**, a 3D hand model learned from around 2000 hand scans of different people in many poses. and **FLAME** which uses a novel dataset of 4D facial sequences to capture realistic 3D head shape, jaw articulation, eye movement, blinking, and facial expressions. Combining all these parametic models into a single full body, face and hand model, is **SMPL-X** . Finally, the latest iteration in the SMPL model family is **STAR**, which introduces a new parametrization for the SMPL model, making it more compact and even easier to use for AI-based pipelines, while retaining all the useful usability features as the earlier models. 

### Academic use 
These models are all developed by the researchers at Max Planck Institute's Perceiving Systems Department (MPI-PS), and they are free to use for all academic purposes. You can find the academic websites for all these models here: 
[Quick Links](quick-links.md) 
 
### Commercial use 
At Meshcapade, we are making these models also available for commercial products and R&D purposes as well. more information about commercial licensing available here:
[https://meshcapade.com/infopages/licensing.html](https://meshcapade.com/infopages/licensing.html) 


## Human Body Models
The human body is certainly central to our lives and is commonly depicted in images and video. We are developing the world's most realistic models of the body by learning their shape and how they move from data.  Our goal is to make 3D models of the body look and move in ways that make them indistinguishable from real humans.  Such virtual humans can be used in special effects and will play an important role in emerging virtual reality systems. They can also be used in computer vision to generate training data for learning methods or can be fit directly to sensor data. What makes this hard is that the human body is highly articulated, deforms with kinematic changes, and exhibits large shape variability across subjects. 

More details about the human body models within the "SMPL family" is available on the [SMPL wiki](SMPL.md).


### Hand Model
*MANO* is created from the SMPL hand topology, and has analogous components to those in SMPL: a template shape, kinematic tree, shape and pose blend shapes, blend weights and a joint regressor.

### Face Model
*FLAME* adapts the SMPL body model formulation to create a statistical head model that is significantly more accurate and expressive than existing head and face models, while remaining compatible with standard graphics software. In contrast to existing models, FLAME explicitly models head pose and eyeball rotation. 

### Infant Model
*SMIL* learns a statistical for 3D shape and 3D pose estimation of infants. It is the first work on learning a statistical 3D body model from lowquality, incomplete RGB-D data of freely moving humans. 


## Animal Models
The detection, tracking, and analysis of animals has many applications in biology, neuroscience, ecology, farming, and entertainment. Despite the wide applicability, the computer vision community has focused more heavily on modeling humans, estimating human pose, and analyzing human behavior. Can we take the best practices learned from the analysis of humans and apply these directly to animals? To address this, the SMAL model takes the approach for 3D human pose and shape modeling and extends it to modeling animals.

More details about the SMAL animal model is available in the [SMAL wiki](SMAL.md).


-----------
> Disclaimer: These wiki pages are a product of joint collaboration between Max Planck Institute for Intelligent Systems and Meshcapade GmbH, and are provided and maintained as a free service for the research community.   