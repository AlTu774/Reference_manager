*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Add Valid Tag As User 
    Delete All Users
    Create User
    Click Link  Add tags
    Set Tag  Kandi
    Click Button  Submit
    Index Page Should Be Open
    skip

Duplicate Tag Is Not Added  
    Click Link  Add tags
    Set Tag  Kandi
    Click Button  Submit
    Tag Page Should Be Open
    Page Should Contain  Error: Tag by this name already exists.

Tag With Invalid Input Is Not Added
    Click Link  Add tags
    Set Tag  @Kandi
    Click Button  Submit
    
    Tag Page Should Be Open
    ${error}  Get Element Attribute  id=tag_name  title
    Should Be Equal  ${error}  Special characters are not allowed

Existing Tag Can Be Added To New Source
    Click Link  Add references
    Set Latex Key  AI101
    Set Title  ChatGPT ja Kanditutkielmat
    Set Author  Matti Luukkainen
    Set Publish Year  2023
    Set Publisher  Helsingin Yliopisto
    Click Element  Kandi
    Click Button  Submit
    Add Page Should Be Open
    # Todo: check that the added tag is visible on the reference
    skip

Tag Is Visible On Source
    skip

*** Keywords ***
Register And Go To Tag Page
    Create User
    Go To Tag Page

Create User
    Go To Register Page
    Write Username  user1
    Write Password1  password1
    Write Password2  password1
    Click Button  Register
