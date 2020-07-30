Feature: Open Development Page
  # Enter feature description here


  Scenario: OpenDevelopmentPage
    Given I open Habr URL in browser
    Then I see 'Хабр' in title
    When I click Войти button
    Then I see 'Вход' in title
    When I enter 'v.e.k@bk.ru' login
    And  I enter 'Htubcnhfwbz' password
    And  I click Войти
    Then I click development page
    And  I see 'Разработка' in title
