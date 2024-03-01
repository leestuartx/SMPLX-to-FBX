import numpy as np
from FbxCommon import *

SMPLX_JOINT_NAMES = [
    'pelvis','left_hip','right_hip','spine1','left_knee','right_knee','spine2','left_ankle','right_ankle','spine3', 'left_foot','right_foot','neck','left_collar','right_collar','head','left_shoulder','right_shoulder','left_elbow', 'right_elbow','left_wrist','right_wrist',
    'jaw','left_eye_smplhf','right_eye_smplhf','left_index1','left_index2','left_index3','left_middle1','left_middle2','left_middle3','left_pinky1','left_pinky2','left_pinky3','left_ring1','left_ring2','left_ring3','left_thumb1','left_thumb2','left_thumb3','right_index1','right_index2','right_index3','right_middle1','right_middle2','right_middle3','right_pinky1','right_pinky2','right_pinky3','right_ring1','right_ring2','right_ring3','right_thumb1','right_thumb2','right_thumb3'
]

def CreateCubikNahuy(pSdkManager, pName):
    lMesh = FbxMesh.Create(pSdkManager, pName)

    lControlPoint0 = FbxVector4(-50, 0, 50)
    lControlPoint1 = FbxVector4(50, 0, 50)
    lControlPoint2 = FbxVector4(50, 100, 50)
    lControlPoint3 = FbxVector4(-50, 100, 50)
    lControlPoint4 = FbxVector4(-50, 0, -50)
    lControlPoint5 = FbxVector4(50, 0, -50)
    lControlPoint6 = FbxVector4(50, 100, -50)
    lControlPoint7 = FbxVector4(-50, 100, -50)

    lNormalXPos = FbxVector4(1, 0, 0)
    lNormalXNeg = FbxVector4(-1, 0, 0)
    lNormalYPos = FbxVector4(0, 1, 0)
    lNormalYNeg = FbxVector4(0, -1, 0)
    lNormalZPos = FbxVector4(0, 0, 1)
    lNormalZNeg = FbxVector4(0, 0, -1)

    lMesh.InitControlPoints(24)
    lMesh.SetControlPointAt(lControlPoint0, 0)
    lMesh.SetControlPointAt(lControlPoint1, 1)
    lMesh.SetControlPointAt(lControlPoint2, 2)
    lMesh.SetControlPointAt(lControlPoint3, 3)
    lMesh.SetControlPointAt(lControlPoint1, 4)
    lMesh.SetControlPointAt(lControlPoint5, 5)
    lMesh.SetControlPointAt(lControlPoint6, 6)
    lMesh.SetControlPointAt(lControlPoint2, 7)
    lMesh.SetControlPointAt(lControlPoint5, 8)
    lMesh.SetControlPointAt(lControlPoint4, 9)
    lMesh.SetControlPointAt(lControlPoint7, 10)
    lMesh.SetControlPointAt(lControlPoint6, 11)
    lMesh.SetControlPointAt(lControlPoint4, 12)
    lMesh.SetControlPointAt(lControlPoint0, 13)
    lMesh.SetControlPointAt(lControlPoint3, 14)
    lMesh.SetControlPointAt(lControlPoint7, 15)
    lMesh.SetControlPointAt(lControlPoint3, 16)
    lMesh.SetControlPointAt(lControlPoint2, 17)
    lMesh.SetControlPointAt(lControlPoint6, 18)
    lMesh.SetControlPointAt(lControlPoint7, 19)
    lMesh.SetControlPointAt(lControlPoint1, 20)
    lMesh.SetControlPointAt(lControlPoint0, 21)
    lMesh.SetControlPointAt(lControlPoint4, 22)
    lMesh.SetControlPointAt(lControlPoint5, 23)

    # Set the normals on Layer 0.
    lLayer = lMesh.GetLayer(0)
    if lLayer == None:
        lMesh.CreateLayer()
        lLayer = lMesh.GetLayer(0)

    # We want to have one normal for each vertex (or control point),
    # so we set the mapping mode to eByControlPoint.
    lLayerElementNormal = FbxLayerElementNormal.Create(lMesh, "")
    lLayerElementNormal.SetMappingMode(FbxLayerElement.EMappingMode.eByControlPoint)

    # Here are two different ways to set the normal values.
    firstWayNormalCalculations = True
    if firstWayNormalCalculations:
        # The first method is to set the actual normal value
        # for every control point.
        lLayerElementNormal.SetReferenceMode(FbxLayerElement.EReferenceMode.eDirect)

        lLayerElementNormal.GetDirectArray().Add(lNormalZPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalZPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalZPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalZPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalXPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalXPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalXPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalXPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalZNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalZNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalZNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalZNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalXNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalXNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalXNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalXNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalYPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalYPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalYPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalYPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalYNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalYNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalYNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalYNeg)
    else:
        # The second method is to the possible values of the normals
        # in the direct array, and set the index of that value
        # in the index array for every control point.
        lLayerElementNormal.SetReferenceMode(FbxLayerElement.EReferenceMode.eIndexToDirect)

        # Add the 6 different normals to the direct array
        lLayerElementNormal.GetDirectArray().Add(lNormalZPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalXPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalZNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalXNeg)
        lLayerElementNormal.GetDirectArray().Add(lNormalYPos)
        lLayerElementNormal.GetDirectArray().Add(lNormalYNeg)

        # Now for each control point, we need to specify which normal to use
        lLayerElementNormal.GetIndexArray().Add(0)  # index of lNormalZPos in the direct array.
        lLayerElementNormal.GetIndexArray().Add(0)  # index of lNormalZPos in the direct array.
        lLayerElementNormal.GetIndexArray().Add(0)  # index of lNormalZPos in the direct array.
        lLayerElementNormal.GetIndexArray().Add(0)  # index of lNormalZPos in the direct array.
        lLayerElementNormal.GetIndexArray().Add(1)  # index of lNormalXPos in the direct array.
        lLayerElementNormal.GetIndexArray().Add(1)  # index of lNormalXPos in the direct array.
        lLayerElementNormal.GetIndexArray().Add(1)  # index of lNormalXPos in the direct array.
        lLayerElementNormal.GetIndexArray().Add(1)  # index of lNormalXPos in the direct array.
        lLayerElementNormal.GetIndexArray().Add(2)  # index of lNormalZNeg in the direct array.
        lLayerElementNormal.GetIndexArray().Add(2)  # index of lNormalZNeg in the direct array.
        lLayerElementNormal.GetIndexArray().Add(2)  # index of lNormalZNeg in the direct array.
        lLayerElementNormal.GetIndexArray().Add(2)  # index of lNormalZNeg in the direct array.
        lLayerElementNormal.GetIndexArray().Add(3)  # index of lNormalXNeg in the direct array.
        lLayerElementNormal.GetIndexArray().Add(3)  # index of lNormalXNeg in the direct array.
        lLayerElementNormal.GetIndexArray().Add(3)  # index of lNormalXNeg in the direct array.
        lLayerElementNormal.GetIndexArray().Add(3)  # index of lNormalXNeg in the direct array.
        lLayerElementNormal.GetIndexArray().Add(4)  # index of lNormalYPos in the direct array.
        lLayerElementNormal.GetIndexArray().Add(4)  # index of lNormalYPos in the direct array.
        lLayerElementNormal.GetIndexArray().Add(4)  # index of lNormalYPos in the direct array.
        lLayerElementNormal.GetIndexArray().Add(4)  # index of lNormalYPos in the direct array.
        lLayerElementNormal.GetIndexArray().Add(5)  # index of lNormalYNeg in the direct array.
        lLayerElementNormal.GetIndexArray().Add(5)  # index of lNormalYNeg in the direct array.
        lLayerElementNormal.GetIndexArray().Add(5)  # index of lNormalYNeg in the direct array.
        lLayerElementNormal.GetIndexArray().Add(5)  # index of lNormalYNeg in the direct array.

    lLayer.SetNormals(lLayerElementNormal)

    # Array of polygon vertices.
    lPolygonVertices = (0, 1, 2, 3,
                        4, 5, 6, 7,
                        8, 9, 10, 11,
                        12, 13, 14, 15,
                        16, 17, 18, 19,
                        20, 21, 22, 23)

    # Create UV for Diffuse channel
    lUVDiffuseLayer = FbxLayerElementUV.Create(lMesh, "DiffuseUV")
    lUVDiffuseLayer.SetMappingMode(FbxLayerElement.EMappingMode.eByPolygonVertex)
    lUVDiffuseLayer.SetReferenceMode(FbxLayerElement.EReferenceMode.eIndexToDirect)
    lLayer.SetUVs(lUVDiffuseLayer, FbxLayerElement.EType.eTextureDiffuse)

    lVectors0 = FbxVector2(0, 0)
    lVectors1 = FbxVector2(1, 0)
    lVectors2 = FbxVector2(1, 1)
    lVectors3 = FbxVector2(0, 1)

    lUVDiffuseLayer.GetDirectArray().Add(lVectors0)
    lUVDiffuseLayer.GetDirectArray().Add(lVectors1)
    lUVDiffuseLayer.GetDirectArray().Add(lVectors2)
    lUVDiffuseLayer.GetDirectArray().Add(lVectors3)

    # Now we have set the UVs as eINDEX_TO_DIRECT reference and in eBY_POLYGON_VERTEX  mapping mode
    # we must update the size of the index array.
    lUVDiffuseLayer.GetIndexArray().SetCount(24)

    # Create polygons. Assign texture and texture UV indices.
    for i in range(6):
        # we won't use the default way of assigning textures, as we have
        # textures on more than just the default (diffuse) channel.
        lMesh.BeginPolygon(-1, -1, False)

        for j in range(4):
            # this function points
            lMesh.AddPolygon(lPolygonVertices[i * 4 + j])  # Control point index.

            # Now we have to update the index array of the UVs for diffuse, ambient and emissive
            lUVDiffuseLayer.GetIndexArray().SetAt(i * 4 + j, j)

        lMesh.EndPolygon()

    lNode = FbxNode.Create(pSdkManager, pName)
    lNode.SetNodeAttribute(lMesh)
    lNode.SetShadingMode(FbxNode.EShadingMode.eTextureShading)
    return lNode

fbxExportScale = 100

def CreateChelikNahuy(pSdkManager, verts:np.ndarray, faces:np.ndarray, pName):
    lMesh = FbxMesh.Create(pSdkManager, pName)

    lMesh.InitControlPoints(verts.shape[0])
    for i in range(verts.shape[0]):
        point = FbxVector4(verts[i][0], verts[i][1], verts[i][2]) * fbxExportScale
        lMesh.SetControlPointAt(point, i)

    for i in range(faces.shape[0]):
        lMesh.BeginPolygon(-1, -1, False)

        lMesh.AddPolygon(faces[i][0])
        lMesh.AddPolygon(faces[i][1])
        lMesh.AddPolygon(faces[i][2])

        lMesh.EndPolygon()

    lNode = FbxNode.Create(pSdkManager, pName)
    lNode.SetNodeAttribute(lMesh)
    lNode.SetShadingMode(FbxNode.EShadingMode.eTextureShading)
    return lNode

def CreateSkeleton(lSdkManager, joints, bonesHierarchy, pName):
    # Create skeleton root
    lRootName = pName + "Root"
    lSkeletonRootAttribute = FbxSkeleton.Create(lSdkManager, lRootName)
    lSkeletonRootAttribute.SetSkeletonType(FbxSkeleton.EType.eRoot)
    lSkeletonRoot = FbxNode.Create(lSdkManager, lRootName)
    lSkeletonRoot.SetNodeAttribute(lSkeletonRootAttribute)
    lSkeletonRoot.LclTranslation.Set(FbxDouble3(0.0, 0.0, 0.0))

    fbxJoints = []
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

def generateFBXfromSMPLX(sdkManager:FbxManager, verts:np.ndarray, faces:np.ndarray, joints:np.ndarray, bonesHierarchy):
    lScene = FbxScene.Create(sdkManager, "")
    lRootNode = lScene.GetRootNode()

    #cubeNode = CreateCubikNahuy(sdkManager, "cubiknahuy")
    chelik = CreateChelikNahuy(sdkManager, verts, faces, "chelik")
    lRootNode.AddChild(chelik)

    lSkeletonRoot = CreateSkeleton(sdkManager, joints, bonesHierarchy, "Skeleton")
    lRootNode.AddChild(lSkeletonRoot)

    return lScene