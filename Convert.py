from FbxReadWriter import FbxReadWrite
from SmplObject import SmplObjects
from SmplxParamsObject import SmplxParamsObject
from SMPLX_to_FBX_generator import generateFBXfromSMPLX
from smplx import SMPLX
import argparse
import tqdm

def getArg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_pkl_base', type=str, required=True)
    parser.add_argument('--fbx_source_path', type=str, required=True)
    parser.add_argument('--output_base', type=str, required=True)

    return parser.parse_args()

def loadSMPLXBodyModel(smplxParams:SmplxParamsObject):
    print('Loading body model')
    extra_params = {'gender': smplxParams.data["gender"]}
    extra_params['use_pca'] = False
    extra_params['flat_hand_mean'] = True
    extra_params['use_face_contour'] = True

    model = SMPLX(f'ml_body_models/smplx', **extra_params)

    print(f'Loaded body model')

    return model

if __name__ == "__main__":
    args = getArg()
    input_pkl_base = args.input_pkl_base
    fbx_source_path = args.fbx_source_path
    output_base = args.output_base

    #smplObjects = SmplObjects(input_pkl_base)
    smplxParams = SmplxParamsObject(input_pkl_base)

    try:
        fbxReadWrite = FbxReadWrite(fbx_source_path)
        #sourceScene = fbxReadWrite.lScene

        smplxBodyModel = loadSMPLXBodyModel(smplxParams)

        input_params = {}  # copy.deepcopy(AppWindow.POSE_PARAMS[body_model])

        # for k, v in input_params.items():
        #     input_params[k] = v.reshape(1, -1)
        model_output = smplxBodyModel(
            betas=smplxParams.data["betas"],
            expression=smplxParams.data["expression"],
            **input_params,
        )

        verts = model_output.vertices[0].detach().numpy()
        #AppWindow.JOINTS = model_output.joints[0].detach().numpy()
        faces = smplxBodyModel.faces

        generatedChelik = generateFBXfromSMPLX(fbxReadWrite.lSdkManager, verts, faces)
        # fbxReadWrite.addAnimation(pkl_name, smpl_params)
        fbxReadWrite.writeFbx(generatedChelik, output_base)
        fbxReadWrite.destroy()
    except Exception as e:
        print("Something went wrong while opening or writing FBX")
        raise e