from functools import wraps, update_wrapper
from flask import request, abort, current_app

def validate_account_and_region(f):
    @wraps(f)
    def check_account_and_region_function(*args, **kwargs):
        try:
            account = request.path.split('/')[1]
            if current_app.config['CONFIG']['accounts'][account]:
                pass
            region = request.path.split('/')[2]
            if region in current_app.config['CONFIG']['regions']:
                pass
        except:
            abort(404)
        return f(*args, **kwargs)
    return check_account_and_region_function