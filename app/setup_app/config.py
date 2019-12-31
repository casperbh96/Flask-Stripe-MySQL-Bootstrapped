MODE='Testing'

if MODE == 'Testing':
    # For MacOS, this fixes an issue where you can't reach other endpoints on localhost
    MYSQL_HOST="host.docker.internal"
    BASE_URL='host.docker.internal'
else:
    MYSQL_HOST="localhost"
    BASE_URL='localhost:5000'

BASE_PORT = ':5000'

MYSQL_PORT='5001'
MYSQL_USER="root"
MYSQL_PASSWORD="rootpw"
MYSQL_DB_NAME="UserDB"

DEBUG=True
TRIAL_LENGTH_DAYS=1
SQLALCHEMY_TRACK_MODIFICATIONS=False
PROTOCOL='http'

SECRET_KEY='super secret string'
STRIPE_PLAN_STARTER='plan_GLXg9InyA37U3l'
STRIPE_PLAN_GROWTH='plan_GLXgiOgfPpscMY'
STRIPE_PLAN_SCALE='plan_GLXgHjFavnxdBA'
STRIPE_PUBLIC_KEY='pk_test_H9P7ybsV5u43G5tmKcBqYqSZ007jr2J6zD'
STRIPE_SECRET_KEY='sk_test_wSMfrRKnGyFpDlH6GMMfaDEo00Jizg9GJh'
WEBHOOK_SUBSCRIPTION_SUCCESS='whsec_26zKj4jFtnrsF6LVgCvJxp4dilM4Bo73'
WEBHOOK_NEW_INVOICE='whsec_VlSaqc1aVmcYK5BQoQat5fEiFxfHzxv9'
WEBHOOK_SUBSCRIPTION_ENDED='whsec_gIXe1MTEkNTp4cZMzIknS6uU1kosNKUy'
FRONTEND_PORT='5000'
NOTIFICATION_PORT='5002'
USER_PORT='5003'
STRIPE_PORT='5004'