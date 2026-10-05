# Opportunity enquiry email on Render

Set these environment variables for the existing Render web service `rps-website` before accepting live enquiries. The non-secret values below are also the Django defaults; the mailbox password must come from the environment.

| Variable | Value to supply |
| --- | --- |
| `EMAIL_HOST` | `smtp.mweb.co.za` |
| `EMAIL_PORT` | `587` |
| `EMAIL_HOST_USER` | `projects@rpsswitchgearsa.co.za` |
| `EMAIL_HOST_PASSWORD` | Actual Projects mailbox password, entered privately in Render |
| `EMAIL_USE_TLS` | `True` (STARTTLS) |
| `DEFAULT_FROM_EMAIL` | `RPS Switchgear SA Projects <projects@rpsswitchgearsa.co.za>` |

The default backend is Django SMTP. `EMAIL_BACKEND` can be overridden for local testing. No SMTP credentials are committed. This project reads process environment variables with `os.environ`; it does not automatically load a `.env` file. Do not commit a `.env` containing credentials. No `.env.example` currently exists.

Both opportunity forms deliver to `projects@rpsswitchgearsa.co.za`; the visitor's Company Email is set as `Reply-To`:

- EPC subject: `EPC for PV Solar Solutions – Project Enquiry`
- Capital Partners subject: `RPS Project Capital Partners – Project Enquiry`

Failed deliveries retain the existing server logging and generic visitor retry message. Form fields, validation, CSRF, honeypot and success behaviour remain unchanged.

## Render environment and connectivity

Audit on 2026-10-05: `rps-website` uses the Starter paid instance plan. Initially its Environment page contained only `DEBUG` and `SECRET_KEY`, with no linked environment groups or secret files. After the successful connectivity test, the five non-secret email variables above were saved using **Save only**. No deployment was triggered. `EMAIL_HOST_PASSWORD` exists: **NO**. The owner must enter the mailbox password privately, then apply the environment changes with a deployment. Source changes in this workspace have not been deployed.

A TCP-only socket check executed inside the deployed service connected successfully to `smtp.mweb.co.za:587` with a five-second timeout. Production TCP connectivity is ready for the mailbox credentials. No SMTP authentication or email send was attempted; mailbox authentication and actual delivery remain for the owner's manual test.

The legacy Outlook SMTP configuration `smtp.worldonline.co.za:25` was previously tested from Render and timed out. It is not the website SMTP endpoint. The current website configuration uses authenticated external SMTP at `smtp.mweb.co.za:587` with STARTTLS.

In `rps-website` → Environment, check the six variables above. Correct the non-secret values and preserve any existing password. If `EMAIL_HOST_PASSWORD` is missing, enter the actual Projects mailbox password manually before testing delivery. Do not reveal its value.

Do not change the configured SMTP host or port to work around a failure without agreeing the next step.

Run this in the deployed Render service's Shell (where available), rather than on a local computer, to check outbound TCP only. It does not authenticate, read credentials or send email:

```bash
python - <<'PY'
import socket

try:
    with socket.create_connection(("smtp.mweb.co.za", 587), timeout=5):
        print("TCP connection succeeds")
except ConnectionRefusedError:
    print("Connection refused")
except TimeoutError:
    print("Connection timed out; outbound port may be blocked")
except OSError:
    print("TCP connection failed; check DNS and outbound network access")
PY
```

## Local manual delivery test

In the same PowerShell window that starts Django, set the following. Replace the password placeholder privately with the real Projects mailbox password; never paste it into source, logs or chat. These variables apply to this shell and its child processes.

```powershell
$env:EMAIL_HOST="smtp.mweb.co.za"
$env:EMAIL_PORT="587"
$env:EMAIL_HOST_USER="projects@rpsswitchgearsa.co.za"
$env:EMAIL_HOST_PASSWORD="<ENTER PROJECTS MAILBOX PASSWORD>"
$env:EMAIL_USE_TLS="True"
$env:DEFAULT_FROM_EMAIL="RPS Switchgear SA Projects <projects@rpsswitchgearsa.co.za>"
$env:EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"

.\.venv\Scripts\python.exe manage.py runserver
```

The user manually submits the forms to test real delivery. Automated Opportunity tests use Django's in-memory backend with an empty SMTP password and never send external email:

```powershell
.\.venv\Scripts\python.exe manage.py test website.tests
.\.venv\Scripts\python.exe manage.py check
```
