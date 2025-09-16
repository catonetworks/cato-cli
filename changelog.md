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

## 2.1.2 (2025-08-28)

### Features

- Updated dynamic cli generator to support multi-threaded processing and fixed missing fields in sub operations
- Added support for custom documentation in cli generation process, first examples in appStats and appStatsTimeSeries

## 2.1.4 (2025-09-11)

### Features

- Added all latest APIs
- Updated bulk site export/import functions to include all nested attributes for socket_sites, interfaces, and network_ranges
- Added support for csv output for appStats, appStatsTimeSeries, accountMetrics, and socketPortMetricsTimeSeries operations with some examples in the readmes

## 2.1.6 (2025-09-15)

- Added licensing mutation support - New mutation_licensing parser for commercial license operations
- Enhanced export functionality - Added CSV export format support alongside existing JSON export for socket sites 
- Improved CSV import capabilities - Extended import functionality to support both JSON and CSV data sources for Terraform imports
- Enhanced WAN interface handling - Improved interface index formatting for better consistency (INT_X format)
- Improved network range management - Better handling of native ranges and default LAN interfaces in import/export workflows
- Updated query models - Refreshed device and events data models with latest API schema
- Code organization improvements - Reordered imports for better maintainability