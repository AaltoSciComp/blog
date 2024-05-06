:blogpost: true
:date: 2024-05-06
:author: Richard Darst
:category: triton


Triton v3 SSH host key warnings
===============================

When updating Triton, many users will get a message like this (or
similar things if you use other SSH clients like PuTTY):

::

   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
   Someone could be eavesdropping on you right now (man-in-the-middle attack)!
   It is also possible that a host key has just been changed.


What it means
-------------

SSH (Secure SHell) is made to be secure, and that means one it
verifies the server you are connecting **to** via its **ssh host
key**.  The representation of this key is the **fingerprint**, like
``SHA256:OqCehC2lbHdl8mYGI/G9vlxTwew3H3KrvxKDkwIQy9Y``.  This means
that the NSA or someone can't intercept the connecting and get your
password by pretending to be Triton.  This is a good thing.

OpenSSH (the command line program on Linux, MacOS, Windows) saves
these connection IDs (fingerprints) in
``$HOME/.ssh/authorized_keys``.  Other programs may store the keys
somewhere else.


What you should do when you see the warning
-------------------------------------------

The warning looks scary but the first thing to ask is "should the
server I am connecting to have changed?".  If you have been directed
to this blog post, then probably yes, it has.  You should *always*
think if the fingerprint should change, and if there is no reason for
them to have changed, contact your administrators.  You can usually
verify the keys online, for example
:external:doc:`triton/usage/ssh-fingerprints`.

If you are on command line OpenSSH (Linux), it will propose a command
that will remove the old host key:

.. code-block:: console

  $ ssh-keygen -R "triton.aalto.fi"

For other programs, follow whatever prompts it might give to replace
the host key fingerprint.

What are the current SSH keys?
------------------------------

When you get a "The authenticity of host 'triton.aalto.fi' can't be
established", verify the SSH key fingerprints that are presented, then
click "yes" to permanently save them (until they change next, they can
always be updated).  The fingerprints for Triton v3 are::

  3072 SHA256:3u8iICwjmvJ/+9YGxqqK+3r7FmrDflcgpoGl5ygtAWw login4.triton.aalto.fi (RSA)
  256 SHA256:OqCehC2lbHdl8mYGI/G9vlxTwew3H3KrvxKDkwIQy9Y login4.triton.aalto.fi (ECDSA)
  256 SHA256:ibL4dBsdrwRjbJCBWL1J5p/Sg4PGHWxTG6HF65yPcps login4.triton.aalto.fi (ED25519)
