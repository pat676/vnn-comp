'''
Computation Settings. Change settings by assigning directly to the class attributes.

For example:
Settings.TIMEOUT = 10
'''

import os

from nnenum.util import FreezableMeta

class Settings(metaclass=FreezableMeta):
    '''enumeration settings. Access these using, for example, Settings.TIMEOUT

    These get initialized by the metaclass to the values in the reset() class method.
    '''

    BRANCH_OVERAPPROX, BRANCH_EGO, BRANCH_EGO_LIGHT, BRANCH_EXACT = range(4) # used for BRANCH_MODE
    SPLIT_LARGEST, SPLIT_ONE_NORM, SPLIT_SMALLEST, SPLIT_INORDER = range(4) # used for SPLIT_ORDER

    @classmethod
    def reset(cls):
        'assign default settings'

        # settings / optimizations
        cls.NUM_PROCESSES = len(os.sched_getaffinity(0)) # use multiple cores
        cls.TIMEOUT = None # verification timeout, in seconds (None = no timeout)

        cls.SINGLE_SET = False # only do single-set overapproximation (no splitting)

        cls.PRINT_OUTPUT = True # print anything to stdout? (controls all output)

        cls.RESULT_SAVE_POLYS = False # save 2-d projections of output polygons to Result.polys?
        cls.RESULT_SAVE_POLYS_DIMS = (0, 1) # (x_dim, y_dim) of 2-d projections, used if RESULT_SAVE_POLYGONS is True

        cls.RESULT_SAVE_STARS = False # save LpStar objects in result?

        cls.RESULT_SAVE_TIMERS = [] # list of timers to record in Result.timers; TIMING_STATS must be True

        cls.FIND_CONCRETE_COUNTEREXAMPLES = True # should we try to find concrete counterexamples if spec violated?

        #########################
        ### advanced settings ###
        cls.PRINT_PROGRESS = True # print periodic progress updates
        cls.PRINT_INTERVAL = 0.1 # print interval in seconds (0 = no printing)
        cls.TIMING_STATS = False # compute and print detailed timing stats

        cls.CHECK_SINGLE_THREAD_BLAS = True
        
        cls.UPDATE_SHARED_VARS_INTERVAL = 0.05 # interval for each thread to update shared state

        cls.COMPRESS_INIT_BOX = True

        cls.EAGER_BOUNDS = True
        
        cls.CONTRACT_ZONOTOPE = False # try domain contraction on zonotopes (more accurate prefilter, but slower)
        cls.CONTRACT_ZONOTOPE_LP = False # contract zonotope using LPs (even more accurate prefilter, but even slower)

        cls.CONTRACT_OVERAPPROX_VIOLATION = False # contract from overapproximation violation?

        # the types of overapproximation to use in each round
        cls.OVERAPPROX_TYPES = [['zono.area'],
                                ['zono.area', 'zono.ybloat', 'zono.interval'],
                                ['zono.area', 'zono.ybloat', 'zono.interval', 'star.lp']]

        cls.OVERAPPROX_NEAR_ROOT_MAX_SPLITS = 2
        cls.OVERAPPROX_TYPES_NEAR_ROOT = cls.OVERAPPROX_TYPES

        cls.OVERAPPROX_CONTRACT_ZONO_LP = True # contract LP during overapproximation steps?
        cls.OVERAPPROX_GEN_LIMIT_MULTIPLIER = 1.5 # don't try approx star if multizono.gens > THIS * last_safe_gens
        cls.OVERAPPROX_MIN_GEN_LIMIT = 50 # minimum generators to use as cap
        cls.OVERAPPROX_LP_TIMEOUT = 1.0 # timeout for LP part of overapproximation
        cls.OVERAPPROX_BOTH_BOUNDS = False # should overapprox star method compute both bounds or just reject branches?

        cls.SAVE_BRANCH_TUPLES_FILENAME = None
        cls.SAVE_BRANCH_TUPLES_TIMES = True # when saving branch tuples, also include runtimes
        cls.BRANCH_MODE = cls.BRANCH_OVERAPPROX
        cls.PRINT_BRANCH_TUPLES = False

        cls.TRY_QUICK_OVERAPPROX = True
        cls.QUICK_OVERAPPROX_TYPES = [['zono.area'],
                                      ['zono.area', 'zono.ybloat', 'zono.interval']]

        # one_norm is especially good at finding counterexamples
        cls.SPLIT_ORDER = cls.SPLIT_ONE_NORM # rearrange splitting order within each layer
        
        cls.RESULT_SAVE_POLYS_EPSILON = 1e-7 # accuracy of vertices when projecting polygons for Kamenev method

        cls.OFFLOAD_CLOSEST_TO_ROOT = True # when offloading work to other threads, use stars closest to root of search

        cls.SPLIT_TOLERANCE = 1e-8 # small outputs get rounded to zero when deciding if splitting is possible
        cls.TEST_FUNC_BEFORE_ASSIGNMENT = None # function to call before eager assignement, used for unit testing

        cls.SPLIT_IF_IDLE = True # force splitting (rather than overapproximation) if there are idle processes

        cls.SHUFFLE_TIME = None # shuffle star sets after some time (improves unsafe specs)

        ####
        cls.NUM_LP_PROCESSES = 1 # if > 1, then force multiprocessing during lp step
        cls.PARALLEL_ROOT_LP = True # near the root of the search, use parallel lp, override NUM_LP_PROCESES if true

        ####
        # generally it should be safe to add any linear layers to the whitelist
        cls.ONNX_WHITELIST = ['Add', 'AveragePool', 'Constant', 'Concat', 'Conv', 'Flatten', 'Gather', \
                              'Gemm', 'MatMul', 'Mul', 'Reshape', 'Relu', 'Shape', 'Sub', 'Unsqueeze']

        cls.ONNX_BLACKLIST = ['Atan', 'MaxPool', 'Sigmoid', 'Tanh'] # unsupported nonlinear laters

        ###
        # settings for adversarial generation
        cls.ADVERSARIAL_TRY_QUICK = True # if settings are provided, try quick adversrial generation at start
        cls.ADVERSARIAL_QUICK_NUM_ATTEMPTS = 10 # how many attempts
        cls.ADVERSARIAL_IN_WORKERS = True # do lots of attempted adversarial generation until more work is produced
        cls.ADVERSARIAL_WORKERS_MAX_ITER = 100 # how many attempts workers should make
        cls.ADVERSARIAL_FROM_ABSTRACT_VIO = False # try adversarial examples from abstract violations

        
        cls.ADVERSARIAL_ONNX_PATH = None # path to .onnx file with corresponidng .onnx.pb file
        cls.ADVERSARIAL_EPSILON = None
        cls.ADVERSARIAL_ORIG_IMAGE = None
        cls.ADVERSARIAL_ORIG_LABEL = None
