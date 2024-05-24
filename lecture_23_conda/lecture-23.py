"""...................................................             Conda       ..........................................."""

# As soon as the anaconda installed in our system, firstly it inject itself in the powershell and
# By default ek base virtualenv activate ho jata hai unlike python virtualenv (.venv) in lecture_22 (which we have to activate manually using command)
# In conda, we can create different virtual environment and install modules and directly be used in vs code


"""         Rule : Do not use 'pip' and 'conda' simultaneously      """


"""     To show environment list        """
# PS D:\Chai Aur Code\Chai-Aur-Python> conda env list
# # conda environments:
# #
# base                     E:\Anaconda


"""         To create a new environment named : newpy     """
# PS D:\Chai Aur Code\Chai-Aur-Python> '''conda create --name newpy python=3.10'''
# Collecting package metadata (current_repodata.json): done
# Solving environment: done


# ==> WARNING: A newer version of conda exists. <==
#   current version: 23.7.4
#   latest version: 24.1.2

# Please update conda by running

#     $ conda update -n base -c defaults conda

# Or to minimize the number of packages updated during conda update use

#      conda install conda=24.1.2


# ## Package Plan ##

#   environment location: E:\Anaconda\envs\newpy

#   added / updated specs:
#     - python=3.10


# The following packages will be downloaded:

#     package                    |            build
#     ---------------------------|-----------------
#     bzip2-1.0.8                |       hcfcfb64_5         122 KB  conda-forge
#     ca-certificates-2024.2.2   |       h56e8100_0         152 KB  conda-forge
#     libffi-3.4.2               |       h8ffe710_5          41 KB  conda-forge
#     libsqlite-3.45.1           |       hcfcfb64_0         850 KB  conda-forge
#     libzlib-1.2.13             |       hcfcfb64_5          54 KB  conda-forge
#     openssl-3.2.1              |       hcfcfb64_0         7.8 MB  conda-forge
#     pip-24.0                   |     pyhd8ed1ab_0         1.3 MB  conda-forge
#     python-3.10.13             |h4de0772_1_cpython        15.2 MB  conda-forge
#     setuptools-69.1.1          |     pyhd8ed1ab_0         459 KB  conda-forge
#     tk-8.6.13                  |       h5226925_1         3.3 MB  conda-forge
#     tzdata-2024a               |       h0c530f3_0         117 KB  conda-forge
#     ucrt-10.0.22621.0          |       h57928b3_0         1.2 MB  conda-forge
#     vc-14.3                    |      hcf57466_18          17 KB  conda-forge
#     vc14_runtime-14.38.33130   |      h82b7239_18         732 KB  conda-forge
#     vs2015_runtime-14.38.33130 |      hcb4865c_18          17 KB  conda-forge
#     wheel-0.42.0               |     pyhd8ed1ab_0          56 KB  conda-forge
#     xz-5.2.6                   |       h8d14728_0         213 KB  conda-forge
# -64::vc-14.3-hcf57466_18
#   vc14_runtime       conda-forge/win-64::vc14_runtime-14.38.33130-h82b7239_18
#   vs2015_runtime     conda-forge/win-64::vs2015_runtime-14.38.33130-hcb4865c_18
#   wheel              conda-forge/noarch::wheel-0.42.0-pyhd8ed1ab_0
#   xz                 conda-forge/win-64::xz-5.2.6-h8d14728_0


# Proceed ([y]/n)? y


# Downloading and Extracting Packages

# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done
# #
# # To activate this environment, use
# #
# #     $ conda activate newpy
# #
# # To deactivate an active environment, use
# #
# #     $ conda deactivate
"""        END      """


"""     To show environment list        """
# PS D:\Chai Aur Code\Chai-Aur-Python> conda env list
# # conda environments:
# #
# base                     E:\Anaconda
# newpy                    E:\Anaconda\envs\newpy


""" To Deactivate Conda """
# PS D:\Chai Aur Code\Chai-Aur-Python> conda deactivate
# PS D:\Chai Aur Code\Chai-Aur-Python>


"""        Installing module seaborn        """

# PS D:\Chai Aur Code\Chai-Aur-Python> conda install seaborn
# Collecting package metadata (current_repodata.json): done
# Solving environment: done


# ==> WARNING: A newer version of conda exists. <==
#   current version: 23.7.4
#   latest version: 24.1.2

# Please update conda by running

#     $ conda update -n base -c defaults conda

# Or to minimize the number of packages updated during conda update use

#      conda install conda=24.1.2


# ## Package Plan ##

#   environment location: E:\Anaconda

#   added / updated specs:
#     - seaborn


# The following packages will be downloaded:

#     package                    |            build
#     ---------------------------|-----------------
#     certifi-2024.2.2           |     pyhd8ed1ab_0         157 KB  conda-forge
#     seaborn-0.13.2             |       hd8ed1ab_0           7 KB  conda-forge
#     seaborn-base-0.13.2        |     pyhd8ed1ab_0         229 KB  conda-forge
#     ------------------------------------------------------------
#                                            Total:         392 KB

# The following NEW packages will be INSTALLED:

#   seaborn-base       conda-forge/noarch::seaborn-base-0.13.2-pyhd8ed1ab_0

# The following packages will be UPDATED:

#   ca-certificates    pkgs/main::ca-certificates-2023.12.12~ --> conda-forge::ca-certificates-2024.2.2-h56e8100_0
#   seaborn            pkgs/main/win-64::seaborn-0.12.2-py31~ --> conda-forge/noarch::seaborn-0.13.2-hd8ed1ab_0

# The following packages will be SUPERSEDED by a higher-priority channel:

#   certifi            pkgs/main/win-64::certifi-2024.2.2-py~ --> conda-forge/noarch::certifi-2024.2.2-pyhd8ed1ab_0


# Proceed ([y]/n)?  y


# Downloading and Extracting Packages

# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done
"""       END       """


# PS D:\Chai Aur Code\Chai-Aur-Python> python
# Python 3.11.5 | packaged by Anaconda, Inc. | (main, Sep 11 2023, 13:26:23) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import numpy as np
# >>> exit()


"""     To stop conda from auto activation during the start of the terminal     """
# conda config --set auto_activate_base false


""""    To Use jupyter Notebook within vs code    :  .ipynb     """
# 1. jupyter notebook is in the format 'ipynb'     (I python notebook)

# 2. To select a kernel (conda env)
