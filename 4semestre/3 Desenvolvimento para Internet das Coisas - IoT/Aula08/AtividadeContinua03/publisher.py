
import paho.mqtt.client as mqtt
 
TOPICO = "aula/SI/AC3/archeros"

# cria um identificador baseado no id definido
client = mqtt.Client()

# conecta ao broker
client.connect("mqtt.eclipse.org", 1883, 60)

# codificando o payload
#st =  "\n\nArcheros 1900519 - Fernando de Souza Franco \n 1901118 - Lara Angelini Argento \n 1901008 - Leonardo Ferreira \n 1900675 - Lucas Eduardo Ano \n 1900953 - Nicholas Ferreira"   
st = "\n _/﹋\_ \n (҂`_´) \n <,︻╦╤─ ҉ - - \n _/﹋\_\n"
payload = st.encode()
# envia a publicação
client.publish(TOPICO,payload,qos=0)
print (TOPICO + "" + payload.decode())
