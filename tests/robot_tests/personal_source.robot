*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Register And Go Check Add Page
#Test Teardown  Reset Application

*** Test Cases ***
List Does Not Show Other User Sources
    Create User And Go Add Page  user2
    Set Tag  JTKT1
    Set Title  Johdatus Tietojenkäsittelyyn
    Set Author  Matti Luukkainen
    Set Publish Year  2018
    Set Publisher  WSOY
    Click Button  Submit
    Add Page Should Be Open

    Click Loink  Logout

    Create User And Go Add Page  user2

    Click Link  List all references
    List Page Should Be Open

    Page Should Not Contain  @JTKT
    Page Should Not Contain  Johdatus Tietojenkäsittelyyn
    Page Should Not Contain  Matti Luukkainen
    Page Should Not Contain  2018
    Page Should Not Contain  WSOY

*** Keywords ***
Create User And Go Add Page
    [Arguments]  ${user}
    Go To Register Page
    Write Username  ${username}
    Write Password1  password1
    Write Password2  password1
    Click Button  Register
    Go And Check Add Page
