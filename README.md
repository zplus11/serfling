# serfling

Regression by matrix approach for the serfling's flu model. At time $t$, the number of infectives is given by

$$f(t) = \sum_{i=0}^d a_it^i + \sum_{i=1}^r \Bigg(b_i\cos\left(\frac{2\pi t}{\omega_i}\right) + c_i\sin\left(\frac{2\pi t}{\omega_i}\right)\Bigg)$$

where $d$ is the degree upto which you wish to consider the polynomial terms, $r$ is the number of pairs of $\sin$ and $\cos$ terms corresponding to cycle lengths $\omega_1,\omega_2,\ldots,\omega_r$, and $a_i,b_i,c_i$'s are regression coefficients.

### Installation

Install the package by running

```
pip install git+"https://github.com/zplus11/serfling"
```

### Usage

Sort out your dataset. Usually, it should look like this:

```py
>>> data = [169, 168, 158, 136, ..., 13, 31, 29, 32, 45]
```

Or if it is in a csv file,

```py
>>> with open("data.csv", "r") as file:
...     read = csv.reader(file)
...     data = [row[0] for row in read] # assuming data is in the first col
```

Import the package and estimate the parameters:

```py
>>> from mreg import MatrixRegression

>>> degree = 1
>>> omegas = [26, 52]

>>> mr = MatrixRegression(data, degree, omegas)
>>> mr.solve()
array([ 787.28656043,   -2.62617957, -345.25924634, -325.31274084,
         76.24631779, -278.56634957])
```

which are the required regression coefficients.

---

See LICENSE
