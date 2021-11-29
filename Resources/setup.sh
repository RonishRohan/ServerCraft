#cd ..
mkdir -p ./Servers/Versions/$1
wget -O ./Servers/Versions/$1/server.jar https://serverjars.com/api/fetchJar/vanilla/$1 -q -o /dev/null
path=$(realpath ./Servers/Versions/$1)
cd $path
touch eula.txt
echo eula=true >> eula.txt
st sh -c "cd $path && java -jar server.jar nogui"



