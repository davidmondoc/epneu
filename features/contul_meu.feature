Feature: loging in account
  Background:
    Given i am trying to login to my account but fail
    @test2
    Scenario:
      When i navigate to account login
      When i type in my email
      When i type in my password
      When i forgot my password
      When i return to my account page
      When i type in my email
      When i press autentificare
      Then i check if error message is displayed on password field