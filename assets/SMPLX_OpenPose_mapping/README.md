Information about the smplx_openpose25.json file:
-------------------------------------------------

The JSON file contains following keys:

- smplx_keypoint_names: The names of the SMPL-X keypoints
- openpose25_keypoint_names: The names of the OpenPose keypoints. The order for OpenPose here is:
    - 25 body keypoints
    - 21 left hand keypoints
    - 21 right hand keypoints
    - 51 facial landmarks
    - 17 contour landmarks
- openpose_idxs: The indices of the OpenPose keypoint array. 
- smplx_idxs: The corresponding SMPL-X indices.

The attached script shows how to access the SMPLX keypoint corresponding to each OpenPose keypoint.

Note, some SMPLX keypoints do not match with the OpenPose keypoints, this is the list of keypoints that will not have a mapping:

    spine1
    spine2
    spine3
    left_foot
    right_foot
    left_collar
    right_collar
    head
    left_eye_smplx
    right_eye_smplx