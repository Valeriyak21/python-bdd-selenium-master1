Feature: Search text
  # Enter feature description here

  @test-tag5
  Scenario: Search text
    Given I open Habr URL in browser
    Then I see 'Хабр' in title
    When I click Search button
    And  I enter 'text' Search field
    Then I see 'Результаты поиска по запросу «text»' in title
