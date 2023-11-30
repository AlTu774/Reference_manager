*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go And Check Add Page

*** Test Cases ***
Add Source With Valid Fields
    Set Tag  JTKT1
    Set Title  Johdatus Tietojenkäsittelyyn
    Set Author  Matti Luukkainen
    Set Publish Year  2018
    Set Publisher  WSOY
    Click Button  Submit
    Click Link  Listaa lähteet
    List Page Should Be Open

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

*** Keywords ***
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