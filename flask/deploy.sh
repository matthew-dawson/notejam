#! /usr/bin/bash
BUCKETNAME="$(date +%Y%j)-cf"
echo $BUCKETNAME
aws s3 mb s3://$BUCKETNAME
aws cloudformation deploy --capabilities CAPABILITY_NAMED_IAM --template-file aws/CFT.yml --stack-name notejam-prod \
  --s3-bucket $BUCKETNAME
ECR_URI=$(aws ecr describe-repositories | grep Uri | awk '{ print $2 }')
docker compose build
docker tag notejam/app:latest $ECR_URI
aws ecr get-login-password --region region | docker login --username AWS \
  --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
docker push $ECR_URI
aws elbv2 describe-load-balancers | grep DNSName | awk '{ print $2 }'