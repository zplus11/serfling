# mreg

Simple and probably already-existing python package for doing some matrix regression for no reason. **numpy** is a dependency.

### Usage

Sort out your dataset. Usually, it should look like this:

```py
>>> data = [169, 168, 158, 136, 170, 203, 159, 221, 367, 548, 483, 607, 679, 997, 1122, 1187, 1136, 926, 941, 853, 751, 670, 549, 378, 250, 219, 231, 192, 207, 276, 352, 491, 763, 822, 1215, 1533, 1884, 1897, 1553, 1950, 1458, 1176, 812, 627, 470, 321, 345, 371, 358, 271, 185, 181, 153, 134, 165, 171, 181, 171, 248, 277, 466, 653, 888, 930, 1196, 1185, 1117, 1289, 1331, 1112, 946, 796, 738, 506, 433, 279, 186, 130, 162, 142, 159, 96, 86, 99, 146, 154, 86, 360, 521, 710, 829, 2148, 1536, 1706, 1580, 1229, 1269, 1454, 1444, 1220, 1097, 1114, 1022, 734, 493, 464, 300, 243, 163, 91, 77, 53, 57, 44, 22, 28, 22, 13, 31, 29, 32, 45]
```

Or if it is in a csv file,

```py
>>> with open("data.csv", "r") as file:
...     read = csv.reader(file)
...     data = [row[0] for row in read] # assuming data is in the first col
```

Then, it is only a matter of

```py
>>> from mreg import MatrixRegression

>>> degree = 1
>>> pairs = 2
>>> omegas = [26, 52]

>>> MatrixRegression(data, degree, pairs, omegas)
MatrixRegression(...data..., 1, 2, [26, 52])
>>> _.solve()
array([ 787.28656043,   -2.62617957, -345.25924634, -325.31274084,
         76.24631779, -278.56634957])
```

-

See LICENSE