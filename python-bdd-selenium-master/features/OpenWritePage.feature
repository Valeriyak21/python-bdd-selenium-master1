Feature: Open write page
  # Enter feature description here

  @test-tag7
  Scenario: Open write page
    Given I open Habr URL in browser
    Then I see 'Хабр' in title
    When I click Войти button
    Then I see 'Вход' in title
    When I enter 'v.e.k@bk.ru' login
    And  I enter 'Htubcnhfwbz' password
    And  I click Войти
    Then I click account
    When I click write button
    Then I see 'Программа повышения грамотности' in title