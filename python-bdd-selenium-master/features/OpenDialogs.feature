Feature: Open Dialogs
  # Enter feature description here

  @test-tag5
  Scenario: Open Dialogs
    Given I open Habr URL in browser
    Then I see 'Хабр' in title
    When I click Войти button
    Then I see 'Вход' in title
    When I enter 'v.e.k@bk.ru' login
    And  I enter 'Htubcnhfwbz' password
    And  I click Войти
    Then I click account
    When I click Диалоги page
    Then I see 'Сообщения' in title
