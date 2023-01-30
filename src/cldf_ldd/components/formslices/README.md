# FormSlices

A form slice connects a [morph](../morphs) with a [wordform](https://github.com/cldf/cldf/tree/master/components/forms).
The position of a morph in the form is specified with an `Index` column, delimiters like `-` in the `Form` column of the `FormTable` taking on the function of delimiting morphs.
**This is not a great solution**, but it works.

## FormSlices: `formslices.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
`Form_ID` | `string` | singlevalued | 
`Morph_ID` | `string` | singlevalued | 
`Index` | `string` | singlevalued | Specifies the position of a morph in a form.
`Morpheme_Meaning` | `string` | singlevalued | 
`Form_Meaning` | `string` | singlevalued | 