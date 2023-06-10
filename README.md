# NDS-XXX Project Name

## Description

Project description goes here. What is in this repository?

## Value

Why are we even doing this work? Who are we doing this for?

## Initialising python environment
[Reproducible research](https://woodside-digital.atlassian.net/wiki/spaces/DS/pages/405309512/How+do+we+work) is fundamental to Woodside data science way of working. Create [project specific virtual environments](https://woodside-digital.atlassian.net/wiki/spaces/DS/pages/1142128699/Python+virtual+environment+setup) to ensure your python dependencies are tracked. Use the `Makefile` included to automate the project environment.

Set `PYTHON` environment variable to the python executable that you want your project to be based on - `PYTHON` setting defaults to `/opt/python/VERSION/bin/python`. For example, to see available make targets run

```
$ make
```

If you need to set `PYTHON` then run
```
$ PYTHON=/opt/python/3.7/bin/python make
```

The `Makefile` has targets to automate creation, update and clean up of your project specific virtual environment and Jupyter kernel (both take the name of your github repo as default and best practice). Project dependencies are stored in a standard python `requirements.txt` file which you should add and track in Github.

Build or update a new environment with `make build` taget.
Use the new environment as below. Make sure you activate the project environment each time you begin work or use the named Jupyter environment.
```
$ source .venv/bin/activate # can use . instead of source as a shortcut
(project_name) $ which python
/home/wde.woodside.com.au/wXXXX/dev/project_name/.venv/bin/python
```

Install packages as needed using `pip install` but make sure you save your project dependencies by running `make freeze`.
This will save them to requirements.txt which you can save to github.

Deactivate the virtual enviornment with `deactivate`.

## Usage

How does someone pick up your project and recreate your work? Make it **reproducible**

## Secrets

You really don't want to leak your AWS secret key or Postgres username and password on Github. As added motivation the Woodside cyber scanner will flag this and email your manager. [Here's an easy way to proect your secrets](http://drivendata.github.io/cookiecutter-data-science/#keep-secrets-and-configuration-out-of-version-control):

Create a `.env` file in the project root folder. Thanks to the `.gitignore`, this file should never get committed into the version control repository. Here's an example:

```nohighlight
# example .env file
DATABASE_URL=postgres://username:password@localhost:5432/dbname
AWS_ACCESS_KEY=myaccesskey
AWS_SECRET_ACCESS_KEY=mysecretkey
OTHER_VARIABLE=something
```

This will be loaded automatically in the notebooks, and acessible as `os.environ.get("DATABASE_URL")`

## Links

Include links to the relevant Jira Epic, SharePoint, deployed dash app, deployed Uknitee model, etc as pertinent to your project.
