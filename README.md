# Introduction to Pipelines

This repository introduces the concepts of pipelines using the [`scikit-learn`] library.

## `pipeline-env`

To reproduce the `pipeline-env` conda environment, please run the following bash commands:

```bash
# create pipeline-env from the environment.yml file
conda env create -f environment.yml

# add pipeline-env as a kernel in jupyter
python -m ipykernel install --user --name=pipeline-env
```
