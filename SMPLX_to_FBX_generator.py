import numpy as np
from FbxCommon import *

SMPLX_JOINT_NAMES = [
    'pelvis','left_hip','right_hip','spine1','left_knee','right_knee','spine2','left_ankle','right_ankle','spine3', 'left_foot','right_foot','neck','left_collar','right_collar','head','left_shoulder','right_shoulder','left_elbow', 'right_elbow','left_wrist','right_wrist',
    'jaw','left_eye_smplhf','right_eye_smplhf','left_index1','left_index2','left_index3','left_middle1','left_middle2','left_middle3','left_pinky1','left_pinky2','left_pinky3','left_ring1','left_ring2','left_ring3','left_thumb1','left_thumb2','left_thumb3','right_index1','right_index2','right_index3','right_middle1','right_middle2','right_middle3','right_pinky1','right_pinky2','right_pinky3','right_ring1','right_ring2','right_ring3','right_thumb1','right_thumb2','right_thumb3'
]

fbxExportScale = 100
fbxJoints = []

def CreateSkeleton(lSdkManager, joints, bonesHierarchy, pName):
    # Create skeleton root
    lRootName = pName + "Root"
    lSkeletonRootAttribute = FbxSkeleton.Create(lSdkManager, lRootName)
    lSkeletonRootAttribute.SetSkeletonType(FbxSkeleton.EType.eRoot)
    lSkeletonRoot = FbxNode.Create(lSdkManager, lRootName)
    lSkeletonRoot.SetNodeAttribute(lSkeletonRootAttribute)
    lSkeletonRoot.LclTranslation.Set(FbxDouble3(0.0, 0.0, 0.0))

    for i in range(len(SMPLX_JOINT_NAMES)):
        jointNodeName = SMPLX_JOINT_NAMES[i]
        lSkeletonNodeAttr = FbxSkeleton.Create(lSdkManager, jointNodeName)
        lSkeletonNodeAttr.SetSkeletonType(FbxSkeleton.EType.eLimbNode)
        lSkeletonNodeAttr.Size.Set(1.0)
        lNode = FbxNode.Create(lSdkManager, jointNodeName)
        lNode.SetNodeAttribute(lSkeletonNodeAttr)
        # set translation here if you want joints without hierarchy
        #lNode.LclTranslation.Set(FbxDouble3(joints[i][0] * fbxExportScale, joints[i][1] * fbxExportScale, joints[i][2] * fbxExportScale))

        fbxJoints.append(lNode)

    for i in range(len(SMPLX_JOINT_NAMES)):
        # Build skeleton node hierarchy.
        cur = fbxJoints[i]
        parent = lSkeletonRoot

        parentTr = [0, 0, 0]
        parentIndex = bonesHierarchy[i]

        if parentIndex != -1:
            parent = fbxJoints[parentIndex]
            parentTr = joints[parentIndex]

        # set translation here if you want joints with hierarchy
        curTr = [joints[i][0] - parentTr[0], joints[i][1] - parentTr[1], joints[i][2] - parentTr[2]]
        cur.LclTranslation.Set(FbxDouble3(curTr[0] * fbxExportScale, curTr[1] * fbxExportScale, curTr[2] * fbxExportScale))
        parent.AddChild(fbxJoints[i])

    return lSkeletonRoot


def CreateHumanMesh(pSdkManager, verts: np.ndarray, faces: np.ndarray, skinWeights, rootNode, pName):
    lMesh = FbxMesh.Create(pSdkManager, pName)
    lMesh.InitControlPoints(verts.shape[0])

    clusters = []
    for j in range(len(fbxJoints)):
        clusterToJointNode = FbxCluster.Create(pSdkManager, "")
        clusterToJointNode.SetLink(fbxJoints[j])
        clusterToJointNode.SetLinkMode(FbxCluster.ELinkMode.eTotalOne)
        clusters.append(clusterToJointNode)

    for i in range(verts.shape[0]):
        point = FbxVector4(verts[i][0], verts[i][1], verts[i][2]) * fbxExportScale
        lMesh.SetControlPointAt(point, i)
        for j in range(len(fbxJoints)):
            clusters[j].AddControlPointIndex(i, skinWeights[i][j])

    for i in range(faces.shape[0]):
        lMesh.BeginPolygon(-1, -1, False)

        lMesh.AddPolygon(faces[i][0])
        lMesh.AddPolygon(faces[i][1])
        lMesh.AddPolygon(faces[i][2])

        lMesh.EndPolygon()

    lNode = FbxNode.Create(pSdkManager, pName)
    lNode.SetNodeAttribute(lMesh)
    lNode.SetShadingMode(FbxNode.EShadingMode.eTextureShading)

    # transform link
    lGlobalMatrix = FbxAMatrix()
    lXMatrix = FbxAMatrix()
    lScene = rootNode.GetScene()
    if lScene:
        lGlobalMatrix = lScene.GetAnimationEvaluator().GetNodeGlobalTransform(lNode)
        for j in range(len(clusters)):
            clusters[j].SetTransformMatrix(lGlobalMatrix)
            lXMatrix = lScene.GetAnimationEvaluator().GetNodeGlobalTransform(fbxJoints[j])
            clusters[j].SetTransformLinkMatrix(lXMatrix)

    # add skin
    lSkin = FbxSkin.Create(pSdkManager, "")
    for j in range(len(clusters)):
        lSkin.AddCluster(clusters[j])
    lNode.GetNodeAttribute().AddDeformer(lSkin)

    return lNode

def generateFBXfromSMPLX(sdkManager:FbxManager, verts:np.ndarray, faces:np.ndarray, skinWeights, joints:np.ndarray, bonesHierarchy):
    lScene = FbxScene.Create(sdkManager, "")
    lRootNode = lScene.GetRootNode()

    lSkeletonRoot = CreateSkeleton(sdkManager, joints, bonesHierarchy, "Skeleton")
    lRootNode.AddChild(lSkeletonRoot)

    chelik = CreateHumanMesh(sdkManager, verts, faces, skinWeights, lRootNode, "Human")
    lRootNode.AddChild(chelik)

    return lScene