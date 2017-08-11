#!/usr/bin/env python

import argparse
import boto3
from clint.textui import colored, columns, puts, prompt

def list_bucket(session, bucket):
    s3 = session.client('s3')
    if not bucket:
        buckets = s3.list_buckets()
        options = [b['Name'] for b in buckets['Buckets']]
        bucket = prompt.options('Please pick a bucket', options)

    files = s3.list_objects_v2(Bucket=options[bucket-1])
    for file in files['Contents']:
        puts(
            columns(
                [colored.green(file['Key']), 60],
                [colored.red(str(file['Size'])), 25],
            )
        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', '-p', action='store', required=True)
    parser.add_argument('--bucket', '-b', action='store', default=None)
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()
    session = boto3.Session(profile_name=args.profile)
    list_bucket(session, args.bucket)
