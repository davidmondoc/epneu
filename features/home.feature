Feature: testing home page
  Background:
    Given i am an e-pneu user

    @test1
    Scenario:
      When i type in search field
      When i search for tires
      When i select all-season tires
      When i click on logo
      Then i return to homepage

    @test2
    Scenario:
      When i click on tire type
      When i click on width selection
      When i click on height selection
      When i click on diameter selection
      When i click on producer selection
      When i click on season selection
      Then i initiate search

