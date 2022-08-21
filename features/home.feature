Feature: testing home page
  Background:
    Given i am an e-pneu user
    Scenario:
      When i type in search field
      When i search for tires
      When i select all-season tires
      When i click on logo
      Then i return to homepage

