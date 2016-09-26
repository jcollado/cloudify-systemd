# Step 4 - Add property to node type

The `service_name` property can be seen in the `blueprint.yaml` file as
follows:

```yaml
properties:
    service_name:
        type: string
        description: systemd service name
```

Note that the `mongod` node template has been updated as well to set the
property value to `mongod` which is the service name that will be needed to
launch MongoDB later.

Whenever you're ready, the next task is:

    - Update vagrant configuration to ensure that the vagrant VM always gets
      the same IP address
    - Add `inputs.json` file with values for `host_ip`, `ssh_user` and
      `ssh_private_key_path` suitable to connect to the vagrant VM
    - Add input section to blueprint that defines the schema for those inputs

Once you're done, please check out `step-05` branch to compare with the provided
solution and get instructions for the next step.

Hints:
- [Static IP configuration documentation](https://www.vagrantup.com/docs/networking/private_network.html#static-ip)
- [Inputs documentation](http://docs.getcloudify.org/3.4.0/blueprints/spec-inputs/)
