import settings

SECRET_KEY = 'hardtoguesskey'

DATABASE_USERNAME = 'YourDatabaseuserName'
DATABASE_PASSWORD = 'YourDatabasePassword'
DATABASE_NAME = 'YourDatabaseName'
DATABASE_ADDRESS = 'YourDatabaseAddress(either ip or url address)'
DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s?use_unicode=1&charset=utf8' % (DATABASE_USERNAME,DATABASE_PASSWORD,DATABASE_ADDRESS,DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DATABASE_URI


