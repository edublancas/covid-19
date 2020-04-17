import nox
import yaml

# read python version dependency declared in environment.yml
with open('environment.yml') as f:
    env_yml = yaml.load(f, Loader=yaml.SafeLoader)

dep_python = [dep for dep in env_yml['dependencies']
              if dep.startswith('python=3.')]

deps = [dep for dep in env_yml['dependencies']
        if not dep.startswith('python=3.')]

if not len(dep_python):
    raise RuntimeError('environment.yml should declare python=3.x as '
                       'dependency')
if len(dep_python) > 1:
    raise RuntimeError('More than one python=3.x dependency declared')

py_version = dep_python[0].split('=')[1]


@nox.session(venv_backend='conda', python=py_version)
def tests(session):
    # install all conda dependencies from environment.yml
    for dep in deps:
        session.conda_install(dep)

    session.install('-r', 'requirements.txt')

    # run tests
    session.run('python run_notebooks.py')
