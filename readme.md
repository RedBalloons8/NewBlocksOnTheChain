# NewBlocksOnTheChain

**[Insert some awesome tag here]**

## Cloning

This project uses [git submodules](https://www.git-scm.com/book/en/v2/Git-Tools-Submodules). Make sure to clone it while recursing into them on cloning.

```sh
git clone --recurse-submodules https://github.com/RedBalloons8/NewBlocksOnTheChain
```

## Dependencies

To run the python files on this repository you're going to need a
[libsodium](https://libsodium.gitbook.io/doc/installation/) installation.

Python virtual environments are meant to help you encapsulate your dependencies
such as not to pollute your global installation. If this sounds exciting, run:

```sh
python3 -m venv venv/
```

To activate the virtual environment in the current shell use:

on linux:
```sh
source venv/bin/activate
```

on windows:
```cmd
venv\Scripts\activate.bat
```

Also, we keep dependencies listed in a [requirements](requirements.txt) file.
The python package manager - pip - can be used to read and install them like
this:

```sh
pip install -r requirements.txt
```

## Running

To run the project one has to execute the main script

```sh
python3 main.py
```

## License

This project is licensed under the text in the [license file](license.txt).
