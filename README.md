# sacredfig: standard styles for scientific figures in matplotlib

<div align="center">

[![pypi](https://img.shields.io/pypi/v/sacredfig.svg)](https://pypi.org/project/sacredfig/)
[![python](https://img.shields.io/pypi/pyversions/sacredfig.svg)](https://pypi.org/project/sacredfig/)
[![Build Status](https://github.com/cynddl/sacredfig/actions/workflows/tests.yml/badge.svg)](https://github.com/cynddl/sacredfig/actions)
[![codecov](https://codecov.io/gh/cynddl/sacredfig/branch/main/graphs/badge.svg?branch=main)](https://codecov.io/github/cynddl/sacredfig?branch=main)
[![Code Quality](https://img.shields.io/scrutinizer/g/cynddl/sacredfig.svg)](https://scrutinizer-ci.com/g/cynddl/sacredfig/?branch=main)

</div>



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install SacredFig.

```bash
pip install sacredfig
```

## Usage

Simply import the package and use the sacredfig style:

```python
import matplotlib.pyplot as plt
import sacredfig

plt.style.use(sacredfig.style)

fig, ax = plt.subplots(figsize=(4, 4), dpi=150)
ax.grid(False, which='major', axis='x')

ax.plot([0, 1], [0, 1])
ax.set_box_aspect(1)
ax.set(xlabel="x", ylabel="y")
```

You can also use sacredfig temporarily:

```
with plt.style.context(sacredfig.style):
    ax.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')

```