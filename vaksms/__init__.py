import requests
import json
import re

# Thank you for using my library! If there is an error, then write to me, I will fix it

class vaksms:
    """ VakSms API library
    ------------------------------

    ------------------------------

    Example of using this library:
    >>> from vaksms import vaksms
    >>> vakapi = vaksms('your_apikey')
    >>> print(vakapi.getBalance()) # Gives the user's balance on the site

    ------------------------------


    """

    def __init__(self, apikey):

        self.ApiKey = apikey


    def getBalance(self):
        """ Gives the user's balance on the site 

        `Returns`:
            `balance`: int
        """
        
        balance = requests.get(
            f"https://vak-sms.com/api/getBalance/?apiKey={self.ApiKey}"
        ).text

        return json.loads(balance)["balance"]


    def getCountNumber(
            self, 
            service: str, 
            country: str = "ru", 
            operator: str = None, 
            price: bool = False,
            numList: bool = False
    ):
        """Gives the number of available numbers

        -----------------------------------------------------

        `Args`:
            `service` (str): The code of the site, service, social network `*`

            `country` (str): Country code of the phone number. Defaults to "ru".

            `operator` (str): Operator name. Defaults to "None".

            `price` (str): Price per phone number. Defaults to "None".

        `Returns`:
            Returns the number of available numbers

        -----------------------------------------------------

        `Services`: https://vak-sms.com/api/vak/#serviceCodeList1

        `Countres and operators`: https://vak-sms.com/api/vak/#countryOperatorList1
        
        """

        if numList == True: ...

        url = f"https://vak-sms.com/api/getCountNumber/?apiKey={self.ApiKey}&service={service}&country={country}&operator={operator}&price"

        if operator is None:
            url = re.sub(f"&operator={operator}", "", url)
        
        if price is False:
            url = re.sub(f"&price", "", url)

        getCountNumber = requests.get(url).text

        return getCountNumber
    
    
    def getNumber(
            self,
            service: str,
            rent: bool = False,
            country: str = "ru",
            operator: str = None,
            softId: int = None
    ):
        """ Getting a temporary phone number

        -----------------------------------------------------

        `Args`:
            `service` (str): The code of the site, service, social network

            `rent` (bool): If the value rent = true, a rental number is issued, for 8 (eight) hours. Defaults to False.

            `country` (str): Code country of the phone number. Defaults to "ru".

            `operator` (str): Operator name. Defaults to None.

            `softId` (int): The number of the software for receiving deductions from the referral system for developers. Defaults to None.
        `Returns`:
            `returns JSON structured like this`: {"tel": 79991112233, "idNum": "3adb61376b8f4adb90d6e758cf8084fd"}
        
        -----------------------------------------------------

        """

        url = f"https://vak-sms.com/api/getNumber/?apiKey={self.ApiKey}&rent={rent}&service={service}&country={country}&operator={operator}&softId={softId}"

        if rent == False:
            url = re.sub(f"&rent={rent}", "", url)

        if operator is None:
            url = re.sub(f"&operator={operator}", "", url)

        if softId is None:
            url = re.sub(f"&softId={softId}", "", url)

        getNumber = requests.get(url).text

        return getNumber
    
    
    def prolongNumber(
            self,
            service: str,
            tel: str,
    ):
        """ Extension of a previously received number

        -----------------------------------------------------

        `Args`:
            `service` (str): The code of the site, service, social network

            `tel` (str): The phone number to which the code was previously received from the SMS

        `Returns`:
            `returns JSON structured like this`: {"tel": 79991112233, "idNum": "3adb61376b8f4adb90d6e758cf8084fd"}
        
        -----------------------------------------------------

        """
        
        prolongNumber = requests.get(
            f"https://vak-sms.com/api/prolongNumber/?apiKey={self.ApiKey}&service={service}&tel={tel}"
        ).text

        return prolongNumber
    

    def setStatus(
            self,
            idNum: str,
            status: str
    ):
        """ Status change

        -----------------------------------------------------

        `Args`:
            `idNum` (str): Operation ID

            `status` (str): Operation status.


            status = `send` - Another sms

            status = `end` - cancellation of the number

            status = `bad` - the number has already been used, banned

        `Returns`:
            `returns JSON structured like this`: {"status": "ready"}

        -----------------------------------------------------

        """
        
        setStatus = requests.get(
            f"https://vak-sms.com/api/setStatus/?apiKey={self.ApiKey}&status={status}&idNum={idNum}"
        ).text

        return setStatus
    

    def getSmsCode(
            self,
            idNum: str,
            all: bool = None,
    ):
        """ Activation status

        -----------------------------------------------------

        `Args`:
            `idNum` (str): Operation ID

            `all` (bool): The parameter specifies the need to get the entire list of received codes. Defaults to None.

        `Returns`:
            `returns JSON structured like this`:
                `{"smsCode": null}` - the service is waiting for SMS

                `{"smsCode": "CODE"}` - the code has been received, the "CODE" variable contains the activation confirmation code, type = str
        
        -----------------------------------------------------
        
        """
        
        url = f"https://vak-sms.com/api/getSmsCode/?apiKey={self.ApiKey}&idNum={idNum}&all"

        if all is None:
            url = re.sub("&all", "", url)

        getSmsCode = requests.get(url).text

        return getSmsCode
