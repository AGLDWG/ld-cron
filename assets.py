ASSETS = [
    #
    #    AGLDWG
    #
    {
        'label': 'AGRIF Ontology',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/def/agrif',
                'regex': '<h1>The Australian Government Records Interoperability Framework \(AGRIF\) ontology</h1>'
            }
        ]
    },
    {
        'label': 'Dataset Ontology',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/def/dataset',
                'regex': '\<h1\>Dataset Ontology\<\/h1\>'
            }
        ]
    },
    {
        'label': 'FSDF Ontology',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/def/fsdf',
                'regex': '\<h1\>FSDF ontology\<\/h1\>'
            }
        ]
    },
    {
        'label': 'G-NAF Dataset',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/dataset/gnaf',
                'regex': '\<h1\>G-NAF LDAPI\<\/h1\>'
            }
        ]
    },
    {
        'label': 'G-NAF Ontology',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/def/gnaf',
                'regex': '\<h1\>GNAF ontology\<\/h1\>'
            }
        ]
    },
    {
        'label': 'ISO19160 Ontology',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/def/iso19160-1-address',
                'regex': '\<h1\>ISO19160-1\:2015 Address ontology\<\/h1\>'
            }
        ]
    },
    {
        'label': 'ISO19160 NZ Profile Ontology',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/def/iso19160-1-address-nz-profile',
                'regex': '\<h1\>ISO19160-1\:2015 Address ontology - NZ Profile\<\/h1\>'
            }
        ]
    },
    {
        'label': 'Place Names Ontology',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/def/placenames',
                'regex': '\<h1\>Place Names Ontology\<\/h1\>'
            }
        ]
    },
    {
        'label': 'Registry Ontology\'s Status Vocabulary',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/def/reg-status',
                'regex': '\<h1\>Registry Status Vocabulary\<\/h1\>'
            }
        ]
    },
    #
    #    Non-AGLDWG
    #
    {
        'label': 'AGIFT',
        'uris': [
            {
                'address': 'https://data.naa.gov.au/def/agift.html',
                'regex': '<h1>Australian Governments\' Interactive Functions Thesaurus \(AGIFT\)</h1>'
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
    }
]
