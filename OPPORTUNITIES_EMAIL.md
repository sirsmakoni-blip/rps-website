# Opportunity enquiry email on Render

Set these environment variables for the existing Django service before accepting live enquiries:

| Variable | Value to supply |
| --- | --- |
| `EMAIL_HOST` | SMTP server hostname from the mail provider |
| `EMAIL_PORT` | SMTP port, usually `587` when using TLS |
| `EMAIL_HOST_USER` | SMTP account username |
| `EMAIL_HOST_PASSWORD` | SMTP account password or app password |
| `EMAIL_USE_TLS` | `True` for STARTTLS, or `False` if the provider requires another setup |
| `DEFAULT_FROM_EMAIL` | A sender address the SMTP provider authorises |

The default backend is Django SMTP. `EMAIL_BACKEND` can be overridden for local testing. No SMTP credentials are committed. Both opportunity forms deliver to `projects@rpsswitchgearsa.co.za`; the visitor's company email is set as the reply-to address. Failed deliveries are logged on the server and shown to visitors as a generic retry message.
