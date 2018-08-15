.. code:: robotframework

   *** Settings ***
   Library       cal.py

   *** Variables ***
   ${MESSAGE}    2

   *** Test Cases ***
   My Test
       ${MESSAGE}=  phep cong  1   2
       Should Be Equal    ${MESSAGE}    ${3}

   Another Test
       Should Be Equal    ${MESSAGE}    3