# Remote MPI IPython parallel cluster

demo for [this discourse post][post].

[post]: https://discourse.jupyter.org/t/ipython-cluster-tab-create-a-new-profile/18593

This repo contains a [docker-compose][] file to create two machines, simulating the

[docker-compose]: https://docs.docker.com/compose

There are two 'machines':

- 'remote' where the cluster will run in mpi, and
- 'local' where the notebook server runs

Both machines have similar environments with ipyparallel installed with conda and a user named `demo`

remote:

- runs as an ssh server
- has a user `demo` with password `whocares`
- has packages `ipyparallel, mpi4py, openmpi`
- `demo` has a profile `remotempi` with configuration to start engines with mpi

local:

- runs as a jupyterlab server with password `whocares`
- has packages `ipyparallel, jupyterlab`
- has a user `demo` with profile `remotempi`,
  configured to start the controller on `remote` via `ssh`,
  and engines on `remote` via `sshproxy`

## Build images and start the servers

```
docker-compose up --build
```

This will:

1. build the images
2. launch `sshd` in `remote`, and
3. launch `jupyter lab` on host http://localhost:9999

## Connect

Visit http://localhost:9999 and enter password `whocares`

## Setup passwordless ssh

This setup is just for the demo.
You've probably already done an equivalent in your real deployment.
Once connected, you'll want to setup passwordless ssh between `local` and `remote`

In a terminal, run:

```bash
ssh-keygen -f ~/.ssh/id_ecdsa -t ecdsa -b 521 -q -N ""
ssh-copy-id -i ~/.ssh/id_ecdsa remote
```

You will be prompted to enter the password for `demo@remote`.
It is `whocares`:

<details>
    <summary>sample output of ssh-keygen & ssh-copy-id</summary>

```
demo@local:~$ ssh-keygen -f ~/.ssh/id_ecdsa -t ecdsa -b 521 -q -N ""
demo@local:~$ ssh-copy-id -i ~/.ssh/id_ecdsa remote
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/demo/.ssh/id_ecdsa.pub"
The authenticity of host 'remote (172.19.0.2)' can't be established.
ED25519 key fingerprint is SHA256:TK6TemW6RKn0vVY+27kStMRvQnhFOT606mn/aP7Mp6o.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
demo@remote's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'remote'"
and check to make sure that only the key(s) you wanted were added.
```

</details>

## Start and connect to the cluster

```python
import ipyparallel as ipp

cluster = ipp.Cluster(profile="remotempi")
rc = cluster.start_and_connect_sync()
```

or if you've launched the cluster via UI, skip the `start` part:

```python
cluster = ipp.Cluster.from_file(profile="remotempi")
rc = cluster.connect_client_sync()
```
