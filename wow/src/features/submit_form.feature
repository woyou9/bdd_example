    Feature: Fill and submit the form

        Scenario: Fill all the required fields and then submit the form
                Given the user is on the practice form page
                When the user fills "Łukasz" in the required first name field
                And the user fills "Łojewski" in the required last name field
                And the user selects "Male" gender radio button
                And the user fills "5091509500" in the required mobile number field
                And the user uploads profile picture file
                And the user presses submit button
                Then the modal window with form summary should be visible
                And the form summary should contain filled fields values such as "Łukasz", "Łojewski", "5091509500" and "Male"
