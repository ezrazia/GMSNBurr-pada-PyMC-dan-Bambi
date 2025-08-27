# GMSNBurr Distribution for PyMC and Bambi

This repository provides the implementation of the **GMSNBurr** (Generalized Modified to be Stable as Normal from Burr) distribution, designed for seamless integration with the probabilistic programming libraries **PyMC** and **Bambi**.

---

## 🚀 Getting Started

Follow these steps to install and use the GMSNBurr distribution in your own projects.

### 1. Installation

You can install the package directly from this GitHub repository using `pip`:

```bash
pip install git+https://github.com/ezrazia/GMSNBurr-pada-PyMC-dan-Bambi.git
```

### 2. Usage Examples

Once installed, you can import the `GMSNBurr` class and use its methods for various statistical tasks.

#### Basic Import

```python
from gmsnburr import GMSNBurr
```

#### Key Features

The `GMSNBurr` class provides static methods to perform common operations.

* **`.pdf()`**: Calculate the Probability Density Function.
* **`.cdf()`**: Calculate the Cumulative Distribution Function.
* **`.random()`**: Draw random samples from the distribution.

```python
# Define some parameters
mu, sigma, alpha1, alpha2 = 0, 1, 2, 2
x_values = np.linspace(-5, 5, 100)

# 1. Calculate the PDF
pdf_values = GMSNBurr.pdf(x=x_values, mu=mu, sigma=sigma, alpha1=alpha1, alpha2=alpha2)

# 2. Calculate the CDF
cdf_values = GMSNBurr.cdf(x=x_values, mu=mu, sigma=sigma, alpha1=alpha1, alpha2=alpha2)

# 3. Generate 500 random samples
random_samples = GMSNBurr.random(size=500, mu=mu, sigma=sigma, alpha1=alpha1, alpha2=alpha2)
```

#### Integration with PyMC

Use `GMSNBurr` as a custom distribution within a PyMC model.

```python
import pymc as pm

with pm.Model() as model:
    # Define priors
    mu = pm.Normal("mu", mu=0, sigma=1)
    sigma = pm.LogNormal("sigma", sigma=1)
    alpha1 = pm.LogNormal("alpha1", sigma=3)
    alpha2 = pm.LogNormal("alpha2", sigma=3)

    # Define likelihood
    y = GMSNBurr("y", mu=mu, sigma=sigma, alpha1=alpha1, alpha2=alpha2, observed=your_data)
```

#### Integration with Bambi

This distribution is also registered as a family in Bambi, allowing for easy use in generalized linear models.

```python
import bambi as bmb

# Assume 'data' is a pandas DataFrame with columns 'y' and 'x'
model = bmb.Model("y ~ x", data=your_data, family="gmsnburr")
results = model.fit()
```

For a more comprehensive tutorial, please see the `example.ipynb` notebook in the `examples` folder.

---

## 👨‍💻 Reference and the Author

This work is based on the following research:

* Choir, A. S. (2020). *Distribusi Neo-Normal Baru dan Karakteristiknya*. Institut Teknologi Sepuluh Nopember.

**Author**: Ezra Zia Izdihara

