"""
Python program that checks the availability of a web page and sends an SMS in case or problems.
"""
__docformat__ = 'reStructuredText'


import argparse
import logging
import requests
from bs4 import BeautifulSoup


# Program return codes.
RESULT_OK = 0
RESULT_ERROR_SMS_TRANSMIT = 1


def main():
    """
    Entry point into the program.
    """
    # Initialize the program exit code.
    result = RESULT_OK

    # Handle command line parameters.
    parser = argparse.ArgumentParser(description="Python program that checks the availability, " +
                                     "of a web page and sends\r\nan SMS in case or problems.\r\n",
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    # Add mandatory command line parameters.
    parser.add_argument('url', type=str, help='URL of the web page to check')
    parser.add_argument('title', type=str, help='expected web page title')
    parser.add_argument('phone', type=str, help='phone number to send the SMS to')

    # Add optional command line parameters.
    parser.add_argument('-d', '--debug', action='store_true', dest='debug_enabled', default=False,
                        help='enable debug messages on the standard output')
    parser.add_argument('-k', action='store', dest='apikey',
                        default='textbelt',
                        help='API key to use (textbelt.com)')
    parser.add_argument('-m', action='store', dest='smsmsg',
                        default='WebTimon detected that your web page is unavailable.',
                        help='text message for the SMS')
    # Perform actual command line parameter parsing.
    args = parser.parse_args()

    # Enable debug logging level if requested.
    if args.debug_enabled:
        logging.basicConfig(level=logging.DEBUG)

    # Set the configuration values that where specified on the command line.
    cfg_url = args.url
    cfg_title = args.title
    cfg_phone = args.phone
    cfg_apikey = args.apikey
    cfg_smsmsg = args.smsmsg

    # Display configuration values for debugging purposes.
    logging.debug('URL: {}'.format(cfg_url))
    logging.debug('Title: {}'.format(cfg_title))
    logging.debug('Phone: {}'.format(cfg_phone))
    logging.debug('API Key: {}'.format(cfg_apikey))
    logging.debug('SMS Message: {}'.format(cfg_smsmsg))

    # Check if the title of the webpage does not match with what is expected.
    if not check_webpage_by_title(cfg_url, cfg_title):
        logging.debug('Title mismatch')
        # This probably means the website is either down or hacked. Inform administrator by SMS.
        if not send_textbelt_sms(cfg_phone, cfg_smsmsg, cfg_apikey):
            logging.debug('SMS Transmit error')
            result = RESULT_ERROR_SMS_TRANSMIT

    # Give the exit code back to the caller.
    return result


def send_textbelt_sms(phone, msg, apikey):
    """
    Sends an SMS through the Textbelt API.

    :param phone: Phone number to set the SMS to.
    :param msg: SMS message. Should not be more than 160 characters.
    :param apikey: Your textbelt API key. 'textbelt' can be used for free for 1 SMS per day.

    :returns: True if the SMS could be sent. False otherwise.
    :rtype: bool
    """
    result = True
    json_success = False

    # Attempt to send the SMS through textbelt's API and a requests instance.
    try:
        resp = requests.post('https://textbelt.com/text', {
            'phone': phone,
            'message': msg,
            'key': apikey,
        })
    except Exception as e:
        result = False
        logging.debug('Textbelt API error: {}'.format(e))

    # Extract boolean API result
    if result:
        try:
            json_success = resp.json()["success"]
        except Exception as e:
            result = False
            logging.debug('JSON parse error: {}'.format(e))

    # Evaluate if the SMS was successfully sent.
    if result:
        if not json_success:
            result = False;

    # Give the result back to the caller.
    return result


def check_webpage_by_title(url, title):
    """
    Extracts the webpage title and compares it to the title specified in the parameter. So the part between the
    <title></title> HTML tags.

    :param url: URL of the webpage to check.
    :param title: Expected webpage title.

    :returns: True if the extracted title matches the one in the parameter, False otherwise.
    :rtype: bool
    """
    result = True

    # Attempt to construct a requests instance, based on the webpage URL.
    try:
        reqs = requests.get(url)
    except Exception as e:
        # Flag error
        result = False
        logging.debug('Connection error: {}'.format(e))

    # Construct BeautifulSoup instance that parses the result of the request.
    if result:
        try:
            soup = BeautifulSoup(reqs.text, 'html.parser')
        except Exception as e:
            # Flag error
            result = False
            logging.debug('HTML parse error: {}'.format(e))

    # Extract the title.
    if result:
        try:
            title_extracted = soup.find("title").get_text()
            logging.debug('Extracted title: {}'.format(title_extracted))
        except Exception as e:
            # Flag error
            result = False
            logging.debug('Title extract error: {}'.format(e))

    # Compare the extracted title with the one specified in the function parameter.
    if result:
        if title_extracted != title:
            # Update the result accordingly.
            result = False

    # Give the result back to the caller.
    return result
