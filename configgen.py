import json 

data = {
  "Version": "14.1.0",
  "Name": "kurumi-eyes",
  "DestinationType": "ImageUploader, FileUploader",
  "RequestMethod": "POST",
  "RequestURL": "https://kurumi-eyes.cyou/api/upload/",
  "Headers": {
    "Authorization": "Token token"
  },
  "Body": "MultipartFormData",
  "FileFormName": "image",
  "URL": "{json:upload_url}",
  "ErrorMessage": "{json:displayMessage}"
}

# export json

with open('user.sxcu', 'w') as f:
    json.dump(data, f, indent=2)
