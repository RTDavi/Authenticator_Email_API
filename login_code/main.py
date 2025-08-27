from authenticator_code.controllers import authenticator
from authenticator_code.controllers import send_email
from login_code.controllers.login import app, login_required, login
from login_code.controllers.index import index
from login_code.controllers import db_init

def main():


    app.run(debug=True)
    

main()


