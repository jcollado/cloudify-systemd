# Step 7 - Move node type definition to separate file

A new file with the node type definition can be found in `types/systemd.yaml`.
The `blueprint file is now more concise and easy to read.

Whenever you're ready, the next task is:

    - Implement the create/delete lifecycle operations for the `mongod`
      template, so that service file is available when the start/stop
      operations are executed.

Once you're done, please check out `step-08` branch to compare with the provided
solution and get instructions for the next step.

Hints:
- [Built-in workflows documentation](http://docs.getcloudify.org/3.4.0/workflows/built-in-workflows/)
