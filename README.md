# Step 2 - Create virtual environment

To create a new virtual enviroment using `virtualenvwrapper` run:

    mkvirtualenv cloudify-systemd --python /usr/bin/python2

after that, create a `requirements.txt` file that contain `cloudify==3.4` and
install it:

    pip install -r requirements.txt

Whenever you're ready, the next task is:

    Write a basic blueprint file that contains:
        - a `systemd` node type that derives from `cloudify.nodes.SoftwareComponent`
        - a `vagrant_vm` node template of type `cloudify.nodes.Compute`
        - a `mongo_db` node template of type `systemd`

Once you're done, please check out `step-03` branch to compare with the provided
solution and get instructions for the next step.

Hints:
- [Node types documentation](http://docs.getcloudify.org/3.4.0/blueprints/spec-node-types/)
- [Node templates documentation](http://docs.getcloudify.org/3.4.0/blueprints/spec-node-templates/)
