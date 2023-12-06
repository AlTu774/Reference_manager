*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register New User
    Write Username  user1
    Write Password1  password1
    Write Password2  password2
    Click Button  Submit
    Index Page Should Be Open

Can't Register With Existing Username


*** Keywords ***
Write Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Write Password1
    [Arguments]  ${password}
    Input Text  password  ${password}

Write Password2
    [Arguments]  ${password2}
    Input Text  password2  ${password2}
