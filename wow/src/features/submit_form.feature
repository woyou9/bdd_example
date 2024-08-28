    Feature: Fill the form

        Scenario: Fill all the required fields and then submit the form
                Given the user is on the practice form page
                When the user fills "Łukasz" in the required first name field
                When the user fills "Łojewski" in the required last name field
                When the user selects gender radio button
                When the user fills "5091509500" in the required mobile number field
                When the user presses submit button
                Then the modal window with form summary should be visible
