# Step 5 - Add inputs to connect to SSH

The `Vagrantfile` configuration has been updated to make sure that the VM
always gets the same IP address:

```ruby
config.vm.network "private_network", ip: "192.168.33.10"
```

this will be useful to connect to the VM through SSH.

After the configuration update, please keep in mind to restart the VM with these commands:

    vagrant halt
    vagrant up

The inputs needed to connect to the vagrant VM have been set as follows:

```json
{
  "host_ip": "192.168.33.10",
  "ssh_user": "vagrant",
  "ssh_private_key_path": ".vagrant/machines/default/virtualbox/private_key"
}
```

where the `host_ip` value is the same one set for vagrant.

The schema for the values in the input file has been added to `blueprint.yaml`.

Note that the cloudify environment now needs to be initialized with the inputs
file to avoid validation errors:

    cfy local init -p blueprint.yaml -i inputs.json

Whenever you're ready, the next task is:

    - Implement scripts to start/stop a service named `service_name` using
      `systemctl`
    - Update `systemd` node type to call the scripts for the start/stop
      lifecycle operations using the fabric plugin
    - Verify that the scripts are indeed called when the install/uninstall
      workflows are executed

Once you're done, please check out `step-06` branch to compare with the provided
solution and get instructions for the next step.

Hints:
- [Fabric plugin documentation](http://docs.getcloudify.org/3.4.0/plugins/fabric/)
- [Built-in workflows documentation](http://docs.getcloudify.org/3.4.0/workflows/built-in-workflows/)
