# Advanced Control Methods. Seminar 1

This repository is designed to provide students with the necessary resources for the first seminar of the "Advanced Control Methods" course.


## Repo structure

- Source code: [`src/`](./src/)
- Main config that defines the main callbacks: [`main.yaml`](./main.yaml)
- Run the code without scenario: [`run.py`](run.py)
- Run the code with scenario: [`scenario.py`](scenario.py)

## Setup

### Visual Studio Code

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

### Prettify your terminal

- install z shell.
    ```
	sudo apt install zsh
	```
    Read more here: https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH

- install oh-my-zsh.
    ```
	sudo apt install curl
	sudo apt install git
	sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```
    Read more here: https://ohmyz.sh/	

- install pretty theme for oh-my-zsh.
    ```
	git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
	
	nano ~/.zshrc
	```

    And set the theme, write in ~/.zshrc:
    ```
	ZSH_THEME="powerlevel10k/powerlevel10k"
	```
- Reload:
    ```
	exec zsh
	```
    Answer the questions as you desire.

    Read more here: https://github.com/romkatv/powerlevel10k#installation	

- Install auto-suggestions:
    ```
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    ```
- Add the plugin to the list of plugins for Oh My Zsh to load (inside ~/.zshrc):
    ```
    plugins=( 
        # other plugins...
        zsh-autosuggestions
    )
    ```


### pyenv

- Install dependencies
    ```shell
	sudo apt install build-essential libssl-dev zlib1g-dev \
	libbz2-dev libreadline-dev libsqlite3-dev curl \
	libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    ```

- Install pyenv. They "-k" option is to avoid issues with an antivirus.
    ```shell
	curl https://pyenv.run | bash
	```
- Sync pyenv with the terminal.
    ```shell
	echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
	echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
	echo 'eval "$(pyenv init -)"' >> ~/.zshrc
	exec zsh
	```

    Read more here: https://github.com/pyenv/pyenv/wiki#suggested-build-environment

- Install Python 3.11
    ```
	pyenv install 3.11
	```

- Check pyenv versions. Check that Python 3.11 is there.
    ```
	pyenv versions
    ```

### Final steps

- Clone repo
    ```
    git clone https://github.com/OdinManiac/acm-2024-sem-1.git
    ```
- Create virtual env and assosiate with your folder
    ```
    cd acm-2024-sem-1
    pyenv virtualenv 3.11 my-env-name
    pyenv local my-env-name
    pip install -r requirements.txt
    ```