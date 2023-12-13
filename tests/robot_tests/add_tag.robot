*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User

*** Test Cases ***
Add Valid Tag As User 
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
