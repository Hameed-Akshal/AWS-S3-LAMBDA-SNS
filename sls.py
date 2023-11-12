import boto3
mysns = boto3.client("sns")

def lw(x, y):

  mysns.publish(
    TopicArn='arn of sns', # arn of sns
    Message='something is uploaded',
    Subject='I got new doc in s3 bucket',
  
  )
  print("Hey i am Hameed Akshal from s3 bucket..... NOw I am going tO Call sns....")
