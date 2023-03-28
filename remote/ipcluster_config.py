# remote:.ipython/profile_remotempi/ipcluster_config.py
c = get_config()  # noqa

# launch engines with mpiexec
c.Cluster.engine_launcher_class = "mpi"

# PATH hack
import os
import sys
# make sure sys.prefix is on $PATH before we start launching subprocesses
env_path = os.environ["PATH"].split(os.pathsep)
sys_bin = os.path.join(sys.prefix, "bin")
if sys_bin not in env_path:
    os.environ["PATH"] = sys_bin + os.pathsep + os.environ["PATH"]
