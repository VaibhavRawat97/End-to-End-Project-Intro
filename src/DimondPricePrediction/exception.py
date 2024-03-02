# Lets start with our own custom exception
# Inside we'll pass a few parameters like error_message,error_details
# Now we'll initialize a variable error_message, then we'll find out some details regarding the errors.
# We want to know the script name i.e, in which script we're facing the error, in which file
# in which module we're getting the error. 



class customexception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        
        
    

if __name__ == "__main__":
    try:
        
        a=1/0
    
    except Exception as e:
        raise customexception(e,sys)