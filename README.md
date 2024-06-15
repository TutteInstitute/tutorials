# Tutorials

**True README in construction**

## Table of Contents
[List of Tutorials](#Order)
[Requirements](#Requirements)  
[Installation](#Getting-started)  

A collection of tutorials on methodologies involving the tools of the Institute

## Requirements

| | |
|------------:|:----|
| **Minimum** | Python version 3.10. Later version, or version 3.9, _might_ work. Earlier versions, we don't want to know. |
| **Best**    | A working Conda install. |

## Getting started

Before you can run through and play with the tutorial notebooks, you must put together their computing environment.
Please open an [issue](https://github.com/TutteInstitute/tutorials/issues/new/choose) if you encounter any issue that is not documented below, or if you get stuck during setup.

### Build and activate the environment

In a terminal window, type

```sh
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

On Windows, the sequence is almost the same, but the environment is activated slightly differently:

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Alternatively, if you have Conda, you can benefit from a better assurance of a clean virtual environment with a suitable version of Python:

```sh
conda create -p venv "python=3.10" "pip"
conda activate ./venv
pip install -r requirements.txt
```

### Customize the environment according to incumbent Jupyter Lab

<a id="own-jupyter-lab"></a>
If you do not already have a Jupyter Lab instance running, then you can start it now, from the tutorial venv you just built.

```sh
jupyter lab
```

If you are running it on the same computer as your desktop,
then this will open up a web browser window automatically.
Otherwise, arrange port forwarding, and browse to the `http://localhost:8xxx/lab?token=...` URL printed by Jupyter Lab.

However...

#### If you are working out of an existing Jupyter Lab instance or JupyterHub mini-server

You have to ensure that your running instance of Jupyter Lab matches versions with this environment for the three following packages:

1. `bokeh`
2. `panel`
3. `pyviz-comms`

For that, locate the Conda environment or venv your Jupyter Lab instance (or instance of `jupyter-labhub`, or `jupyterhub-singleuser`) runs from.
If it runs from an environment at path `/conda/env`, then run

```sh
conda list -p /conda/env
```

If it runs off of a regular Python venv at path `/regular/venv`, try instead

```sh
pip list --path /regular/venv/lib/python3.10/site-packages
```

(The version number on the right of `python` can be different.)
This latter form will also work if your Jupyter Lab runs from some cursed systemwide or user account deployment, such as

```sh
pip list --path /usr/lib/python3.10/site-packages
pip list --path $HOME/.local/lib/python3.9/site-packages
```

In the list you get from any of these commands, look for the names of the packages above.
The version deployed in this environment is displayed on the right of the name.
You can get creative:

| Platform | Command |
|---------------|---------|
| Linux / macOS | `conda list -p /opt/conda/envs/jupyterhub \| grep bokeh` |
| Windows       | `conda list -p "C:\Users\johndoe\miniconda3\envs\jupyter" \| findstr bokeh` |

After a reasonable effort, you will either find the version of each package as it was deployed in that foreign Jupyter environment, or not.
On the one hand, if version information can be found for any of the three packages above,
then force the installation of the same version of that package in your own environment.
For instance, if you've discovered that the Jupyterhub environment has Bokeh version 3.0.1, then run

```sh
pip install --upgrade --ignore-installed --no-deps "bokeh==3.0.1"
```

You can further run `pip list` or `conda list` in your own Conda environment or venv to double-check that versions match.

On the other hand, for one of these packages, you might not have found any version information.
This is likely because the package is not yet deployed in the Jupyter Lab or JupyterHub environment.
As the case may be, you may have the privileges to add packages to that environment.
If this is so, use `pip list` once again to look up the version of that package that got installed in your own environment,
and use `pip install <package>==<same version>` to deploy it in the foreign environment wherefrom Jupyter Lab runs.
However, if you don't have that privilege, then it will not be possible for you to run these tutorials in that Jupyter Lab or JupyterHub instance.
If you can access the computer differently (say, through SSH),
or if you can just simply start another Jupyter Lab instance on the box,
then you can run Jupyter Lab from the tutorial venv you built, as shown [above](#own-jupyter-lab).
Otherwise, you will have to restart the setup on a computer you can access and configure suitably.

### Naming the kernel

In your Jupyter Lab instance, open a terminal, and activate your venv.

| Tool / Platform              | Activating the venv...   |
|------------------------------|--------------------------|
| Conda / Any                  | `conda activate ./venv`  |
| Pure Python / Linux or macOS | `. venv/bin/activate`    |
| Pure Python / Windows        | `venv\Scripts\activate`  |

Then punch in the following command:

```sh
python -m ipykernel install --user --name tutte-tutorials --display-name "Tutte Institute Tutorials"
```

If you open another launcher and wait a few seconds,
you should see a new blue-and-yellow icon show up under **Notebooks**,
with the label *Tutte Institute Tutorials*.
You can now close the terminal.

From here, we are ready to [start](1-recipes-bag-of-words.ipynb)!

## Order
The existing tutorials, in a suggested order of reading, are:
1. [Introduction to Data Visualization](1-recipes-bag-of-words.ipynb)
2. [Topic Modelling](2-topic-modelling-pokemon.ipynb)
