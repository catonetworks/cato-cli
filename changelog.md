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

## 2.1.8 (2025-09-15)

- Updated path to settings file

## 3.0.0 (2025-09-24)

- Updated eventFeed operation to support persistent marker and -run to pull events continuously
- Embedded SCIM SDK into catocli, updating authentication management to prompt for bearer token and scim baseurl, supporting the following operations:
    •  catocli scim add_members - Add members to SCIM group
    •  catocli scim create_group - Create new SCIM group  
    •  catocli scim create_user - Create new SCIM user
    •  catocli scim disable_group - Disable SCIM group
    •  catocli scim disable_user - Disable SCIM user
    •  catocli scim find_group - Find groups by display name
    •  catocli scim find_users - Find users by field/value
    •  catocli scim get_group - Get specific SCIM group
    •  catocli scim get_groups - Get all SCIM groups
    •  catocli scim get_user - Get specific SCIM user
    •  catocli scim get_users - Get all SCIM users  
    •  catocli scim remove_members - Remove members from SCIM group
    •  catocli scim rename_group - Rename SCIM group
    •  catocli scim update_group - Update SCIM group
    •  catocli scim update_user - Update SCIM user
- Updated the socket_site export/import to support csv and json to align with bulk socket site module

## 3.0.2 (2025-09-24)

- Minor fix to support import lan_lag_member in csv
- Added support for generating csv and json templates for export/import
- Fixed path issue to be OS agnostic for local template for generating templates

## 3.0.3 (2025-09-24)

- Updated manifest file to include template directory

## 3.0.4 (2025-09-26)

- Updated csv formatting for appStatsTimeSeries, and socketPortMetricsTimeSeries 

## 3.0.8 (2025-10-08)

- Added bulk import, export, and purge for scim users and groups for json and csv, as well as options to generate templates
- Updated dynamic schema generation to format examples with pretty print as well as single line json blob
- OS context aware help menus for unix vs windows, and multi-line json input for both unix and windows
- Added comprehensive timeframe examples to dynamic readme generation process (appStats, socketPortMetrics, etc)

## 3.0.18 (2025-10-09)

- Upated cli to support multi-line json input for ease of use for windows and unix
- Updated eventsFeed with marker and run, and included --append-new-line for Chronicle support
- Updated help menu formatting to be dynamic for windows powershell
- Added custom report examples in readme and help menu for appStats, and appStatsTimeSeries
- Updated custom exmaples to render properly for windows
- Minor fix for readme for eventsFeed, and exception handling in menu for configure with no -h
- Updated eventsFeed help menu to properly render on Windows systems
- Updated SCIM client removing external_id from standard client to pull from url

## 3.0.22 (2025-10-15)
- Added custom reports for query.accountMetrics, query.appStats, query.appStatsTimeSeries, query.eventsTimeSeries, query.socketPortMetrics, query.socketPortMetricsTimeSeries, updating format to human readable output
- Added -f csv for custom reports
- Updated report generation to be a part of dynamic cli generation process
- Fixed examples for socketPortMetrics
