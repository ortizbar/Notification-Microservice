from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/send-notification', methods=['POST'])
def send_notification ():
  data = request.get_json()

#checking for missing data
  if (
    "user" not in data or
    "notification" not in data or
    "message" not in data ):
      return jsonify({'status': "Error", 'message': "Required data not found"}), 400

  user = data["user"]
  notification = data["notification_type"]
  message = data["message"]

#notification types validation
  valid_types = ["error","status","success"]
  
  if notification_type not in valid_types:
    return jsonify({'status': "Error", 'message': "Invalid notification type"}), 400
  return jsonify ({
    'status': "sent",
    'user': user,
    'notification_type': notification_type,
    'message': message,
    'delivery_status': "Notification delivered successfully" }), 200

if __name__ == '__main__':
  app.run(host= "0.0.0.0" , port = 5001)
  


    
