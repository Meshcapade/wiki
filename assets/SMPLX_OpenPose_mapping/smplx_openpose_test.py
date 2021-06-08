import json

with open('./smplx_openpose25_200519.json') as f: 
    data = json.load(f)

wrong_idxs = []
print 'OP  \t| SMPLX\n____________________'
for idx in range(len(data['openpose_idxs'])):
    opose_keyname = data['openpose25_keypoint_names'][idx]
    smplx_keyname = data['smplx_keypoint_names'][data['smplx_idxs'][idx]]
    if opose_keyname != smplx_keyname:
        wrong_idxs.append(idx)
    else:
        print "%s  \t| %s" % (opose_keyname, smplx_keyname)

if wrong_idxs:
    print "ERROR! The following keypoint names didn't match up: \n", wrong_idxs
else:
    print "No mismatched keypoints found found!"