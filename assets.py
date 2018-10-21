ASSETS = [
    {
        'label': 'AGRIF Ontology',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/def/agrif',
                'regex': '<h1>The Australian Government Records Interoperability Framework (AGRIF) ontology</h1>'
            }
        ]
    },
    {
        'label': 'GA Samples, Surveys, Sites',
        'uris': [
            {
                'address': 'http://pid.geoscience.gov.au/sample/?_format=text/turtle',
                'regex': 'rdfs:label \"Sample igsn:AU1000082\"\^\^xsd:string ;'
            },
            {
                'address': 'http://pid.geoscience.gov.au/sample/AU239?_format=text/turtle',
                'regex': 'rdfs:label \"Sample igsn:AU239\"\^\^xsd:string ;'
            },
            {
                'address': 'http://pid.geoscience.gov.au/survey/ga/?_format=text/turtle',
                'regex': '<http://pid.geoscience.gov.au/survey/ga/> a reg:Register ;'
            },
            {
                'address': 'http://pid.geoscience.gov.au/survey/ga/801?_format=text/turtle',
                'regex': '<http://pid.geoscience.gov.au/survey/ga/801> a gapd:PublicSurvey,'
            },
            {
                'address': 'http://pid.geoscience.gov.au/site/ga/?_format=text/turtle',
                'regex': 'rdfs:label \"Site 94\"\^\^xsd:string ;'
            },
            {
                'address': 'http://pid.geoscience.gov.au/site/ga/94?_format=text/turtle',
                'regex': 'rdfs:label \"Site 94\"\^\^xsd:string ;'
            }
        ]
    },
    {
        'label': 'AGIFT',
        'uris': [
            {
                'address': 'hhttps://data.naa.gov.au/def/agift.html',
                'regex': '<h1>Australian Governments\' Interactive Functions Thesaurus \(AGIFT\)</h1>'
            }
        ]
    }
]
