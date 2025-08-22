from requirements import *

def logp(y: at.TensorVariable,
        mu: at.TensorVariable,
        sigma: at.TensorVariable,
        alpha1: at.TensorVariable,
        alpha2: at.TensorVariable,
        log=True, **kwargs): 

  betaln_val = gammaln(alpha1) + gammaln(alpha2) - gammaln(alpha1 + alpha2)
  lomega = (
      -0.5 * at.log(2 * at.pi)
      + betaln_val
      - alpha2 * (at.log(alpha2) - at.log(alpha1))
      + (alpha1 + alpha2) * at.log1p(alpha2 / alpha1))
  omega = at.exp(lomega)
  zo = -omega * ((y - mu) / sigma)
  zoa = zo + at.log(alpha2) - at.log(alpha1)
  logp = (
      lomega
      - at.log(sigma)
      + alpha2 * (at.log(alpha2) - at.log(alpha1))
      + alpha2 * zo
      - (alpha1 + alpha2) * at.log1p(at.exp(zoa))
      - betaln_val)
  lp = switch(isinf(zo), -at.inf, logp)
  if not log:
    lp = at.exp(lp)
  return check_parameters(lp, alpha1 > 0, alpha2 > 0, sigma > 0, msg='alpha1, alpha2, and sigma must be more than 0')

def logcdf(y: at.TensorVariable,
          mu: at.TensorVariable,
          sigma: at.TensorVariable,
          alpha1: at.TensorVariable,
          alpha2: at.TensorVariable,
          lower_tail=True,
          log=True, 
          **kwargs):

  betaln_val = gammaln(alpha1) + gammaln(alpha2) - gammaln(alpha1 + alpha2)
  lomega = (
      -0.5 * at.log(2 * at.pi)
      + betaln_val
      - alpha2 * (at.log(alpha2) - at.log(alpha1))
      + (alpha1 + alpha2) * at.log1p(alpha2 / alpha1))
  omega = at.exp(lomega)
  epart = at.exp(-omega * ((y - mu) / sigma))
  ep = 1 / (1 + (alpha2 / alpha1) * epart)
  cdf_value = at.betainc(alpha1, alpha2, ep)
  if log:
    final_cdf_value = at.log(cdf_value) if lower_tail else at.log(1 - cdf_value)
  else: 
    final_cdf_value = cdf_value if lower_tail else 1 - cdf_value
  return check_parameters(final_cdf_value, alpha1 > 0, alpha2 > 0, sigma > 0, msg='alpha1, alpha2, and sigma must be more than 0')

def random(
      mu: np.ndarray | float,
      sigma: np.ndarray | float,
      alpha1: np.ndarray | float,
      alpha2: np.ndarray | float,
      rng = np.random.default_rng(),
      size: Optional[Tuple[int]]=None, **kwargs):

  if any(param <= 0 for param in [sigma, alpha1, alpha2]):
    raise ValueError("sigma, alpha1, and alpha2 must be more than 0")
  betaln_val = np_gammaln(alpha1) + np_gammaln(alpha2) - np_gammaln(alpha1 + alpha2)
  lomega = (
      -0.5 * np.log(2 * np.pi)
      + betaln_val
      - alpha2 * (np.log(alpha2) - np.log(alpha1))
      + (alpha1 + alpha2) * np.log1p(alpha2 / alpha1))
  omega = np.exp(lomega)
  z1 = rng.chisquare(2 * alpha1, size=size) / (2 * alpha1)
  z2 = rng.chisquare(2 * alpha2, size=size) / (2 * alpha2)
  logzf = np.log(z2) - np.log(z1)
  random_variate = mu - (sigma / omega) * logzf
  return np.asarray(random_variate)

class GMSNBurr(pm.Continuous):
  def __init__(self, mu, sigma, alpha1, alpha2, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.mu = at.as_tensor_variable(mu)
    self.sigma = at.as_tensor_variable(sigma)
    self.alpha1 = at.as_tensor_variable(alpha1)
    self.alpha2 = at.as_tensor_variable(alpha2)
  @staticmethod
  def main(name: str, mu, sigma, alpha1, alpha2, observed=None, **kwargs):
    return pm.CustomDist(
        name, mu, sigma, alpha1, alpha2,
        logp=logp,logcdf=logcdf, random=random, observed=observed,
        **kwargs)
  @staticmethod
  def dist(mu, sigma, alpha1, alpha2, **kwargs):
    return pm.CustomDist.dist(
        mu, sigma, alpha1, alpha2, 
        logp=logp, logcdf=logcdf, random=random,
        **kwargs)
