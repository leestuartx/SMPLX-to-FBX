import numpy as np
from FbxCommon import *

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
def generateFBXfromSMPLX(sdkManager:FbxManager):
    lScene = FbxScene.Create(sdkManager, "")

    # create the node containing the mesh
    #lNode = FbxNode.Create(lScene, "GeneratedFbxChelikNode")
    #lMesh = FbxMesh.Create(sdkManager, "ChelikMesh")
    #lNode.SetNodeAttribute(lMesh)
    cubeNode = CreateCubikNahuy(sdkManager, "cubiknahuy")
    lRootNode = lScene.GetRootNode()
    lRootNode.AddChild(cubeNode)

    return lScene