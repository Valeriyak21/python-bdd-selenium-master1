Feature: OpenAdmin
  # Enter feature description here

  @test-tag4
  Scenario: OpenAdmin page in Habr
    Given I open Habr URL in browser
    Then I see 'Хабр' in title
    When I click Администрирование page
    Then I see 'Администрирование' in title

    #Then I see repositories associated with this user