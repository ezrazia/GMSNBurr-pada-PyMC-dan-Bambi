import pymc as pm
import numpy as np
import pandas as pd
import pytensor.tensor as at
import arviz as az
import bambi as bmb
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
import math

from pytensor.tensor import gammaln, switch, isinf
from scipy.special import gammaln as np_gammaln
from typing import Optional, Tuple
from pymc.distributions.dist_math import check_parameters