*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Register And Go Check Add Page
#Test Teardown  Reset Application

*** Test Cases ***
Add Source With Valid Fields
    Set Tag  JTKT1
    Set Title  Johdatus Tietojenkäsittelyyn
    Set Author  Matti Luukkainen
    Set Publish Year  2018
    Set Publisher  WSOY
    Click Button  Submit
    Add Page Should Be Open

    Click Link  List all references
    List Page Should Be Open

    Page Should Contain  @JTKT
    Page Should Contain  Johdatus Tietojenkäsittelyyn
    Page Should Contain  Matti Luukkainen
    Page Should Contain  2018
    Page Should Contain  WSOY

Add Source With Missing Title
    Set Tag  JTKT1
    Set Author  Matti Luukkainen
    Set Publish Year  2018
    Set Publisher  WSOY
    Click Button  Submit

    Add Page Should Be Open
    Element Should Be Visible  css=input#title:required:invalid

Add Source With Missing Author
    Set Tag  JTKT1
    Set Title  Johdatus Tietojenkäsittelyyn
    Set Publish Year  2018
    Set Publisher  WSOY
    Click Button  Submit

    Add Page Should Be Open
    Element Should Be Visible  css=input#author:required:invalid

Add Source With Whitespace
    Set Tag  JTKT1
    Set Title  Johdatus Tietojenkäsittelyyn ${SPACE}
    Set Author  Matti Luukkainen
    Set Publish Year  2018
    Set Publisher  WSOY
    Click Button  Submit

    Add Page Should Be Open
    ${error}  Get Element Attribute  id=title  title
    Should Be Equal  ${error}  Remove leading or trailing spaces

Add Source With Invalid Year
    Set Tag  JTKT1
    Set Title  Johdatus Tietojenkäsittelyyn
    Set Author  Matti Luukkainen
    Set Publish Year  kaksi
    Set Publisher  WSOY
    Click Button  Submit

    Add Page Should Be Open
    ${error}  Get Element Attribute  id=publish_year  title
    Should Be Equal  ${error}  Please enter a valid year


*** Keywords ***
Register And Go Check Add Page
    Create User
    Go And Check Add Page

Create User
    Go To Register Page
    Write Username  user1
    Write Password1  password1
    Write Password2  password1
    Click Button  Register
