"""LOGGING SYSTEM"""

import logging


def log_data(ID, loginTime, logoutTime, timestamp, clearance):
    
    ID = str(ID)
    loginTime = str(loginTime)
    logoutTime = str(logoutTime)
    
    # Change filename to desired path with the log file name.
    if clearance == "clearance 0":
        logging.basicConfig(filename="DataLog.log", level=logging.INFO)
        logging.info("\nUser ID:["+ID+"] \n\t* Accessed the system at: "+loginTime+"\n\t* Logged out of the system at: "+logoutTime)

    else:
        logging.basicConfig(filename="DataLog.log", level=logging.INFO)
        logging.info("\nUser ID:["+ID+"] \n\t* Accessed the system at: "+loginTime+"\n\t* Logged out of the system at: "+logoutTime+"\n\t* Lifted security measures at: {}".format('\n\t                               '.join(map(str, timestamp))))
   
    logging.shutdown()
