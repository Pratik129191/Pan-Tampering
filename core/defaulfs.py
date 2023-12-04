from typing import Final


# Constants for sending password-reset emails.
LOGO_FILE_PATH: Final[str] = "img/logo.png"
LOGO_CID_NAME: Final[str] = "logo"
PASSWORD_RESET_FORM_TEMPLATE: Final[str] = "registration/password_reset_form.html"
PASSWORD_RESET_HTML_TEMPLATE: Final[str] = "registration/password_reset_email.html"
PASSWORD_RESET_TEXT_TEMPLATE: Final[str] = "registration/password_reset_email.txt"
PASSWORD_RESET_SUBJECT_TEMPLATE: Final[str] = "registration/password_reset_subject.txt"
SUPPORT_EMAIL: Final[str] = "YOUR_SUPPORT_EMAIL_ADDRESS"
FROM_EMAIL: Final[str] = f"YOUR_COMPANY_NAME Support <{SUPPORT_EMAIL}>"


