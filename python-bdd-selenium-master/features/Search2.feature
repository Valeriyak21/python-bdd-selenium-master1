Feature: Search dimbbass
  As user
  I want to have a possibility to search repositories, users and so on

  @test-tag2
  Scenario: Search by user name
    Given I open Github URL in browser
    Then I see 'GitHub' in title
    When I search 'user:dimbbass' text
    Then I see repositories associated with this user
