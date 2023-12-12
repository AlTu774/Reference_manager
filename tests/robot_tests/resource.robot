*** Settings ***
Library  SeleniumLibrary
#Library  ../../app_library.py

*** Variables ***
${SERVER}  127.0.0.1:5000
${DELAY}  0 seconds
${HOME_URL}  http://${SERVER}
${ADD_URL}  http://${SERVER}/add
${LIST_URL}  http://${SERVER}/list
${REGISTER_URL}  http://${SERVER}/register
${LOGOUT_URL}  http://${SERVER}/logout
${LOGIN_URL}  http://${SERVER}/login
${DELETE_URL}  http://${SERVER}/reset_users

*** Keywords ***

# Uncomment line with ChromeOptions and comment line with FirefoxOptions
#   to use corresponding browser for tests.
# Headless option disables physical browser opening.
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    #${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Add Page Should Be Open
    Title Should Be  New reference

List Page Should Be Open
    Title Should Be  List of references

Go To Add Page
    Go To  ${ADD_URL}

Go To List Page
    Go To  ${LIST_URL}

Go To Register Page
    Go To  ${REGISTER_URL}

Go To Logout Page
    Go To  ${LOGOUT_URL}

Go To Login Page
    Go To  ${LOGIN_URL}

Delete All Users
    Go To  ${DELETE_URL}

Index Page Should Be Open
    Title Should Be  Reference manager

Register Page Should Be Open
    Title Should Be  Register

Write Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Write Password1
    [Arguments]  ${password}
    Input Text  password  ${password}

Write Password2
    [Arguments]  ${password2}
    Input Text  password2  ${password2}

Go and Check Add Page
    Go To Add Page
    Add Page Should Be Open

Set Tag
    [Arguments]  ${tag}
    Input Text  tag  ${tag}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Publish Year
    [Arguments]  ${publish_year}
    Input Text  publish_year  ${publish_year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}