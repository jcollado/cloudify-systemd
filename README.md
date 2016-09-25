# cloudify-systemd

In this exercise, you're going to write a new node type that takes care of
starting/stopping a given service using `systemd`.

The node type will be tested using a cloudify 3.4 in local mode with a
blueprint that provides a node templates that use this node type to launch
services in a VM.

The exercise has been splitted in multiple small tasks that you'll need to
follow and once completed you can compare against the provided solution by
switching to the next branch.

Whenever you're ready, the first task is as follows:

    Create a VM based on CentOS using vagrant.

Once you're done please check out `step-01` branch to compare with the provided
solution and get instructions for the next step.

Hints:

- [Vagrant init documentation](https://www.vagrantup.com/docs/cli/init.html)
