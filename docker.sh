sudo docker run -it -p 1883:1883 -p 9001:9001 -v ./conf/:/mosquitto/config/ -v /mosquitto/data -v /mosquitto/log eclipse-mosquitto


##mosquitto.conf

# listener 1883
# persistence true
# allow_anonymous true