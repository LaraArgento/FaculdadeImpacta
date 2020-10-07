#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# Funçao a ser chamada quando chegar um pacote do tipo CONNACK .
def conectou(client, userdata, flags, rc):
    print("Conectado! Código recebido:"+str(rc))
    # Assinando todas as publicações dentro do tópio 
    # /teste/primeiro/10
    client.subscribe("aula/#")

# Função chamada quando uma nova mensagem do tópico é recebida.
def chegou_mensagem(client, userdata, msg):
    dado = str(msg.payload)
    print(msg.topic+" "+dado)

client = mqtt.Client()
client.on_connect = conectou
client.on_message = chegou_mensagem

client.connect ("mqtt.eclipse.org",1883, 60)

# Permanece em loop, recebendo mensagens # e manipulando a conexão.
client.loop_forever()
