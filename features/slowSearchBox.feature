Feature: searching for tires using slow search box
  Background:
    Given i am using another methode to search for tires
    @test3
    Scenario:
      When i click on tire type
      When i click on width selection
      When i click on height selection
      When i click on diameter selection
      When i click on producer selection
      When i click on season selection
      Then i initiate search