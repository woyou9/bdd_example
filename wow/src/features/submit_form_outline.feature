    Feature: Fill and submit the form

        Scenario Outline: Fill all the required fields and then submit the form
                Given the user is on the practice form page
                When the user fills "<first_name>" in the required first name field
                And the user fills "<last_name>" in the required last name field
                And the user selects "<gender>" gender radio button
                And the user fills "<mobile_number>" in the required mobile number field
                And the user uploads profile picture file
                And the user presses submit button
                Then the modal window with form summary should be visible
                And the form summary should contain filled fields values such as "<first_name>", "<last_name>", "<mobile_number>" and "<gender>"
                Examples: First names, Last names, Mobile numbers, Genders
                        | first_name | last_name  | mobile_number | gender |
                        | Lucas      | Lucasowsky | 1234567899    | Male   |
                        | Cindy      | Sin        | 3213213210    | Female |
                        | Karen      | McLaren    | 6666666666    | Other  |
