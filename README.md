# Step 9 - Implement create/delete operations for app service

The blueprint has been updated to include a node template for the new app
service that will run in the same VM. The scripts to create/delete the app
service dependencies have been added to the `scripts` directory in the same way
the install/uninstall scripts are called in the `systemd` node type definition.

As you probably have noticed, the install/uninstall script don't work for the
`app` service because there is no service file for it. This will be addressed
in the next step.

Whenever you're ready, the next task is:

    - Add a new property named `service_binary_path` to the `systemd` node type
    - Set that property for the `app` node template to the path available in
      the VM through the synced folder
    - Implement the `configure` operation for the `systemd` node type, so that
      a default service file is automatically created when the path to the
      binary is provided.

Once you're done, please check out `step-10` branch to compare with the provided
solution and get instructions for the next step.

Hints:
- [Node type properties documentation](http://docs.getcloudify.org/3.3.1/blueprints/spec-node-types/#properties)
- [Vagrant synced folders documentation](https://www.vagrantup.com/docs/synced-folders/index.html)
- [Built-in workflows documentation](http://docs.getcloudify.org/3.4.0/workflows/built-in-workflows/)
