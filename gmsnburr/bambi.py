import pymc as pm
import bambi as bmb
from .pymc import GMSNBurr

pm.GMSNBurr = GMSNBurr

likelihood = bmb.Likelihood(
    "GMSNBurr",
    params=["mu", "sigma", "alpha1", "alpha2"],
    parent="mu")

priors = {"sigma": bmb.Prior("HalfCauchy", beta=2),
          "alpha1": bmb.Prior("Lognormal", mu=0.5, sigma=0.5),
          "alpha2": bmb.Prior("Lognormal", mu=0.5, sigma=0.5)}

family = bmb.Family("GMSNBurr", likelihood, bmb.Link("identity"))

bmb.Family.set_default_priors(family, priors)