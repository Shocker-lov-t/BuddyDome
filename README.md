# buddydome
Highly Available Django Application deployed using AWS Elastic Beanstalk, EC2, RDS, S3 Bucket and Route53

Step-1: Create an AWS database instance of postgreSql database  ( Compulsory in both )
        
        -Login to AWS console and head toward for RDS Service
        -Launch an Postgresql Database instance and note down the username,master username and password of the instance ( it will be shown one time only so make sure to note them down very carefully)
        -Wait for the database instance to be in running state ( Takes approximately 10 min)
        -After Launched, click on the instance and it will show the details of your database
        -Open Django project's Settings.py file, there you will see a section "DATABASE" IN LINE 85 
              >>> Change name to the username to saved earlier
              >>> Change Username to master username
              >>> Change Password to new Password
              >>> Change Host to new host which is shown exactly on aws console database instance page
        -SAVE CHANGES

Step-2: (Follow only if you are working with BuddyDome with s3 only otherwise ignore this step) Setting up S3 bucket 

  >>Create an s3 bucket ( with unchecking the box of " Block all public access" ) <br>
  >>Change the bucket policy as follows <br>
   //S3 Policy//

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::s3-bucket/*"
            }
        ]
    } 
    
   >>Create an IAM user
          
            >>>In AWS Look for IAM service 
            >>>Create an IAM user with S3 Policy
            >>>Generate Access key and secret key and note them down

   >>Go to your Django project and first install two libraries using following command 
             
             pip install boto3 django-storages
              
   >>Add Following in settings.py file
        
              import boto3
              from storages.backends.s3boto3 import S3Boto3Storage


              INSTALLED_APPS = [ 
                      'storages'
                      ]

              //Write Corresponding Values//
              AWS_ACCESS_KEY_ID =
              AWS_SECRET_ACCESS_KEY = 
              AWS_STORAGE_BUCKET_NAME = 
              AWS_S3_REGION_NAME='ap-south-1'

              AWS_QUERYSTRING_AUTH = False


              # Set the static files storage backend to S3
              STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

              # Set the URL for static files
              STATIC_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/"

              AWS_LOCATION = 'media'

              DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

              # Set the URL for media files
              MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{AWS_LOCATION}/"

              STATIC_ROOT = "https://s3.amazonaws.com/my-static-bucket/"
              MEDIA_ROOT = "https://s3.amazonaws.com/my-media-bucket/"
         
   >>Some Changes in all urls.py file <br>
    //urls.py//

              from Buddy import settings
              from django.conf.urls.static import static
              
   //In URL_patterns ending Square bracket Add below code as it is//
  
               +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



Step-3: Setting up Load Balanacing ( Compulsory in Both)

>  > Install Elastic Beansrtalk CLI using following:-

         pip install awsebcli

>  > Create a Config file to speicify settings file and .conf file to specify upload limit for your elasticbeasntalk environment in following format

        ~/BuddyDome/
        |-- .ebextensions
        |   `-- django.config
        |-- .platform
        |   --nginx
        |        --conf.d
        |                `--proxy.conf

>  > Write the following in django.config file

        container_commands:
          01_collectstatic:
            command: "source $PYTHONPATH/activate && python manage.py collectstatic --noinput"
        option_settings:
          aws:elasticbeanstalk:container:python:
            WSGIPath: Buddy.wsgi:application
          aws:elasticbeanstalk:environment:proxy:staticfiles:
            static: "static"

>  > Write the Following in proxy.conf

        client_max_body_size 400M;        

>  > In terminal initialize the application for elasticbeanstalk using awsebcli
>  > Make sure you are in main directory where you can access manage.py file ( Use dir or ls command to verify)

        eb init -i

        Select a default region 
        (Default is 3): 6  

        application name: Buddydome

        Enter Application Name
        (default is "BuddyDome "): BuddyDome

        Select a platform
        (make a selection): 9       //Python

        Select a platform branch. 3

>  >  In Terminal Create Elastic beanstalk environment:- 

        eb create Buddydome-env
        
>  > use the following to get the status and to open the deployed application:-

        eb status
        eb open
>  > Use the following only in case you make some changes after environment creation

        ed deploy

