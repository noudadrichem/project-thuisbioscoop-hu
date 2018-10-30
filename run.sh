docker build . -t thuisbioscoop
docker run thuisbioscoop 
docker run -e DISPLAY=$DISPLAY thuisbioscoop