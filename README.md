# Step 8 - Implement create/delete operations for mongod service

The scripts to create/delete mongod service have been added to the `scripts`
directory. The blueprint has been updated to run those scripts for the
create/delete operations in the same way the install/uninstall scripts are
called in the `systemd` node type definition.

Now the install/uninstall scripts should work as expected because the
create/delete ones take care of the service file.

As you will see, there's a new `app.py` script in the `scripts` folder. This is
a simple flask-based server that will be integrated to run through systemd.

Whenever you're ready, the next task is:

    - Implement the create/delete operations for the `app.py` script. Note that
      what those operations should is is just install/uninstall `flask`.

Once you're done, please check out `step-09` branch to compare with the provided
solution and get instructions for the next step.

Hints:
- [Built-in workflows documentation](http://docs.getcloudify.org/3.4.0/workflows/built-in-workflows/)
