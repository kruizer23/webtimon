---
title: WEBTIMON
section: 1
header: User Manual
footer: webtimon 0.1.0
date: February 6, 2021
---

# NAME

webtimon - Program that checks the availability of a web page.

# SYNOPSIS

**webtimon** [*OPTION*] url title phone

# DESCRIPTION

**webtimon** is a command line program program that checks the availability of a web page
and sends an SMS in case or problems. It builds on the textbelt.com service for SMS
messaging.

# OPTIONS
**-h** 
: display help message

**-k** 
: your textbelt.com API key

**-m** 
: contents of the SMS message to send (max 160 characters)

**-d** 
: enable the output of debug messages


# EXAMPLES
**webtimon**
: Displays usage information and then exits.

**webtimon -k "textbelt" -m "Problem with example.com detected." "https://www.example.com" "Welcome to example.com" "+1555123456"**
: Sends an SMS message to +1 555-123456 if the web page title of https://www.example.com
could not be read of does not equal "Welcome to example.com". The SMS message will read
"Problem with example.com detected." and the "textbelt" API-key will be used.

# EXIT VALUES
**0**
: Success

# AUTHOR

Written by Frank Voorburg.

# REPORTING BUGS

Submit bug reports online at: <https://github.com/kruizer23/webtimon/issues>

# COPYRIGHT
Copyright (c) 2021 Frank Voorburg. License MIT: <https://opensource.org/licenses/MIT>
This is free software: you are free to change and redistribute it. There is NO WARRANTY,
to the extent permitted by law.

# SEE ALSO
Full documentation and sources at: <https://github.com/kruizer23/webtimon>


