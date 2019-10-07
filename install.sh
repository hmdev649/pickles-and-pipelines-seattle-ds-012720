# create pipeline-env from the environment.yml file
conda env create -f environment.yml

# add pipeline-env as a kernel in jupyter
python -m ipykernel install --user --name=pipeline-env
