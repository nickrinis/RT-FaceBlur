"""LOGGING SYSTEM"""

import logging


def log_data(user_id, login_time, logout_time, timestamp, clearance):
    
    user_id = str(user_id)
    login_time = str(login_time)
    logout_time = str(logout_time)
    
    # Change filename to desired path with the log file name.
    if clearance == "clearance 0":
        logging.basicConfig(filename="DataLog.log", level=logging.INFO)
        logging.info("\nUser ID:["+user_id+"] \n\t* Accessed the system at: "+login_time +
                     "\n\t* Logged out of the system at: "+logout_time)

    else:
        logging.basicConfig(filename="DataLog.log", level=logging.INFO)
        logging.info("\nUser ID:["+user_id+"] \n\t* Accessed the system at: "+login_time +
                     "\n\t* Logged out of the system at: "+logout_time +
                     "\n\t* Lifted security measures at: {}".
                     format('\n\t                               '.join(map(str, timestamp))))
   
    logging.shutdown()
