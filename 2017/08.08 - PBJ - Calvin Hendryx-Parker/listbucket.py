import argparse
import boto3

def list_bucket(session, bucket):
    s3 = session.client('s3')
    files = s3.list_objects_v2(Bucket=bucket)
    for file in files['Contents']:
        print(file['Key'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', '-p', action='store', required=True)
    parser.add_argument('--bucket', '-b', action='store', required=True)
    args = parser.parse_args()
    session = boto3.Session(profile_name=args.profile)
    list_bucket(session, args.bucket)
