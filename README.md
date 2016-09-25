# Step 1 - Create Vagrant VM

To create a new VM with vagrant based on CentOS, run:

    vagrant init centos/7

This generates the `Vagrantfile` that you'll find included in this repository.
After that the VM can be booted up with:

    vagrant up

Whenever you're ready, the next task is:

    Setup your development environment to be able to run cloudify locally:
        - make a virtual environment
        - install cloudify 3.4

Once you're done, please check out `step-02` branch to compare with the provided
solution and get instructions for the next step.

Hints:

- [mkvirtualenv documentation](http://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html#mkvirtualenv)
- [cloudify 3.4 in pypi](https://pypi.python.org/pypi/cloudify/3.4)
