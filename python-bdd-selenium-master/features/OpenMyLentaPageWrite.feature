Feature: Open my lenta page
  # Enter feature description here

  @test-tag8
  Scenario: Open my lenta page
    Given I open Habr URL in browser
    Then I see 'Хабр' in title
    When I click Войти button
    Then I see 'Вход' in title
    When I enter 'v.e.k@bk.ru' login
    And  I enter 'Htubcnhfwbz' password
    And  I click Войти
    Then I click my lenta page
    And  I click write
