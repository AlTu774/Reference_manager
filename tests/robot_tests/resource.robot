*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  127.0.0.1:5000
${DELAY}  0.5 seconds
${HOME_URL}  http://${SERVER}
${ADD_URL}  http://${SERVER}/add
${LIST_URL}  http://${SERVER}/list

*** Keywords ***
Open And Configure Browser
    #${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    #Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Add Page Should Be Open
    Title Should Be  Uusi lähde

List Page Should Be Open
    Title Should Be  Lähdelista

Go To Add Page
    Go To  ${ADD_URL}

Go To List Page
    Go To  ${LIST_URL}
