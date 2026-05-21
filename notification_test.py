import requests
url = "http://localhost:5001/send-notification"

data = {
  'user': "test123",
  'notification_type':"Error",
  'message': "Image generation failed" }

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response JSON:", response.json())
