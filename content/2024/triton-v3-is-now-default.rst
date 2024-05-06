:blogpost: true
:date: 2024-05-06
:author: Richard Darst
:category: triton


Triton v3 is now default
========================

Triton has a major update.  You can read our previous info about this at
:doc:`/2023/preparing-for-new-triton`, and our "what has changed" in
`Triton issue #1593 <https://version.aalto.fi/gitlab/AaltoScienceIT/triton/-/issues/1593>`__.


What is Triton v3
-----------------

It has the same name, and importantly the same user accounts and data,
but all the software and operating system is changed.  In particular:

* All software modules are different
* Any software which has been complied will need to be re-compiled.


Why, and why now?
-----------------

Triton's previous operating system was released in 2014.  Security
support runs out at the end of 2024 May, and it *has* to be updated.
Stability is good for research, so we try to reduce the number of
changes (compare)

We realize that a change is very disruptive and painful, especially
since the expectation is that Triton never changes.  But an old
operating system makes problem for users too, and they have gotten
more and more over the years.


What to do
----------

Most of the transition for different types of software is described in
`Triton issue #1593
<https://version.aalto.fi/gitlab/AaltoScienceIT/triton/-/issues/1593>`__.


FAQ
---

* **Why are all software modules different?  Everything I need is
  missing or changed.**

  If we update the base operating system, then all compiled software
  needs to be updated.  We have modules that are almost a decade old,
  and we can't re-install them all automatically.  We don't know which
  ones are needed.  We reinstalled things which people had asked for
  in advance, and will continue to install things which are requested.

* **Anaconda / conda are missing**

  Before there was a big mix-up with anaconda (the distribution),
  anaconda (the module with lots of stuff we had installed, that was
  different from the distribution), and conda (the package manager).
  We have tried to make the following arrangement:

  * module load ``python-scicomp-env`` for the common software
    packages people need.  It doesn't include the ``conda`` or
    ``mamba`` commands.

  * ``module load mamba`` for ``mamba`` (and ``conda``) to create new
    environments.
