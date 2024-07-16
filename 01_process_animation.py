import os
import subprocess

def run_cmd(cmd, verbo=True, bg=False):
    if verbo: print('[run] ' + cmd, 'run')
    if bg:
        args = cmd.split()
        print(args)
        p = subprocess.Popen(args)
        return [p]
    else:
        os.system(cmd)
        return []

cmd = 'python Convert.py --input_pkl_base test_data/SMPLX_male_2.pkl --input_pkl_src_animation test_data/220923_yogi.pkl --fbx_source_path fbx_path/SMPL_m_unityDoubleBlends_lbs_10_scale5_207_v1.0.0.fbx --output_base output_path/outfile.fbx'
run_cmd(cmd)
print('complete')