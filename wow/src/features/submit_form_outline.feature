    Feature: Fill and submit the form

        Scenario Outline: Fill all the required fields and then submit the form
                Given the user is on the practice form page
                When the user fills "<first_name>" in the required first name field
                And the user fills "<last_name>" in the required last name field
                And the user selects gender radio button
                And the user fills "<mobile_number>" in the required mobile number field
                And the user uploads profile picture file
                And the user presses submit button
                Then the modal window with form summary should be visible
                Examples:
                        | first_name | last_name  | mobile_number |
                        | Lucas      | Lucasowsky | 1234567899    |
                        | Conor      | McGregor   | 3213213210    |
                        | Randy      | Random     | 9999999999    |
