Feature: testing contact me function
  Background:
    Given i want to be contacted
    @test4
    Scenario:
    When i click on contact me button
    When i type in my name
    When i type in my phone no.
    When i type in my email address
    Then i send request
