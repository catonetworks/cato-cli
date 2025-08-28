# Changelog

## 2.0.1 (2025-07-05)

### Features
- Refactored authentication to support multiple profiles in a ini format
- Added export functions for IFW and WAN rules and sections into json
- Added import function into tf module for backup and restore, adjusted to use name of section and rule instead of index in source data to align with accompanying module 

## 2.1.0 (2025-08-22)

### Features

- Optimized exception handling for bulk rule import 
- Added exception handling keyboard escape 
- Added custom settings support

## 2.1.2 (2025-08-228)

### Features

- Updated dynamic cli generator to support multi-threaded processing and fixed missing fields in sub operations
- Added support for custom documentation in cli generation process, first examples in appStats and appStatsTimeSeries
