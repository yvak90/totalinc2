import boto3
session = boto3.Session(region_name='ap-south-1')
ec2 = session.resource('ec2')
d = dict()
print(" OS 	Type	Count")
print("-----------------------------------")
for i in ec2.instances.all():
    key = "{},{}".format(i.platform,i.instance_type)
    if key in d:
        count = d[key]
        d[key] = count+1
    else:
        d[key] = 1
for x in d.keys():
    ar = x.split(",")
    print("{}   {}    {}".format(ar[0],ar[1],d[x]));
