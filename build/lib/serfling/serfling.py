import numpy as np


class MatrixRegression:
    """Matrix Regression Object."""

    def __init__(self, data: list[int], degree: int = 1, omegas: list[int] = [52]):
        """
        Initiates the regression object.

        data.     Time-series record of the number of infectives;
        degree.   Degree of regression;
        omegas.   Omega values for the cycles.

        Example.  MatrixRegression(
                    [...data...],
                    1,
                    [26, 52]
                  )
        """

        self.data = data
        self.degree = degree
        self.omegas = omegas

        assert isinstance(data, list) and all(isinstance(x, (int, float)) for x in data), \
               "Data is not appropriate. Ref help"
        assert type(degree) == int and degree >= 1, "Invalid n. Ref help(MatrixRegression)"
        assert isinstance(omegas, (list, tuple)) and all(isinstance(x, (int, float)) for x in omegas), "Invalid omegas. Ref help(MatrixRegression)"

    def __repr__(self):
        """Representation."""

        return "MatrixRegression(...data..., " + \
               str(self.degree) + ", " + \
               str(self.omegas) + ")"

    def solve(self):
        """Solves the regression problem."""

        self.n = len(self.data)
        self.A = np.array([self._tuple(t) for t in range(1, self.n+1)])
        self.b = np.array(self.data)

        return np.linalg.pinv(self.A.T @ self.A) @ (self.A.T @ self.b)

    def _tuple(self, t):
        return tuple((t**i for i in range(self.degree + 1))) + \
               sum([(np.cos(2*np.pi*t/omg), np.sin(2*np.pi*t/omg)) for \
                    omg in self.omegas], ())

    def interpret(self):
        """Interpretation."""

        print(f"The first {self.degree+1} term/s is/are the polynomial\
            \nregression coefficients. Following that, there is/are {len(self.omegas)}\
            \npair/s of coefficients corresponding to the respective pairs\
            \nof sin and cos terms.")
