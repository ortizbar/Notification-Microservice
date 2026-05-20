# Notification-Microservice
# Description: 
The Notification Microservice is responsible for sending notifications to users when system events occur It supports notifications like errors, status updates, and successful updates.
# Communication Pipe: 
Rest API with JSON formatted requests/responses.
Method: POST
Format: JSON
Endpoint /send-notification

# Request Data:
Request Parameters
•	user (string)
•	notification_type (string)
•	message (string)

Example call:
response = requests.post(
  "http://localhost:5001/send-notification",
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

SEND POST request to /send-notification

RECEIVE JSON response

If status == “sent”:
    continue processing
Else:
    log notification failure

# UML Sequence:
Client/Test Program    Notification Microservice
        |                        |
        |--- POST /send-notification------->|
        |                        |
        |<--- JSON response-----------------|
        |                        |
