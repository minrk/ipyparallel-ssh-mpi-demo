# local:.ipython/profile_remotempi/ipcluster_config.py
c = get_config()  # noqa
# tell it to launch the controller via ssh
c.Cluster.controller_launcher_class = "ssh"
# the host to ssh to
c.SSHControllerLauncher.hostname = "remote"
# tell the controller to listen on all ips, so the client can connect to it
# (alternately, use ssh tunneling from the client)
c.Cluster.controller_args = ["--ip=*"]

# back in local:.ipython/profile_remotempi/ipcluster_config.py

c.Cluster.engine_launcher_class = "sshproxy"
c.SSHProxyEngineSetLauncher.hostname = "remote"

# general config, specific to the demo
# remote python is not on $PATH by default via ssh
c.SSHLauncher.remote_python = "/opt/conda/bin/python3"
