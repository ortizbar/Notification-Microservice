# Notification-Microservice
# Description: The Notification Microservice is responsible for sending notifications to users when system events occur It supports notifications like errors, status updates, and successful updates.
# Communication Pipe: Rest API with JSON formatted requests/responses.

# Request Data:
POST /send-notification

Example call:
response = requests.post(
  "http://localhost:5000/send-notification",
  json={
   "user": "user123",
   "notification_type": "error",
   "message": "Image generation failed"
  }
)
print(response.json())

# Receive Data:
Microservice returns JSON responses containing delivery status.

Example call:
