"""
Python program that checks the availability of a web page and sends an SMS in case or problems.
"""
__docformat__ = 'reStructuredText'

import argparse
import logging


# Program return codes.
RESULT_OK = 0


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

    # Temporary test code.
    print("Woohoo!")
    
    # Give the exit code back to the caller.
    return result

