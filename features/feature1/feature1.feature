Feature: Requesting get quote

  @f1s1
  Scenario: User requesting for get quote
    Given demo page is open
    When user enters full name as "Test User"
    And user enters contact number as "1234567890"
    And user enters email address as "test@test.com"
    And user click on button "get quote"
    Then validation message should be displayed