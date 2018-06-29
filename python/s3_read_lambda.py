import csv
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    bucket = 'dev-data'
    key = 'iyers/sfdc/product.csv'
    
    try:
        data = s3.get_object(Bucket=bucket, Key=key)
        csv_data = data['Body'].read()
        s3.download_file(bucket,key,'/tmp/product.csv')
        
        with open('/tmp/product.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                print row[0] ," ",row[1]
        
        return csv_data
    
    
    except Exception as e:
        print(e)
        raise e
