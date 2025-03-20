from flask import Flask, render_template, jsonify, request
import boto3
import threading

app = Flask(__name__)

# Initialize Boto3 EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/instances')
def get_instances():
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name'],
                'PublicIpAddress': instance.get('PublicIpAddress', 'N/A')
            })
    return jsonify(instances)

@app.route('/manage_instance', methods=['POST'])
def manage_instance():
    data = request.json
    instance_id = data['instance_id']
    action = data['action']

    def perform_action():
        if action == 'start':
            ec2.start_instances(InstanceIds=[instance_id])
        elif action == 'stop':
            ec2.stop_instances(InstanceIds=[instance_id])
        elif action == 'reboot':
            ec2.reboot_instances(InstanceIds=[instance_id])

    # Use multithreading to handle actions concurrently
    thread = threading.Thread(target=perform_action)
    thread.start()

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)