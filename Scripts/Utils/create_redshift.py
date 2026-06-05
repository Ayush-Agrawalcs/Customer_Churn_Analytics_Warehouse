# import boto3
# import postgrey2
# redshift = boto3.client('redshift',region_name='ap-south-1')

# response = redshift.create_cluster(
#     ClusterIdentifier='telecom-cluster',
#     DBName='telecom_dw',
#     MasterUsername='telecom_database',
#     MasterUserPassword='Ayush1234@',
#     NodeType='dc2.large',
#     ClusterType='single-node',
#     IamRoles=[
#         'arn:aws:iam::103869374478:role/service-role/AmazonRedshift-CommandsAccessRole-20260601T230844'
#     ],
#     PubliclyAccessible=True
# )

# print("Cluster creation started")

import boto3

client = boto3.client(
    "redshift",
    region_name="ap-south-1"
)

print(client.describe_clusters())