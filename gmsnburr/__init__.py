from .pymc import GMSNBurr
from .bambi import family as _bambi_family
from .dist import pdf_gmsnburr, cdf_gmsnburr, random_gmsnburr

GMSNBurr.family = _bambi_family
GMSNBurr.pdf = staticmethod(pdf_gmsnburr)
GMSNBurr.cdf = staticmethod(cdf_gmsnburr)
GMSNBurr.random = staticmethod(random_gmsnburr)

__all__ = ["GMSNBurr"]