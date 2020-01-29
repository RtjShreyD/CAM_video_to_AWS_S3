# import the necessary packages
from twilio.rest import Client
import boto3
from threading import Thread
 
class TwilioNotifier:
	def __init__(self, conf):
		# store the configuration object
		self.conf = conf
 
	def send(self, msg, tempVideo):
		# start a thread to upload the file and send it
		t = Thread(target=self._send, args=(msg, tempVideo,))
		t.start()

	def _send(self, msg, tempVideo):
		# create a s3 client object
		s3 = boto3.client("s3",
			aws_access_key_id=self.conf["aws_access_key_id"],
			aws_secret_access_key=self.conf["aws_secret_access_key"],
		)
 
		# get the filename and upload the video in public read mode
		filename = tempVideo.path[tempVideo.path.rfind("/") + 1:]
		s3.upload_file(tempVideo.path, self.conf["s3_bucket"],
			filename, ExtraArgs={"ACL": "public-read",
			"ContentType": "video/mp4"})    

