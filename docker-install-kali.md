# Installing Docker on Kali Linux

> **Environment:** Kali Linux Rolling (2026.1), x86_64
> **Method:** Official Kali repository package (`docker.io` v27.5.1)

---

## Methodology — How to Approach This

Before running a single command, the goal is to understand the current state of the system. This applies to any install task, not just Docker. The sequence is:

1. **Reconnaissance first** — check what you have before doing anything. OS, architecture, whether the thing is already installed, what the package manager knows about it.
2. **Understand your constraints** — do you have sudo? What's the network situation? What packages are available?
3. **Choose the simplest path** — there are often multiple ways to install something (package manager, official repo, binary, build from source). For a lab/learning machine, prefer the one that integrates with your existing package manager.
4. **Execute one logical step at a time** — update index, install, start service, configure permissions, verify. Each step has a clear purpose and a clear success condition.
5. **Verify at each stage** — don't assume a step worked. Check it. A command that exits without error doesn't always mean it did what you expected.
6. **Handle errors at the root cause** — read the error message fully. Most errors tell you exactly what went wrong. Look for the actual cause, not just the symptom.
7. **Document actual output** — notes that show real output are more useful than notes that show only expected output. When something behaves unexpectedly, that's the most valuable thing to record.

### Reconnaissance commands for any new system

```bash
# Who am I and what can I do?
whoami
id                        # shows all groups — important for sudo, docker, wireshark, etc.

# What OS and architecture?
cat /etc/os-release
uname -m                  # x86_64, aarch64, etc.

# What's already installed?
which <tool>
<tool> --version

# What does the package manager know?
apt-cache show <package>  # version, dependencies, description
```

---

## Background

Kali Linux ships a maintained `docker.io` package in its official repositories. This is the simplest installation path on Kali and stays in sync with the system package manager (`apt`). The alternative is the upstream Docker CE from `download.docker.com`, which gives the absolute latest version but requires manually adding a third-party repo — not necessary for learning purposes.

### Key concepts before you start

| Term | What it means |
|---|---|
| **Docker Engine** | The daemon (`dockerd`) that manages containers on your machine |
| **Docker CLI** | The `docker` command you type — it talks to the daemon |
| **containerd** | Low-level container runtime Docker Engine sits on top of |
| `docker.io` | The Debian/Kali package name that installs all of the above |

---

## Step 1 — Check Your System

Before installing anything, confirm your OS and architecture. Docker behaves differently on ARM vs x86.

```bash
cat /etc/os-release    # confirm distro and version
uname -m               # should be x86_64 for standard installs
```

**Expected output:**
- `VERSION="2026.1"`, `ID=kali`
- `x86_64`

Also check if Docker is already present:

```bash
which docker
docker --version
```

If those return nothing, proceed with installation.

---

## Step 2 — Update the Package Index

Always refresh `apt`'s package list before installing. This ensures you get the latest available version.

```bash
sudo apt-get update
```

> **Why `apt-get` instead of `apt`?** Both work. `apt-get` is the older, more script-friendly form. `apt` is the newer human-friendly wrapper. For scripting or documentation, `apt-get` is conventional.

---

## Step 3 — Install Docker

```bash
sudo apt-get install -y docker.io
```

The `-y` flag auto-confirms the install prompt. This pulls in:
- `docker.io` — the Docker CLI and Engine
- `containerd` — the container runtime
- Supporting dependencies

---

## Step 4 — Start and Enable the Docker Service

Installing the package does not automatically start the daemon. You need to start it and optionally enable it to start on boot.

```bash
# Start the Docker daemon now
sudo systemctl start docker

# Enable it to start automatically on boot
sudo systemctl enable docker

# Verify it's running
sudo systemctl status docker
```

> **systemctl vocabulary:**
> - `start` — starts the service right now
> - `enable` — sets it to start at boot (doesn't start it now)
> - `status` — shows current running state and recent log lines

---

## Step 5 — Add Your User to the `docker` Group

By default, the Docker socket (`/var/run/docker.sock`) is owned by root. Running `docker` commands without `sudo` requires your user to be in the `docker` group.

```bash
sudo usermod -aG docker $USER
```

> **Important:** This change takes effect on your **next login** (or new shell session). To apply it immediately in the current shell without logging out:
> ```bash
> newgrp docker
> ```

> **Security note:** Members of the `docker` group have effective root-level access to the host system — a container can mount the host filesystem. On a personal/lab machine this is fine. On shared systems, be aware of the implication.

---

## Step 6 — Verify the Installation

```bash
docker --version
docker run hello-world
```

`hello-world` is a minimal test image that Docker pulls from Docker Hub and runs. If it prints a confirmation message, Docker is fully working end-to-end: daemon is up, network is functional, and image pulls work.

**Expected output from `docker run hello-world`:**
```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
...
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

The first two lines are normal — Docker checks locally first, doesn't find the image, then pulls it from Docker Hub. Subsequent runs skip the pull.

---

## Important: Group Membership and Shell Sessions

After running `usermod -aG docker $USER`, the change **does not apply to your current shell session**. You have two options:

**Option A — Open a new terminal** (simplest)
Close and reopen your terminal. The new session picks up the group membership.

**Option B — Apply immediately with `newgrp`**
```bash
newgrp docker
```
This starts a new shell with the `docker` group active. Note: only applies to that shell instance.

**Option C — Run a single command with the group applied (`sg`)**
Useful for scripts or one-off commands in the current session:
```bash
sg docker -c "docker run hello-world"
```

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `permission denied while trying to connect to the Docker daemon socket` | Group membership not yet applied to current session | Open a new terminal, or use `newgrp docker` |
| `Cannot connect to the Docker daemon` | Daemon not running | `sudo systemctl start docker` |
| `docker: command not found` | Package not installed or PATH issue | Re-run install, then `which docker` |

---

## Quick Reference

```bash
# Full install sequence (copy-paste)
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker          # apply group change immediately, or open a new terminal
docker run hello-world # confirm everything works
```

---

## What Actually Happened — Session Notes

This section records what deviated from the ideal path during the first install. These are the most educational parts.

### Issue 1: sudo credentials didn't carry across shell contexts

**What happened:** Running `sudo -v` in the VS Code terminal cached credentials for that terminal session. When commands were run through Claude Code, they executed in a separate subprocess with its own TTY — no shared credential cache, so sudo failed.

**Root cause:** `sudo` caches credentials per-TTY (terminal device), not per-user. Different shells = different TTY = separate cache.

**Fix:** Run sudo-required commands directly in your terminal. For a Docker install this is a one-time issue — once Docker is installed and your user is in the `docker` group, you rarely need sudo for Docker operations.

**Takeaway:** When you see `sudo: a terminal is required to read the password`, the process doesn't have a TTY. You can either: run the command yourself, use `sudo -S` (reads password from stdin — useful in scripts), or configure passwordless sudo for specific commands.

### Issue 2: Group membership didn't apply immediately

**What happened:** After `usermod -aG docker talos`, running `docker run hello-world` gave `permission denied` on the Docker socket.

**Root cause:** Linux group membership is read at login. Adding a user to a group doesn't retroactively update processes already running under that user in the current session.

**Fix:** Open a new terminal (gets a fresh login with updated groups), run `newgrp docker` (spawns a subshell with the new group), or use `sg docker -c "<command>"` to run a single command under the group without a new shell.

**Takeaway:** Any time you modify group membership, assume it won't take effect until a new session. Build this check into your verification step.
