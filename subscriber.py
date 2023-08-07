from google.cloud import pubsub_v1

def on_message(message):
    print(f"Received message: {message.data}")

def receive_messages(project_id, subscription_name):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=on_message)
    print(f"Listening for messages on {subscription_path}...\n")

    try:
        streaming_pull_future.result()
    except KeyboardInterrupt:
        streaming_pull_future.cancel()

if __name__ == "__main__":
    project_id = "" #Enter your GCP project id  
    subscription_name = "receive_data-sub" # Your Subscriptions name


    receive_messages(project_id, subscription_name)
