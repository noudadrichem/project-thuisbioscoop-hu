# docker build . -t thuisbioscoop
# docker run thuisbioscoop 
# docker run -e DISPLAY=$DISPLAY thuisbioscoop
pip3 install -r requirements.txt
sudo apt-get install -y python3-tk
python3 app.py