    Feature: Fill the form

        Scenario Outline: Fill all the required fields and then submit the form
                Given the user is on the practice form page
                When the user fills "<first_name>" in the required first name field
                When the user fills "<last_name>" in the required last name field
                When the user selects gender radio button
                When the user fills "<mobile_number>" in the required mobile number field
                When the user presses submit button
                Then the modal window with form summary should be visible
                Examples:
                        | first_name | last_name  | mobile_number |
                        | Lucas      | Lucasowsky | 1234567899    |
                        | Randy      | Orton      | 9999999999    |
                        | Conor      | McGregor   | 3213213210    |