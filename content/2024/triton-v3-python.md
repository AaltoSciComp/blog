---
blogpost: true
date: 2024-04-16
author: Richard Darst
category: triton, triton-v3, python, jupyter
---

# Triton v3: Python and Jupyter

*This post will be updated with additional info, as people ask questions to us.*

This blog post describes how to migrate to Triton V3, if you use Python or Jupyter. Read more about the migration at {doc}`/2024/triton-v3`.  Our main documentation at scicomp.aalto.fi is in the progress of being updated (and may not be fully updated yet).


## Generic Python

The `anaconda` module is replaced with `scicomp-python-env` (the previous module wasn't default Anaconda anyway).

This module is a generic environment that has many common packages inside of it.  We can install some more packages here, but for advanced use you should make your own conda environments.


## Conda environments

Quick reference: {ref}`ref-conda`

Old conda environments *might* still work, but in case of any problems reinstalling the environment is the recommended way of fixing problems. In general, we would recommend to export the environment and reinstall it to avoid unexpected side effects (especially if additional pip packages were installed)

You will also have to re set up your conda configuration (see [here](https://scicomp.aalto.fi/triton/apps/python-conda/#first-time-setup))
Instead of using `miniconda` one should load the module `mamba` for loading and creation of other environments.  This is a minimal environment with just conda and mamba and in it:

```console
$ module load mamba
$ mamba env create -f environment.yaml
$ source activate NAME
```

Remember, `mamba` is a drop-in replacement for `conda`, but has a much faster dependency resolution algorithm.  They can be used together.


## Virtual environments

Virtual environments need to recreated, since the Python interpreter they depend on will change.


## JupyterHub

Triton JupyterHub won't continue.  Instead, a similar environment is available in Open OnDemand.  The v3 Open OnDemand is available at https://ondemand.triton.aalto.fi/ .

By using the "Jupyter" interactive app, you can start a Jupyter environment equivalent to the old JupyterHub (comes with pre-installed kernels, you can install your own kernels).  In the future, it will be possible to run Jupyter in your own environments.

The biggest known issue is that Open OnDemand isn't yet available outside of Aalto networks (VPN must be used).  If this is important to you, please let us know.
