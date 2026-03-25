# Base Image — Kali Linux Rolling
# This is always the first instruction. Everything builds on top of this layer.
FROM kalilinux/kali-rolling:latest

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install base utilities and development tools
# - apt-get update refreshes the package index first
# - apt-get install -y installs without prompting
# - --no-install-recommends skips suggested packages to keep the image small
# - rm -rf /var/lib/apt/lists/* removes the index cache to keep the layer small
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    wget \
    vim \
    nano \
    ssh \
    zsh \
    sudo \
    tmux \
    python3 \
    python3-pip \
    pipx \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install packages - Networking Tools and Diagnostics
RUN apt-get update && apt-get install -y --no-install-recommends \
    net-tools \
    iproute2 \
    iputils-ping \
    dnsutils \
    traceroute \
    tcpdump \
    netcat-openbsd \
    whois \
    openvpn \
    && rm -rf /var/lib/apt/lists/*

#Install packages - Network Scanners, Reconnaissance, Vulnerability Scanning, and Enumeration
RUN apt-get update && apt-get install -y --no-install-recommends \
#    nmap \
#   ffuf \
#    whatweb \
#    nuclei \
#    nikto \
#    enum4linux \
#    smbclient \
#    hydra \
#    && rm -rf /var/lib/apt/lists/*

# Install packages - Web Exploitation Tools
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    gobuster \
#    sqlmap \
#    burpsuite \
#    && rm -rf /var/lib/apt/lists/*

# Install packages - Binary/Pwn
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    gdb \
#    radare2 \
#    ltrace \
#    binwalk \
#    && rm -rf /var/lib/apt/lists/*
#RUN pipx install pwntools

# Mirror the local user and reconstruct into the container
# The following build arguments are expected to be passed during the build process:
ARG USERNAME

# Set default values for USER_UID and USER_GID if not provided
ARG USER_UID=1000

# Set the USER_GID to the same value as USER_UID by default, which is common for a single-user setup
ARG USER_GID=1000

# Create the group first, then create the user belonging to that group
# Add user to the sudo group and allow passwordless sudo
RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd -m -u ${USER_UID} -g ${USER_GID} -s /bin/zsh ${USERNAME} \
    && usermod -aG sudo ${USERNAME} \
    && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER ${USERNAME}

# Set Working Directory to /CTF
WORKDIR /CTF

# Start zsh shell when the container starts
CMD ["/bin/zsh"]