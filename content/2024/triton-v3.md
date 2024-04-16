---
blogpost: true
date: 2024-04-16
author: Richard Darst
category: triton, triton-v3
---

# Triton v3 is open for testing (main post)

*This post will be updated with additional info, as people ask questions to us.*

We are happy to announce that Triton v3 has begun testing.  V3 will use all of the same hardware and data, but is running a new operating system. This should allow us to solve some of the common problems we have had lately and provide a solid base for future growth.


## What is happening now

As of 9 April 2024, about 20% of current Triton resources (cpu, gpu,
etc) have moved to the v3 operating system. Adventurous users can
begin testing and running jobs here (you might find there are lots of
resources available; maximum job duration is 2 days, though).  The
rest will be migrated shortly, once we are sure things work.  **For
now you can keep using old or new** - we aren't forcing a change right
now, but the day will eventually come.


## Data and paths

**All data and paths are identical.**  If you modify data on one side, it's modified on the other side (the storage systems haven't changed and it's serving both v2 and v3 at the same time).  While it may seem similar, other than data and accounts, the environments of v2 and v3 are fully separate.


## Login to v3

You can login to v3 now, but the default login methods will still take you to v2. Login is via
- SSH to `login4.triton.aalto.fi`
- https://ondemand.triton.aalto.fi (Open OnDemand web interface - note that this is a different address)
- Jupyter (there is no direct replacement in V3 - use Open OnDemand instead where you can find jupyter)

## Software

**All software has been fully reinstalled - this is the hardest point of the transition.**  This means any modules will be different, our provided Python/R/Matlab/etc modules are different, and so on.  Module names may be slightly different - you will need to check and update your workflows.  We'll be adding transition guides for different types of workflows later.
- Python and JupyterHub, see {doc}`/2024/triton-v3-python`
- R: use new modules and re-compile any locally installed packages
- Software you have compieled: you must re-compile, see {doc}`/2024/triton-v3-compiled-software`

Note that we have hierarchical modules (we've added this to v2 already, but it's worth pointing it out again): When you `module spider`, it will tell you what modules you must load *before* you can load other modules.  For example, it will tell you to load the relevant compiler first, and then you can load a module.

The new system is based on a new version of linux: Red Hat Enterprise Linux 9.

Using the cluster should be mostly the same.

## GPUs
For gpu's the slurm notation has been updated.  From now on, use `--gpus=N` and `--gpus=TYPE:N` instead of `--gres=gpu:N`). Check docs for details. We recommend on moving to the new notation asap because it works on v2 also.

We have now split our gpu-partition to multiple partitions. Names of these partitions are:

- `gpu-p100-16g`
- `gpu-v100-16g`
- `gpu-v100-32g`
- `gpu-a100-80g`

Each partition has the corresponding GPU types and thus in future you can choose which GPU to use by submitting your job to the corresponding partitions with e.g. `#SBATCH --partition gpu-v100-32g,gpu-a100-80g`.

Constraints will still work, so you can use those to limit yourself to certain GPU types.

## Reporting problems

If you notice problems, do let us know! It is probably either something that is wrong, or something we need to clarify. **First, check this post for updates.** Then, check the :ref:`issuetracker-general` for a similar problem, then report issues to that tracker:

- missing features or software
- something that is not working
- working differently than you expect

You can use :ref:`chat` for quick questions, but we may be busy so if you don't get a response, make an issue instead.
