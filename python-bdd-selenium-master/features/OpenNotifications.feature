Feature: Open Notifications
  # Enter feature description here

  @test-tag6
  Scenario: Open Notifications
    Given I open Habr URL in browser
    Then I see 'Хабр' in title
    When I click Войти button
    Then I see 'Вход' in title
    When I enter 'v.e.k@bk.ru' login
    And  I enter 'Htubcnhfwbz' password
    And  I click Войти
    Then I click account
    When I click notifications button
    Then I see 'Трекер' in title