## To run the Repository follow-->

#### 1. Download or Pull the repository:
#### 2. Follow Create_S3_boto3.ipynb to create a bucket on AWS.
#### 3. Make Twilio Account, Get your credentials and also get a phone number from Twilio.
#### 4. Make a new folder config and inside it make a file config.json
#### 5. config.json should have the followig contents 

        {
            "thresh": 50,
            "open_threshold_seconds": 60,
            "aws_access_key_id": "Your AWS access Key Id ",
            "aws_secret_access_key": "Your AWS secret Key Id",
            "s3_bucket": "Your AWS Bucket Name",
            "twilio_sid": "Your Twilio sid(Be sure of Test or LIVE credentials",
            "twilio_auth": "Your Twilio auth id",
            "twilio_to": "Mobile number",
            "twilio_from": "Your Twilio alloted mobile number"
        }

#### 6. Run the command python detect.py --conf config/config.json 

Credits to:
Computer Vision God--> https://www.pyimagesearch.com/2019/03/25/building-a-raspberry-pi-security-camera-with-opencv/?submitted_comment=1#comment-687301

https://www.twilio.com/docs/usage/your-request-to-twilio

