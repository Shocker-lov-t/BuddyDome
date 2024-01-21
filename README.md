# buddydome
<div align="center">
        <img width="306" alt="newlogo" src="https://github.com/Shocker-lov-t/buddydome/assets/98687345/ff41be25-ff70-4880-adf7-7a0c9df5f33d">
        


</div>

Highly Available Django Application implemented using Blue/Green deployment on AWS Elastic Beanstalk resulting in a seamless 
deployment process and enabling cloud enthusiasts to share and access learning resources.<br>
<br>Technology: AWS, Django, HTML/CSS, JavaScript, PostgreSQL<br>
<br> Major AWS Services used :- <ul type="square">
<li>RDS</li>
<li>S3</li>
<li>ELASTICBEANSTALK</li>
<li>ROUTE53</li>

</ul>

# Step-1: Create an AWS database instance of postgreSql database  ( Compulsory in both )
        
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

# Step-2: (Follow only if you are working with BuddyDome with s3 only otherwise ignore this step) Setting up S3 bucket

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



# Step-3: Deployment Using AWS Elastic Beanstalk( Compulsory in Both)

>  > Install Elastic Beanstalk CLI using following:-

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

>  > In terminal initialize the application for elasticbeanstalk using awsebcli <br>
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

        eb deploy

# Step-4 : Setting Up DNS (Route53 and Hostinger)
<OL>
<li>Go to Route53 and create a "Hosted Zone" with corresponding Hostinger domain name ( e.g. buddydome.cloud) </li>
<li>Change Hostinger Nameservers to Route53 Generated Nameservers (changes might take upto 24hr)</li>
<li>In Hosted Zone, create a "A" type Record <br>
        <ul>
<li>Leave Subdomain as blank</li>
<li>Toggle "Alias"</li>
<li>In Endpoint, choose Alias to "Elastic Beanstalk environment"</li>
<li>CHoose Corresponding Region, ap-south-1 "Asia Pacific (Mumbai)" </li>   
<li>Choose Environment, select the corresponding elasticbeanstalk environment that directs to Buddydome Project</li>
<br>
Click "Add another record" <br>
       <li> > > Write "www" in subdomain</li>
       <li> > > Choose Type as "CNAME"</li>
       <li> > > In Value write original domain i.e. buddydome.cloud</li>
<br>
<li> Click "Create Records" </li>
        </ul>
</li>
</OL>
<br>
<br>
<i>With this your application has been successfully deployed and hosted with a Domain</i>
