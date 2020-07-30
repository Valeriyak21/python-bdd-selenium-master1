Feature: Log in Habr
  # Enter feature description here

  @test-tag3
  Scenario: Log in Habr
    Given I open Habr URL in browser
    Then I see 'Хабр' in title
    When I click Войти button
    Then I see 'Вход' in title
    When I enter 'v.e.k@bk.ru' login
    And  I enter 'Htubcnhfwbz' password
    And  I click Войти
    Then I click account
    And  I get name account
    #Then I see repositories associated with this user
