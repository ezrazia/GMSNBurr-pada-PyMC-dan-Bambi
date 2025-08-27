from .pymc import logp, logcdf, random, GMSNBurr
import numpy as np
import pymc as pm
import pytensor.tensor as at

def pdf_gmsnburr(x, mu, sigma, alpha1, alpha2, *kwargs):
    x = np.asarray(x)
    x_var = at.scalar("x")
    rv = GMSNBurr.dist(mu=mu, sigma=sigma, alpha1=alpha1, alpha2=alpha2)
    logp = pm.logp(rv, x_var)
    logp_fn = pm.compile([x_var], logp)
    if x.ndim == 0:
        return np.exp(logp_fn(x))
    else:
        return np.exp([logp_fn(xi) for xi in x])

def cdf_gmsnburr(x, mu, sigma, alpha1, alpha2, *kwargs):
    x = np.asarray(x)
    x_var = at.scalar("x")
    rv = GMSNBurr.dist(mu=mu, sigma=sigma, alpha1=alpha1, alpha2=alpha2)
    logcdf = pm.logcdf(rv, x_var)
    logcdf_fn = pm.compile([x_var], logcdf)
    if x.ndim == 0:
        return np.exp(logcdf_fn(float(x)))
    else:
        return np.exp([logcdf_fn(float(xi)) for xi in x])

def random_gmsnburr(size, mu, sigma, alpha1, alpha2, rng=None, *kwargs):
    rv = GMSNBurr.dist(mu=mu, sigma=sigma, alpha1=alpha1, alpha2=alpha2)
    rng = np.random.default_rng() if rng is None else rng
    samples = pm.draw(rv, draws=size, random_seed=rng)
    return np.asarray(samples)