
import paho.mqtt.client as mqtt
 
TOPICO = "aula/SI/AC3/archeros"

# cria um identificador baseado no id definido
client = mqtt.Client()

# conecta ao broker
client.connect("mqtt.eclipse.org", 1883, 60)

# codificando o payload
st =  "calor dmai"
payload = st.encode()
# envia a publicação
client.publish(TOPICO,payload,qos=0)
print (TOPICO + "" + payload.decode())
