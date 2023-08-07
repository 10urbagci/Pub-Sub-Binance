import websocket
from google.cloud import pubsub_v1

def on_message(ws, message):
    print()
    print(message)
    publish_message(message)

def on_error(ws, error):
    print(error)

def on_close(close_msg):
    print("### closed ###" + close_msg)

def on_open(ws):
    print("Opened connection")

def streamKline(currency, interval):
    websocket.enableTrace(False)
    socket = f'wss://stream.binance.com:9443/ws/{currency}@kline_{interval}'
    ws = websocket.WebSocketApp(socket,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()

def publish_message(message):
    project_id = "" # Enter your Google Cloud project id  
    topic_name = "receive_data"  # Enter your Pub/Sub topic name

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    publisher.publish(topic_path, message.encode("utf-8"))

streamKline('btcusdt', '1m')