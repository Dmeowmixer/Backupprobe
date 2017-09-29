# AWS Config

The aws config file must exist in the current user's home.
To create this file run:
```
aws configure
```
This file can be added manually to ~/.aws/credentials.
add `aws_access_key_id` and `aws_secret_access_key` to the file:

```
[default]
aws_access_key_id = xxxxxxx
aws_secret_access_key = xxxxxxxx
```

# Run the script

```
SOURCE="filename.sqlite" BUCKET="bucket-name" python runner.py
```
