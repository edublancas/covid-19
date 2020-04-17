set -e

NAME=kaggle

# this will create a conda env called "package_name", will replace an existing one if any
echo "Creating conda environment '$NAME'..."
conda env create --file environment.yml --force --name $NAME

# we need to initialize conda, see: https://github.com/conda/conda/issues/7980
eval "$(conda shell.bash hook)"

echo "Activating $NAME environment: conda activate $NAME"
conda activate $NAME

echo "$(type python)"
echo "$(type pip)"


echo 'Installing requirements.txt'
pip install -r requirements.txt

echo "Remember to activate your environment using 'conda activate $NAME'"
