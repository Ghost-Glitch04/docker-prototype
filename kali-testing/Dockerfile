# Base Image — Kali Linux Rolling
# This is always the first instruction. Everything builds on top of this layer.
FROM kalilinux/kali-rolling:latest

# Install packages in a single RUN to keep it one layer.
# Install curl and wget for downloading files from the internet.
# - apt-get update refreshes the package index first
# - apt-get install -y installs without prompting
# - rm -rf /var/lib/apt/lists/* removes the index cache to keep the layer small
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    zsh \
    vim \
    nano \
#    mousepad \
    ssh \
    && rm -rf /var/lib/apt/lists/*

# Install packagers - Development tools
RUN apt-get update && apt-get install -y \
    python3 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install packages - Network Scanners and Initial Reconnaissance Tools
RUN apt-get update && apt-get install -y \
    nmap \
    ffuf \
    whatweb \
    nuclei \
    && rm -rf /var/lib/apt/lists/*

# Install packages - Vulnerability Scanners
RUN apt-get update && apt-get install -y \
    nikto \
#    openvas \
    && rm -rf /var/lib/apt/lists/*

# Install packages - Enumeration and Exploitation Tools
RUN apt-get update && apt-get install -y \
    enum4linux \
    smbclient \
    hydra \
    && rm -rf /var/lib/apt/lists/*

# Install packages - Web Exploitation Tools
# RUN apt-get update && apt-get install -y \
#     gobuster \
#     sqlmap \
#     burpsuite \
#     && rm -rf /var/lib/apt/lists/*

# Install packages - Binary/Pwn
# RUN apt-get update && apt-get install -y \
#     gdb \
#     radare2 \
#     pip3 install pwntools \
#     ltrace \
#     binwalk \
#     && rm -rf /var/lib/apt/lists/*

# Set Working Directory to /CTF
WORKDIR /CTF

# Start zsh shell when the container starts
CMD ["/bin/zsh"]