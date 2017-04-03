echo "trying to CREATE environment "bigdata" (if it already exists, it is ok if fails)"
echo ""
conda env create -f environment.yml
echo "trying to UPDATE environment "bigdata" (if it already exists, it is ok if fails)"
echo ""
conda env update -f environment.yml
echo "trying to activate and update some packages.."
echo ""
source activate bigdata
conda install -yf jupyter matplotlib
sudo pip install geopandas
pip install geopandas pandas
echo ""
echo "I think it should be fine.."
echo ""
jupyter notebook
