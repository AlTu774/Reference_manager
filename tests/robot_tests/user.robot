*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***

Can't Register With Existing Username
    Go To Register Page
    Write Username  user1
    Write Password1  password1
    Write Password2  password1
    Click Button  Register
    Register Page Should Be Open

Can Log Out
    Go To Register Page
    Write Username  user1
    Write Password1  password1
    Write Password2  password2
    Click Button  Register
    Go To Logout Page

Can Login With Right Username And Password
    Go To Login Page
    Write Username  user1
    Write Password1  password1
    Click Button  Login
    Index Page Should Be Open

Can't Login With Wrong Username
    Go To Register Page
    Write Username  user123
    Write Password1  password1
    Click Button  Register
    Register Page Should Be Open


Can't Login With Wrong Password
    Go To Register Page
    Write Username  user1
    Write Password1  password
    Click Button  Register
    Register Page Should Be Open

Register New User
    Delete All Users
    Go To Register Page
    Write Username  user2233
    Write Password1  password123
    Write Password2  password123
    Click Button  Register
    Index Page Should Be Open

*** Keywords ***
Create User And Go To Register Page
    Go To Register Page
    Write Username  user1
    Write Password1  password1
    Write Password2  password1
    Click Button  Register
    Go To Logout Page
    Go To Register Page

Write Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Write Password1
    [Arguments]  ${password}
    Input Text  password  ${password}

Write Password2
    [Arguments]  ${password2}
    Input Text  password2  ${password2}
