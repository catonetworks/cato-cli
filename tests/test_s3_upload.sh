#!/bin/bash
# Test script to run tests with S3 upload simulation
# This script simulates the S3 upload with test data
#
# Optional environment variables:
#   S3_CATOMATIC_TIMESTAMP - Timestamp in milliseconds (default: auto-generate)

cd "$(dirname "$0")/.."

echo "Running tests with S3 upload simulation..."
echo ""

# Build command with optional timestamp
S3_CMD="python3 tests/run_all_tests.py \
    --skip-validation \
    --json-output tests/results/ \
    --s3-upload \
    --s3-region eu-central-1 \
    --s3-bucket external-test-results \
    --s3-test-framework-repo-name cato-cli_tf_ci_read_only_tests \
    --s3-catomatic-cycle cctest \
    --s3-catomatic-run-id 123 \
    --s3-catomatic-suite-name mysuite"
    --s3-catomatic-timestamp 176414

# Add timestamp if provided
if [ -n "$S3_CATOMATIC_TIMESTAMP" ]; then
    S3_CMD="${S3_CMD} --s3-catomatic-timestamp ${S3_CATOMATIC_TIMESTAMP}"
fi

S3_CMD="${S3_CMD} --verbose"

eval $S3_CMD

echo ""
echo "Test run completed!"

