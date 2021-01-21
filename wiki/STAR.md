# STAR

STAR stands for **Sparse Trained Articulated Human Body Regressor**. STAR is a new  human body model based on learned sparse spatially local corrective blend shapes. STAR is compact, generalizes better to new bodies and is a drop-in replacement for SMPL. It is both quantiatively and qualitatively superior to SMPL and can produce more realistic deformations and significantly reduces the number of model parameters to 20% of SMPL. It adds 10000 additional scans of humans to the SMPL training data and builds upon to capture better variation of human population. 

STAR model

- is 80% smaller than SMPL. STAR has 93 pose corrective blend shapes compared to 207 in SMPL and is less likely to overfit.
- generalizes better.
- has local deformations, making animation easier, as changes in pose of one body part doesn't affect others.
- is more realistic, and takes body mass index into consideration during training.
- captures diversity, uses the largest training set to date to learn body shapes.
- has the same pose and shape parameterization as SMPL.


> **A [converter script](https://github.com/ahmedosman/STAR/blob/master/convertors/convert_smpl_to_star.py) from SMPL to STAR for easier migration.**

![](https://star.is.tue.mpg.de/uploads/ckeditor/pictures/321/content_main_teaser.png)

*In STAR, each joint influences only a sparse subset of mesh vertices. The
white mesh is STAR fit to a 3D scan of a professional body builder. The arrows
point to joints in the STAR "skeleton" and the corresponding predicted corrective offset for the joint. The heat map encodes the magnitude of the corrective
offsets. The joints have no influence on the gray mesh vertices. Unlike STAR, SMPL has spurious
long-range displacements.*


# Sources

[Paper](https://ps.is.mpg.de/uploads_file/attachment/attachment/618/star_paper.pdf)


[Project Video](https://youtu.be/JchovWRhrBs)