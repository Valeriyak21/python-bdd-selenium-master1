Feature: Open page hab
  # Enter feature description here

  @test-tag10
  Scenario: Open page hab
    Given I open Habr URL in browser
    Then I see 'Хабр' in title
    When I click Войти button
    Then I see 'Вход' in title
    When I enter 'v.e.k@bk.ru' login
    And  I enter 'Htubcnhfwbz' password
    And  I click Войти
    When I click streams page
    Then I see 'Лучшие публикации за сутки' in title
    When I click hab page
    And  I click information security page
    Then I see 'Информационная безопасность' in title