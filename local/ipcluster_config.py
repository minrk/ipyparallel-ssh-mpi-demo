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
# tell the remote cluster to use mpi
# avoids the need to define the remote profile beforehand
c.SSHProxyEngineSetLauncher.ipcluster_args = ["--engines", "mpi"]
c.SSHProxyEngineSetLauncher.environment

# general config, specific to the demo
# conda env is not on $PATH by default via ssh

# make sure conda env is on $PATH
# this approach is safe because the local and remote machines are the same,
# but it should be easier to _extend_ remote $PATH rather than clobbering it
import os

c.SSHLauncher.environment = {"PATH": os.environ["PATH"]}
c.SSHLauncher.remote_python = "/opt/conda/bin/python3"
