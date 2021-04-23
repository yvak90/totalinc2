# totalinc2
Scripting assignments

**1. Query the covid India API and show statewise active cases**
I have written this using python. I have imported json library and parsed it to get the desired output. I have named this file state_wise_list.py 
https://github.com/yvak90/totalinc2/blob/main/pyscripts/state_wise_list.py

![state_list](https://user-images.githubusercontent.com/58933081/115891019-3b6b1580-a473-11eb-87f1-65f6ad365dff.jpg)



**2. Script to get all AWS EC2 instances in a region and**
I have written this script using python sdk for AWS BOTO3. I have imported boto3 library to get ec2 instances list and parsed it to get the desired output and named this file as ec2_count.py
https://github.com/yvak90/totalinc2/blob/main/pyscripts/ec2_count.py   In Boto3, **ec2.instances.all().platform** returns Windows only for windows machines and in all other cases it returns None. ![running](https://user-images.githubusercontent.com/58933081/115905781-34003800-a484-11eb-86a8-41ffb6eed901.JPG) . Here is the documentation of Boto3 https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.platform
![running2](https://user-images.githubusercontent.com/58933081/115905788-36629200-a484-11eb-8256-ada9e50e0f8b.JPG) . We have 40 AMI's in ap-south-1 and all are either windows or one of Linux/Unix flavour and ![linux](https://user-images.githubusercontent.com/58933081/115906383-14b5da80-a485-11eb-8d0e-26d3cb20db00.JPG)
so i have changed code so that OS type None is replaced as Linux/UNIX. After this change the scripts results like.
![boto3](https://user-images.githubusercontent.com/58933081/115905794-39f61900-a484-11eb-8362-fb84ff06faf2.JPG)

