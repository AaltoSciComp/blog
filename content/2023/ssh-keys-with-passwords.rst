:blogpost: true
:date: 2023-09-24
:author: Richard Darst
:category: aalto


Aalto public servers requiring passwords with SSH keys
======================================================

From 2023-09-25, publicly accessible Aalto server login is changing
and will now require a password in addition to SSH keys.  This will
have a significant usability impact on some users.  This post is made
as a landing page for users who need immediate, practical help and for
whom the `aalto.fi page
<https://www.aalto.fi/en/news/ssh-connections-to-public-linux-servers-from-outside-the-aalto-network-will-require-both-a-password>`__
isn't findable or detailed enough.  The official contact is the `IT
Services service desk
<https://www.aalto.fi/en/services/it-service-desk-contact-information-and-service-hours>`__

The reference page :external:doc:`scicomp/ssh` has been updated to
include detailed reference information for every common operating
system and SSH client.  Secure Shell is one of the standard methods of
connecting to remote servers and it is important that users of all
skill levels are able to use it securely.

This change is *not* from Science-IT, but since it will affect many of
our users but is not being publicized or supported very much, we are
preemptively doing some major user support.



What's happening
----------------

What is **not** happening is: requiring locally encrypted SSH keys (although this is highly recommended).

What **is** happening: When you connect to an SSH server from outside
Aalto networks, you will need to have an SSH key set up **and** send
your Aalto password to the remote server interactively.


What to do
----------

If you already have a SSH key set up, you'll start to be asked to
enter a password every time you connect.

You can always connect to the Aalto VPN in advance to prevent this,
but this doesn't work in all cases.

If you do not have a SSH key set up, you should:

- Follow :external:doc:`scicomp/ssh` to generate a SSH key - we have
  *heavily* revised this page to cover almost every common SSH
  arrangement.

- Place your SSH key on any common Aalto server (``kosh``, etc. -
  *not* Triton since that doesn't share home directories with the
  public servers)

  - You could connect by VPN, and then use normal password to connect
    and add the key.

  - You could use https://vdi.aalto.fi with a Linux computer to place
    the key.

  - You could place the key while on an Aalto network (as usual, this
    means ``eduroam`` or ``aalto`` *only* from an Aalto computer).

  - You could use another computer that's already set up with a SSH
    key to place the key.

- The key will then be available on all common Aalto shell servers
  (and other workstations), since they share the home directory.

- Re-read :external:doc:`scicomp/ssh`, in particular the
  :external:ref:`ssh-agent`, :external:ref:`proxyjump` and
  :external:ref:`ssh-multiplex` sections, to see how to configure your
  SSH to minimize the number of times you need to enter passwords.



Motivations
-----------

This was needed for security as evidenced by recent history.
Password-only login is simply not feasible anymore (nor for some
time).  Removing passwords as an option is good security practice that
most organizations should adopt these days.

But why a ssh key *and* remote password instead of a properly
encrypted SSH key?  A SSH key requires something you have (the key)
and something you know (the password), doesn't it?  And doesn't
require sending a plaintext password to the remote server.  This was
decided by whoever is setting this up, probably partly due to the
fact that it is not possible to enforce passwords on SSH keys via
the server config.

In general (outside of Aalto), you should use SSH keys everywhere and
be suspicious of ever sending plaintext passwords to remote servers
(even in conjunction with a SSH key).  Security is important, and by
using SSH keys with a local password you are doing your part.



This is affecting important workflows
-------------------------------------

We apologize for the difficulty in getting work done and want to help
you as much as possible (though Science-IT was *not* the ones that
designed this or communicated it).

There are, unfortunately, some trivial workarounds that involve
putting your password in plain text on your computer to script things.
However, please note that writing passwords down (outside of password
managers) is bad security practise and against the `Aalto password guidelines
<https://www.aalto.fi/en/services/password-guidelines>`__. It is better to
:external:doc:`contact us <help/garage>` to
help design a better and more secure workflow, or ask `IT Services
<https://www.aalto.fi/en/services/it-services>`__ and ask them to
consider other use cases.
