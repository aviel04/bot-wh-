''' This module sends a message to a whatsapp group or person '''
import pywhatkit

from datetime import datetime
import time

number = ["+972547727054","+972549371771"]
message = "Spam "*50
seconds = time.time() + 40
date = datetime.fromtimestamp(seconds)


pywhatkit.sendwhatmsg(number,
                        message,
                        date.hour,
                        date.minute,)

