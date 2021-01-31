echo "Warning: Running this script will delete the old environment variables"
echo "Ignore this warning if running the script for the first time"
echo ""
echo "Do you want to proceed? (y/n)"
read flag
if [[ $flag == y ]]
then
    echo "Deleting old envirnoment file"
    rm .env
    echo "Creating new environment file"
    touch .env
    g++-10 -o setup_dep setup_dep.cpp
    ./setup_dep 2> .env
    echo "Deleting dependencies"
    rm ./setup_dep
    echo "Setup succesfull"
else
    echo "Terminating script"
fi
