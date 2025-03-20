
# Cloud Based Virtualization Management Dashboard

A web-based tool called the Cloud-Based Virtualization Management Dashboard enables users to oversee and manage virtual machines (VMs) in the cloud. It offers real-time status updates and supports standard operations like starting, stopping, and rebooting instances. This project was created to make cloud virtual machine (VM) management easier using Python (Flask) and AWS EC2.
##  Features
- **Instance Management:** Start, stop, and reboot virtual machines with a single click.
- **Real-Time Monitoring:** View the status of all instances, including instance ID, type, state, and public IP address.
- **User-Friendly Interface:** Intuitive web interface for easy interaction.
- **Multithreading: **Handle multiple VM actions concurrently for a smooth user experience.
- **Extensible Architecture:** Designed to support multiple cloud providers (currently supports AWS EC2).
## Deployment

 Steps to set up and run the project  

 **Prerequisites**

- Python 3.8 or higher
- AWS account with EC2 instances
- AWS CLI configured with valid credentials

**Installation**

- Install Dependencies:

```bash
pip install -r requirements.txt
```
- Configure AWS Credentials:

```bash
aws configure
```
- Run the Application:

```bash
python app.py
```
Access the Dashboard:
```
Open your browser and go to http://127.0.0.1:5000.
```



## Usage
- A table listing every EC2 instance, along with its instance ID, type, state, and public IP address, is shown on the dashboard.

- **Control Instances:**

    * To manage your instances, press the Start, Stop, and Reboot buttons.

    * To display the most recent status, the table will automatically refresh.

## Acknowledgements

- **Flask:**  For providing a lightweight and flexible web framework.
- **Boto3:** For enabling seamless integration with AWS services.
- **AWS EC2:** For providing the cloud infrastructure to manage virtual machines.



## Demo
[![Watch the video](https://raw.githubusercontent.com/Nil-tech/Cloud_Based_vm_management/main/cloud_based_vm_management_thumbnail.jpg)](https://raw.githubusercontent.com/Nil-tech/Cloud_Based_vm_management/main/cloud_based_vm_management_demo_video.mp4)



