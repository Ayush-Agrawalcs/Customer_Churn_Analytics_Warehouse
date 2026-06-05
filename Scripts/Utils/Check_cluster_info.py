import boto3

client = boto3.client('redshift')

response = client.describe_clusters(
    ClusterIdentifier='redshift-cluster-1'
)

print("Database:", response['Clusters'][0]['DBName'])
print("User:", response['Clusters'][0]['MasterUsername'])
print("Endpoint:", response['Clusters'][0]['Endpoint']['Address'])