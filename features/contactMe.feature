Feature: testing contact me function
  Background:
    Given i want to be contacted
    @test4
    When i click on contact me button
    When i type in my name
    When i type in my phone no.
    When i type in my email adress
    Then i send request
