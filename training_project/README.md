# hillel_hw_orangehrmlive

hillel_hw_orangehrmlive is a Python library for testing OrangeHRM system (https://opensource-demo.orangehrmlive.com/web/index.php/auth/login).

## Installation

Use https://github.com/YuliaMag/hillel_hw_orangehrmlive.git to download hillel_hw_orangehrmlive


## Usage

### Test Scenarios

#### Valid credentials
test_successful_login.py
##### Description:
- Verify that a user can successfully log in with valid credentials.
##### Steps:
- Open the login page.
- Enter valid username and password.
- Click on the login button.
- Verify that the user is redirected to the dashboard page.

#### Invalid password
test_unsuccessful_login.py
##### Description:
- Verify the error message when entering an invalid password.
- Verify the user remains on the login page.
##### Steps:
- Open the login page.
- Enter a valid username and an invalid password.
- Click on the login button.
- Verify that the user remains on the login page.
- Verify the error message displayed.

#### Forgot your password redirection
test_forgot_password_redirect.py
##### Description:
- Verify the functionality of the "Forgot your password?" link.
##### Steps:
- Open the login page.
- Click on the "Forgot your password?" link.
- Verify that the user is redirected to the password reset page.

#### Reset password cancellation
reset_password_cancel.py
##### Description:
- Verify that Cancel button returns the user to the login page.
##### Steps:
- Open the login page.
- Click on the "Forgot your password?" link.
- On the password reset page click Cancel button.
- Verify that the user is redirected to the login page.

#### Reset password submit
reset_password_reset.py
##### Description: 
- Verify that Reset Password button redirects the user to the "Reset Password link sent successfully" message page.
##### Steps:
- Open the login page.
- Click on the "Forgot your password?" link.
- On the password reset page click Reset Password button.
- Verify that the user is redirected to the "Reset Password link sent successfully" message page.


## Contributing

For training purposes

## License

--