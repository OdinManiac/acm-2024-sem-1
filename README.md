# Advanced Control Methods. Seminar 1

This repository is designed to provide students with the necessary resources for the first seminar of the "Advanced Control Methods" course.


## Contents

- Source code: [`src/`](./src/)
- Main config that defines the main callbacks: [`main.yaml`](./main.yaml)
- Run the code without scenario: [`run.py`](run.py)
- Run the code with scenario: [`scenario.py`](scenario.py)


## Getting Started

To get started with the materials in this repository, clone the repository to your local machine using the following command:

```
git clone https://github.com/OdinManiac/acm-2024-sem-1.git
```

Then install requirements:

```
pip install -r requirements.txt
```


## Setup

## Visual Studio Code

[Install vscode](https://code.visualstudio.com/download)

### WSL 

Here are the steps to install WSL 2 first. This is the Linux subsystem for Windows.

- First, check the available Linux distributions to install:

    ```shell	
    wsl --list --online
    ```
    The output may be, say:

    ```
    The following is a list of valid distributions that can be installed.
    Install using 'wsl --install -d <Distro>'.

    NAME                                   FRIENDLY NAME
    Ubuntu                                 Ubuntu
    Debian                                 Debian GNU/Linux
    kali-linux                             Kali Linux Rolling
    Ubuntu-18.04                           Ubuntu 18.04 LTS
    Ubuntu-20.04                           Ubuntu 20.04 LTS
    Ubuntu-22.04                           Ubuntu 22.04 LTS
    OracleLinux_8_5                        Oracle Linux 8.5
    OracleLinux_7_9                        Oracle Linux 7.9
    SUSE-Linux-Enterprise-Server-15-SP4    SUSE Linux Enterprise Server 15 SP4
    openSUSE-Leap-15.4                     openSUSE Leap 15.4
    openSUSE-Tumbleweed                    openSUSE Tumbleweed
    ```

- Pick one, say, Ubuntu and install it:
    ```shell
    wsl --install -d Ubuntu
    ```
    Read more here: https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview

- Run Linux terminal from WSL (Windows Run, type "WSL" or "Ubuntu"). Update and upgrade.
    ```shell
	sudo apt update
	sudo apt upgrade
    ```