import argparse
import torch
from FbxReadWriter import FbxReadWrite
from SmplObject import SmplObjects
from SmplxParamsObject import SmplxParamsObject
from SMPLX_to_FBX_generator import generateFBXfromSMPLX
from smplx import SMPLX


def get_args():
    """
    Parse and return command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_pkl_base', type=str, required=True)
    parser.add_argument('--input_pkl_src_animation', type=str, required=True)
    parser.add_argument('--fbx_source_path', type=str, required=True)
    parser.add_argument('--output_base', type=str, required=True)
    return parser.parse_args()


def load_smplx_body_model(smplx_params: SmplxParamsObject):
    """
    Load the SMPLX body model with given parameters.

    Args:
        smplx_params (SmplxParamsObject): SMPLX parameters object.

    Returns:
        SMPLX: Loaded SMPLX body model.
    """
    print('Loading body model')
    extra_params = {
        'gender': 'male',  # Gender parameter
        'use_pca': False,  # Use PCA parameter
        'flat_hand_mean': True,  # Flat hand mean parameter
        'use_face_contour': True  # Use face contour parameter
    }

    model = SMPLX('ml_body_models/smplx', **extra_params)
    print('Loaded body model')
    return model


def main():
    """
    Main function to process and export FBX.
    """
    args = get_args()
    input_pkl_base = args.input_pkl_base
    input_pkl_src_animation = args.input_pkl_src_animation
    fbx_source_path = args.fbx_source_path
    output_base = args.output_base

    smplx_params = SmplxParamsObject(input_pkl_base)
    smplx_animation_params = SmplxParamsObject(input_pkl_src_animation)

    # Print the keys of smplxParams.data and smplx_animation_params.data
    print("smplxParams.data keys:")
    print(smplx_params.data.keys())

    print("\nsmplx_animation_params.data keys:")
    print(smplx_animation_params.data.keys())

    try:
        fbx_read_write = FbxReadWrite()  # Initialize FbxReadWrite
        smplx_body_model = load_smplx_body_model(smplx_params)

        input_params = {}  # Copy pose parameters (if needed)

        # Check if 'expression' key exists and convert to tensor (use a default if not available)
        expression = torch.zeros(1, 10)  # Default value or shape since 'expression' key is missing

        # Check if 'betas' key exists and convert to tensor
        if 'betas' in smplx_animation_params.data:
            betas = torch.tensor(smplx_animation_params.data["betas"], dtype=torch.float32)
            if betas.dim() == 1:
                betas = betas.unsqueeze(0)  # Ensure it's 2D
            if betas.size(1) > 10:  # Adjust this number to match your model's expected number of shape parameters
                betas = betas[:, :10]  # Trim to the first 10 components
            elif betas.size(1) < 10:
                # Optionally handle cases where betas is smaller than expected
                raise ValueError(f"Expected betas to have at least 10 components, but got {betas.size(1)}")
        else:
            raise KeyError("'betas' key is missing in smplx_animation_params.data")

        # Print shapes before proceeding to diagnose the issue
        print(f"Shape of betas: {betas.shape}")
        print(f"Shape of smplxBodyModel.shapedirs: {smplx_body_model.shapedirs.shape}")

        # Model forward pass
        model_output = smplx_body_model(
            betas=betas,
            expression=expression,
            **input_params,
        )

        verts = model_output.vertices[0].detach().numpy()
        faces = smplx_body_model.faces
        joints = model_output.joints[0].detach().numpy()
        bones_hierarchy = smplx_body_model.parents
        skin_weights = smplx_body_model.lbs_weights

        generated_chelik = generateFBXfromSMPLX(fbx_read_write.lSdkManager, verts, faces, skin_weights, joints,
                                                bones_hierarchy)
        fbx_read_write.writeFbx(generated_chelik, output_base)
        fbx_read_write.destroy()
    except Exception as e:
        print("Something went wrong while opening or writing FBX")
        raise e


if __name__ == "__main__":
    main()
