from fancyhands import FancyhandsClient
from datetime import datetime, timedelta # (We'll need this later)

api_key = 'Xup3jDmeLrpsfJJ'
secret = 'iERWXfUdGNF1v1p'

client = FancyhandsClient(api_key, secret)

#client.standard_create(
#    title="Let me know what's new on the internet!",
#    description="Go to Reddit, and find the title of the top story. Call me at (425) 628-7248 and tell me that title.",
#    bid=2.00,
#    expiration_date=datetime.now() + timedelta(1)
#)

client.custom_create(
    title="Prank call my friend!",
    description="Call (425) 628-7248. Ask if their refrigerator is running. When they say 'yes', tell them 'Well you better go catch it!'.",
    bid=3.00,
    expiration_date=datetime.now() + timedelta(1),
    custom_fields=[
        {
            'label': 'Response',
            'type': 'textarea',
            'description': 'Their response to the prank.',
            'order': 1,
            'required': True
        }
    ]
)

print "Successful run!"