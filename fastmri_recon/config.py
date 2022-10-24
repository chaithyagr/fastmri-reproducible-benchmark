"""Module containing the path to the data, the logs and the model weights
"""
import os

def get_set_env(env, var):
    # Gets variable from environment, else sets var to env
    env_var = os.environ.get(env, var)
    os.environ[env] = env_var
    return env_var

DATA_DIR = get_set_env('FASTMRI_DATA_DIR', os.path.join(os.environ.get('SCRATCH'), 'DATA'))
FASTMRI_DATA_DIR = get_set_env('FASTMRI_DATA_DIR', os.path.join(os.environ.get('SCRATCH'), 'DATA'))
OASIS_DATA_DIR = get_set_env('OASIS_DATA_DIR', os.path.join(os.environ.get('SCRATCH'), 'DATA', 'OASIS_tfrecords'))
LOGS_DIR = get_set_env('LOGS_DIR', '/volatile/Chaithya/Networks/LogDir')
CHECKPOINTS_DIR = get_set_env('CHECKPOINTS_DIR', '/volatile/Chaithya/Networks/')
OUT_DIR = get_set_env('OUT_DIR', '/volatile/Chaithya/Networks/')

n_volumes_train = 973
n_volumes_val = 199
n_volumes_test = {
    4: 50,
    8: 58,
}

brain_volumes_per_contrast = {
    'train': {
        'AXFLAIR': 344,
        'AXT1POST': 949,
        'AXT1PRE': 250,
        'AXT1': 248,
        'AXT2': 2678,
    },
    'validation': {
        'AXFLAIR': 107,
        'AXT1POST': 287,
        'AXT1PRE': 77,
        'AXT1': 92,
        'AXT2': 815,
    },
    'test': {
        4: {
            'AXFLAIR': 24,
            'AXT1POST': 54,
            'AXT1PRE': 17,
            'AXT1': 16,
            'AXT2': 170
        },
        8: {
            'AXFLAIR': 25,
            'AXT1POST': 68,
            'AXT1PRE': 19,
            'AXT1': 13,
            'AXT2': 152
        },
    }
}

brain_n_volumes_train = 4469
brain_n_volumes_validation = 1378
brain_n_volumes_test = {
    4: 281,
    8: 277,
}
