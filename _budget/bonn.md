---
name: Stadt Bonn
slug: bonn
tagline: "Haushaltsplan 2013/2014 der Stadt Bonn."
level: kommune
state: NW
budget:
  source: OpenData Bonn
  source_url: http://opendata.bonn.de/
  data_url: http://opendatalabs.org/misc/Plan_Haushalt_2013_2014-4-xlsx.csv

  dataset: de-bonn
  default: produkte

  filters:
    - field: 'year'
      name: 'Jahr'
      default: 2013
    - field: 'typ'
      name: 'Art'
      default: 'Aufwand'
    - field: 'vilv'
      name: 'Verrechnung'
      default: 'ohne sekundäre VILV'
      nullable: true

  hierarchies:
    produkte:
      name: Produkte
      drilldowns:
        - produktbereich
        - produktgruppe
---
