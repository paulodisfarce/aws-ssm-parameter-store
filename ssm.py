#import logging
import boto3
def get_db_credentials(with_decryption=True):
    ssm = boto3.client('ssm')
    
    db_host = ssm.get_parameter(Name='/lab/db/host', WithDecryption=with_decryption)['Parameter']['Value']
    db_user = ssm.get_parameter(Name='/lab/db/user', WithDecryption=with_decryption)['Parameter']['Value']
    db_password = ssm.get_parameter(Name='/lab/db/password', WithDecryption=with_decryption)['Parameter']['Value']
    db_name = ssm.get_parameter(Name='/lab/db/name', WithDecryption=with_decryption)['Parameter']['Value']
    
    return db_host, db_user, db_password, db_name

db_host , db_user, db_password, db_name = get_db_credentials()

print(db_host)
print(db_user)
print(db_password)
print(db_name)