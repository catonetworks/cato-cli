#!/bin/bash
#
# Cato CLI Test Runner
# 
# Usage:
#   ./run_tests.sh              # Run all tests
#   ./run_tests.sh --quick      # Run quick tests only
#   ./run_tests.sh --coverage   # Run with coverage report
#   ./run_tests.sh --verbose    # Run with verbose output
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Cato CLI Test Runner ===${NC}\n"

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo -e "${RED}Error: pytest is not installed${NC}"
    echo "Install test dependencies with:"
    echo "  pip install -r requirements.txt"
    exit 1
fi

# Parse arguments
QUICK_MODE=false
COVERAGE_MODE=false
VERBOSE_MODE=false

for arg in "$@"; do
    case $arg in
        --quick)
            QUICK_MODE=true
            ;;
        --coverage)
            COVERAGE_MODE=true
            ;;
        --verbose|-v)
            VERBOSE_MODE=true
            ;;
        --help|-h)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --quick      Run quick tests only (structure, models, payloads)"
            echo "  --coverage   Generate coverage report"
            echo "  --verbose    Run with verbose output"
            echo "  --help       Show this help message"
            exit 0
            ;;
        *)
            echo -e "${YELLOW}Unknown option: $arg${NC}"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Build pytest command
PYTEST_CMD="pytest test_cli_regression.py"

if [ "$QUICK_MODE" = true ]; then
    echo -e "${YELLOW}Running quick tests only...${NC}\n"
    PYTEST_CMD="$PYTEST_CMD -k 'TestCLIStructure or TestModelFiles or TestQueryPayloads'"
fi

if [ "$COVERAGE_MODE" = true ]; then
    echo -e "${YELLOW}Running with coverage...${NC}\n"
    PYTEST_CMD="$PYTEST_CMD --cov=catocli --cov-report=term --cov-report=html"
fi

if [ "$VERBOSE_MODE" = true ]; then
    PYTEST_CMD="$PYTEST_CMD -vv -s"
else
    PYTEST_CMD="$PYTEST_CMD -v"
fi

# Add color output
PYTEST_CMD="$PYTEST_CMD --color=yes"

# Run tests
echo -e "Running: ${GREEN}$PYTEST_CMD${NC}\n"
echo "======================================"

if eval $PYTEST_CMD; then
    echo ""
    echo "======================================"
    echo -e "${GREEN}✓ All tests passed!${NC}"
    
    if [ "$COVERAGE_MODE" = true ]; then
        echo ""
        echo "Coverage report generated at: htmlcov/index.html"
        echo "Open with: open htmlcov/index.html (macOS) or xdg-open htmlcov/index.html (Linux)"
    fi
    
    exit 0
else
    echo ""
    echo "======================================"
    echo -e "${RED}✗ Some tests failed${NC}"
    echo ""
    echo "Tips:"
    echo "  - Run with --verbose for more details"
    echo "  - Check individual test classes: pytest tests/test_cli_regression.py::TestClassName -v"
    echo "  - Stop on first failure: pytest tests/test_cli_regression.py -x"
    exit 1
fi
