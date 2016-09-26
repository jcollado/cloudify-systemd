# Step 6 - Implement start/stop lifecycle operations

The scripts to start/stop a service using `systemd` have been added to
`scripts/systemd` and `blueprint.yaml` has been updated to import the fabric
plugin and call the scripts using it. Note the use of the `dsl_definitions`
section to avoid duplication in the script execution specification.

After the blueprint has been updated, use the following command to install the
fabric plugin:

    cfy local install-plugins -p blueprint.yaml

After the configuration update, please keep in mind to restart the VM with these commands:

    vagrant halt
    vagrant up

After that, you'll be able to execute the scripts for the install/uninstall
workflows as follows:

    cfy local execute -w install
    cfy local execute -w uninstall

The scripts right now will fail because the `mongod` service is not available
in the CentOS, but that will be fixed in a future step.

Whenever you're ready, the next task is:

    - Move the `systemd` node type definition to a separate yaml file, so that
      it can be reused in other blueprints if needed.

Once you're done, please check out `step-07` branch to compare with the provided
solution and get instructions for the next step.

Hints:
- [Imports documentation](http://docs.getcloudify.org/3.4.0/blueprints/spec-imports/)
