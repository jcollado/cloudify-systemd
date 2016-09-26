# Step 10 - Implement configure operation for systemd node type

The configure script is available `scripts/systemd/systemd-configure.py` while
the yaml files for both the `systemd` node type and the example blueprint have
been updated so that a systemd service is generated when needed.

Now the behavior is just as expected, but it's not easy to verify when MongoDB
and the flask application are running. Being able to check that easily will be
the goal of the next step.

Whenever you're ready, the next task is:

    - Update the vagrant configuration file to expose MongoDB and flask
      application ports to be able to check if the services are runnnig from
      the host machine.

Once you're done, please check out `step-11` branch to compare with the provided
solution and get instructions for the next step.

Hints:
- [Vagrant forwarded ports](https://www.vagrantup.com/docs/networking/forwarded_ports.html)
