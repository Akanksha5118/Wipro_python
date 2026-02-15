*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${baseurl}    http://127.0.0.1:5000

*** Test Cases ***

Create new user
    Create Session    postingsession    ${baseurl}
    ${data}=    Create Dictionary    name=varsha
    ${response}=    POST On Session    postingsession    /users    json=${data}
    Status Should Be    201    ${response}
    ${user_json}=    To Json    ${response.text}
    Log    ${user_json}    console=True

