    Feature: Fill and submit the form

        Scenario: Fill all the required fields and then submit the form
                Given the user is on the practice form page
                When the user fills "Jakub" in the required first name field
                And the user fills "Kowalski" in the required last name field
                And the user selects "Male" gender radio button
                And the user fills "5091509500" in the required mobile number field
                And the user uploads profile picture file
                And the user presses submit button
                Then the modal window with form summary should be visible
                And the form summary should contain filled fields values such as "Jakub", "Kowalski", "5091509500" and "Male"

        Scenario: Secondary fill all the required fields and then submit the form
                Given the user is on the practice form page
                When the user fills "Jon" in the required first name field
                And the user fills "Doe" in the required last name field
                And the user selects "Other" gender radio button
                And the user fills "6092509500" in the required mobile number field
                And the user uploads profile picture file
                And the user presses submit button
                Then the modal window with form summary should be visible
                And the form summary should contain filled fields values such as "Jon", "Doe", "6092509500" and "Other"
