param(
  [string]$EnvironmentName = "technical-internship"
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
if (-not (Get-Command conda -ErrorAction SilentlyContinue)) {
  throw "Conda was not found on PATH. Install Miniconda or Miniforge first."
}

Push-Location $root
try {
  & conda env update --name $EnvironmentName --file environment.yml --prune
  if ($LASTEXITCODE -ne 0) { throw "conda env update failed for $EnvironmentName" }

  & conda run --name $EnvironmentName python scripts\validate_projects.py
  if ($LASTEXITCODE -ne 0) { throw "Conda validation failed for $EnvironmentName" }
} finally {
  Pop-Location
}

Write-Output "Conda environment ready: $EnvironmentName"
Write-Output "Run commands with: conda run --name $EnvironmentName python ..."
