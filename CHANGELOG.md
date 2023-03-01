# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.3] - 2023-02-27

### Changed
* wordformparts don't need to have a gloss (infixation)
* `Order` for inflectional categories is now a list and called `Value_Order`
* for multi-word forms with morph slices, the native `FormTable` is now used
* derivational processes have a language
* adding column `Morpho_Segments` to CLDF-native `FormTable`
* foreign `Lexeme_ID` key for `StemTable`
* lexeme's `Paradigm_View` as `json` column
* texts have a `Name`, not a `Title`

### Removed
* old `FormTable`

## [0.0.2] - 2023-02-19

### Fixed
* include data in MANIFEST.in

## [0.0.1] - 2022-02-19

Initial release

[Unreleased]: https://github.com/fmatter/cldf-ldd/compare/v0.0.3...HEAD
[0.0.3]: https://github.com/fmatter/cldf-ldd/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/fmatter/cldf-ldd/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/fmatter/cldf-ldd/compare/v0.0.1...v0.0.1