# Changelog

## [v1.0.5] - 2024-07-02
#### Added
- Implemented JSON format validation to ensure the uploaded file adheres to the required structure.

#### Changed
- Updated the label for the file input to be more descriptive: "Select the exported ChatGPT Conversation JSON file".
- Added explanatory comments to all major functions for better code readability and maintenance.

## [v1.0.4] - 2024-07-01
#### Changes
- Updated `README.md` for better organization and clarity.
- Organized screenshot files under `assets` folder for easier exclusion when exporting a project archive.

## [v1.0.3] - 2024-06-30
#### Changes
- Updated the title of the HTML page.

## [v1.0.2] - 2024-06-30
#### Changes
- Added a fallback error message when loading GPTTokenizer_cl100k_base fails.
  - Added message: "Switch to Fallback: rough approximation based on the number of words."
 
## [v1.0.1] - 2024-06-30
#### Added
- Implemented the ability to load the `GPTTokenizer_cl100k_base` encoder from a local source if the remote JavaScript file is not accessible. This ensures privacy and offline functionality.
- Added a fallback mechanism that approximates token count based on the number of words if both remote and local tokenizer scripts are unavailable.

#### Changed
- Updated the download icon to use an inline SVG instead of relying on Font Awesome. This change further enhances the privacy of the tool by removing external dependencies.

## [v1.0.0] - 2024-06-29
#### Added
- Initial Release 1.0.0


