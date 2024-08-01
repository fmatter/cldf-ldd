# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
* `Morphs` have `Form`s, not `Name`s

## [0.0.9] - 2024-08-01

### Fixed
* `forms.csv` reference to `formparts.csv`

## [0.0.8] - 2023-11-07

### Added
* `Language_ID` foreign keys

## [0.0.7] - 2023-11-06

### Added
* `Phrase_Number` for examples
* tags
* simple constructions

### Changed
* `Sentence_Number` instead of `Record_Number`

## [0.0.6] - 2023-06-27

### Added
* `Speaker_ID` as a foreign key in `ExampleTable`
* `Morph(emes)` and `Stems` can now have a `Part_Of_Speech`

### Fixed
* unavailable `SpeakerTable`
* speakers have `Name`s, not `Abbreviation`s (although they may be abbreviations)
* missing foreign key from wordformstems to wordforms
* missing foreign key from formparts to wordforms

### Changed
* `Gloss_ID` is optional for inflectional values

## [0.0.5] - 2023-03-04

### Added
* `PhonemeTable`
* `Segments` column for `StemTable` and `WordformTable` 
* `Part_Of_Speech` column for `WordformTable`
* foreign key: `Stem_ID` in `WordformStems`

### Changed
* derivations don't need to reference a specific morph in the target stem
* multi-valued index for stems in wordforms (morphologically complex stems, potentially bipartite)
* make multi-valued `Parameter_ID` (i.e., polysemy) the default

### Removed
* `Gloss_ID` column of `StemTable`

## [0.0.4] - 2023-03-01

### Changed
* texts have a `Name`, not a `Title`

## [0.0.3] - 2023-02-27

### Changed
* wordformparts don't need to have a gloss (infixation)
* `Order` for inflectional categories is now a list and called `Value_Order`
* for multi-word forms with morph slices, the native `FormTable` is now used
* derivational processes have a language
* adding column `Morpho_Segments` to CLDF-native `FormTable`
* foreign `Lexeme_ID` key for `StemTable`
* lexeme's `Paradigm_View` as `json` column

### Removed
* old `FormTable`

## [0.0.2] - 2023-02-19

### Fixed
* include data in MANIFEST.in

## [0.0.1] - 2022-02-19

Initial release

[Unreleased]: https://github.com/fmatter/cldf-ldd/compare/v0.0.9...HEAD
[0.0.9]: https://github.com/fmatter/cldf-ldd/compare/v0.0.8...v0.0.9
[0.0.8]: https://github.com/fmatter/cldf-ldd/compare/v0.0.7...v0.0.8
[0.0.7]: https://github.com/fmatter/cldf-ldd/compare/v0.0.6...v0.0.7
[0.0.6]: https://github.com/fmatter/cldf-ldd/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/fmatter/cldf-ldd/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/fmatter/cldf-ldd/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/fmatter/cldf-ldd/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/fmatter/cldf-ldd/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/fmatter/cldf-ldd/compare/v0.0.1...v0.0.1