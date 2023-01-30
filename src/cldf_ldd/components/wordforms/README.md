# Wordforms


## WordformTable: `wordforms.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | singlevalued | A reference to a language (or variety) the form belongs to<br>References LanguageTable
[Form](http://cldf.clld.org/v1.0/terms.rdf#form) | `string` | singlevalued | The written expression of the form.
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | unspecified | A reference to the meaning denoted by the form<br>References ParameterTable
`Parts` | list of `string` (separated by ` `) | multivalued | The form of the stem, segmented into morphs. Necessary for modeling morphologically complex stems.
`Stem_ID` | `string` | singlevalued | The stem of which this wordform is an inflected form. References StemTable (stems.csv)
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | singlevalued | A free translation of the wordform.
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | unspecified | <div> <p> A human-readable comment on a resource, providing additional context. </p> </div> 