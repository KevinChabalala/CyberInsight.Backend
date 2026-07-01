# ==========================================================
# CyberInsight Backend Project Generator
# Author: CyberInsight Development Team
# Description:
# Creates the complete backend folder structure.
# ==========================================================

Write-Host ""
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "      CyberInsight Backend Generator"
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

# Root folders
$folders = @(
    ".github",
    ".github\ISSUE_TEMPLATE",
    ".github\workflows",

    "alembic",
    "docs",
    "scripts",
    "tests",

    "src",
    "src\cyberinsight",

    "src\cyberinsight\api",
    "src\cyberinsight\config",
    "src\cyberinsight\controllers",
    "src\cyberinsight\core",
    "src\cyberinsight\engines",
    "src\cyberinsight\middleware",
    "src\cyberinsight\models",
    "src\cyberinsight\repositories",
    "src\cyberinsight\schemas",
    "src\cyberinsight\services",
    "src\cyberinsight\utils"
)

foreach ($folder in $folders) {

    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Host "[Created] $folder" -ForegroundColor Green
    }
}

# Python packages
$packages = @(
    "src\cyberinsight",
    "src\cyberinsight\api",
    "src\cyberinsight\config",
    "src\cyberinsight\controllers",
    "src\cyberinsight\core",
    "src\cyberinsight\engines",
    "src\cyberinsight\middleware",
    "src\cyberinsight\models",
    "src\cyberinsight\repositories",
    "src\cyberinsight\schemas",
    "src\cyberinsight\services",
    "src\cyberinsight\utils",
    "tests"
)

foreach ($package in $packages) {

    $init = Join-Path $package "__init__.py"

    if (!(Test-Path $init)) {
        New-Item -ItemType File -Path $init | Out-Null
        Write-Host "[Created] $init" -ForegroundColor Yellow
    }
}

# Root files
$files = @(
    ".env.example",
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    "pyproject.toml",

    ".github\PULL_REQUEST_TEMPLATE.md",

    "src\cyberinsight\main.py"
)

foreach ($file in $files) {

    if (!(Test-Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
        Write-Host "[Created] $file" -ForegroundColor Cyan
    }
}

Write-Host ""
Write-Host "=============================================" -ForegroundColor Green
Write-Host " CyberInsight Backend Structure Created!"
Write-Host "=============================================" -ForegroundColor Green