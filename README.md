# Step 11 - Expose ports from VM

The VM configuration has been updated to expose the services ports as follows:

```ruby
config.vm.network "forwarded_port", guest: 27017, host: 27017
config.vm.network "forwarded_port", guest: 5000, host: 5000
```

After the configuration update, please keep in mind to restart the VM with
these commands:

    vagrant halt
    vagrant up

The procedure to verify that the services are indeed running would be:

- Install applications:

        cfy local execute -w install

- Verify that both `mongod` and the flask application are running:

        $ curl localhost:5000
        Hello Cloudify!
        $ curl localhost:27017
        It looks like you are trying to access MongoDB over HTTP on the native driver port.

- Uninstall application:

        cfy local execute -w uninstall

- Verify that neither `mongod` nor the flask application are running:

        $ curl localhost:5000
        curl: (56) Recv failure: Connection reset by peer
        $ curl localhost:27017
        curl: (56) Recv failure: Connection reset by peer
