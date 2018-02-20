import sys
import os
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "dependancies"))

import pandas as pd
from datetime import datetime, timedelta
from io import BytesIO
from uuid import uuid4


df_options = {}  # for keyword arguments into pd.read_csv
downsample_rate = 3
s3 = boto3.client('s3')
write_bucket = ''
prefix = ''

def downsample(event, context):
    """
    Downsample and if needed transform and serialize the data.
    
    It could be argued that this is already doing too much in the case of AWS lambda by having this function do two
    things as opposed to one.
    
    :param event: 
    :param context: 
    :return: 
    """

    bucket = event['Records'][0]['bucket']['name']
    _key = event['Records'][0]['s3']['object']['key']
    obj = s3.get_object(Bucket=bucket, Key=_key)
    df = pd.read_csv(obj['Body'], **df_options)
    idx = xrange(0, len(df), downsample_rate)
    df = df.iloc[idx, :]
    df = transform(df)
    data = serialize(df)
    s3.put_object(Body=data, Bucket=write_bucket, Key=smart_name(prefix))

def transform(df):
    """
    Any business specific parsing that needs to happen can be easily placed here
    
    :param df: 
    :return: 
    """
    return df

def serialize(df):
    """
    Rules and logic about how to write a processed file. By defult we are just going to be writing this to json
    
    :param df: 
    :return: 
    """
    serialized_json = df.to_json(orient='columns')
    b = BytesIO()
    b.write(serialized_json)
    b.seek(0)
    return b

def smart_name(prefix):
    """
    Combine a prefix where files will be posted and a naming convention.
    
    There is some humor in this name in that smart naming (or smart numbering) is almost never smart and will just cause
    for another conflicting naming convention down the line. 
    
    :param prefix: 
    :return: 
    """
    return '{}/{}-{}.json'.format(prefix, str(datetime.now()), uuid4().hex)