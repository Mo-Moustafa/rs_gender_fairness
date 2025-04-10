# Thresholds for evaluation
LEVELS = [
    1,
    3,
    5,
    10,
    20,
    50,
]

# Which demographic trait to consider
DEMO_TRAITS = [
    'gender'
]

EXP_SEED = 101315  # Seed for algorithms that rely on random initialization

# Parameters for VAE
VAE_MAX_EPOCHS = 100
VAE_LOG_VAL_EVERY = 5

# Saving path
# Structure is lfm2b_res/{ algorithm name }/{ experiment type }--{ date and time }/(val-test)/{ seed or fold_n }
LOG_VAL_STR = '../../lfm2b_res/{}/{}--{}/val/{}'
LOG_TE_STR = '../../lfm2b_res/{}/{}--{}/test/{}'

DATA_PATH = 'data/inter.tsv'
DEMO_PATH = 'data/demo.tsv'
TRACKS_PATH = 'data/tracks.tsv'

DOWN_DATA_PATH = ''
DOWN_DEMO_PATH = ''

OUT_DIR = 'results/{}/'