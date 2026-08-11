param(
  [ValidateSet("all", "B00", "B01", "B02", "B03", "M01", "M02", "M03", "A01", "A02", "A03")]
  [string]$Project = "all"
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$uvArguments = @("sync", "--locked", "--python", "3.12")

if ($Project -eq "all") {
  $uvArguments += "--all-groups"
} else {
  $uvArguments += @("--group", "dev", "--group", "notebooks")
  if ($Project -eq "M01") { $uvArguments += @("--group", "ml") }
  if ($Project -eq "M02") { $uvArguments += @("--group", "dl") }
}

Push-Location $root
try {
  & uv @uvArguments
  if ($LASTEXITCODE -ne 0) { throw "uv sync failed for project scope: $Project" }
} finally {
  Pop-Location
}

$venvPython = Join-Path $root ".venv\Scripts\python.exe"
Write-Output "Environment ready: $venvPython"
Write-Output "Run: $venvPython scripts\validate_projects.py"
