param(
  [Parameter(Mandatory = $true)]
  [ValidateSet("B01", "B02", "B03", "M01", "M02", "M03", "A01", "A02", "A03")]
  [string]$Project,

  [Parameter(Mandatory = $true)]
  [string]$StudentId,

  [ValidateSet("one-week", "one-month", "two-month", "half-year")]
  [string]$Duration = "one-week"
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$manifest = Get-Content -LiteralPath (Join-Path $root "config\projects.json") -Raw -Encoding UTF8 | ConvertFrom-Json
$entry = @($manifest.projects | Where-Object { $_.id -eq $Project })[0]

if ($null -eq $entry) {
  throw "Unknown project: $Project"
}

$selectionPath = Join-Path $root "PROJECT_SELECTION.json"
if (Test-Path -LiteralPath $selectionPath) {
  throw "PROJECT_SELECTION.json already exists; edit or remove it deliberately before selecting again."
}

$selection = [ordered]@{
  schema_version = 1
  student_id = $StudentId
  project_id = $entry.id
  level = $entry.level
  duration = $Duration
  branch_pattern = "feature/$Project-<slice>"
  task = $entry.task
  starter = $entry.starter
  notebook = $entry.notebook
}
$selection | ConvertTo-Json | Set-Content -LiteralPath $selectionPath -Encoding UTF8

Write-Output "Selected $($entry.id): $($entry.title)"
Write-Output "Task: $($entry.task)"
Write-Output "Starter: $($entry.starter)"
Write-Output "Notebook: $($entry.notebook)"
Write-Output "Commit PROJECT_SELECTION.json, then implement only the selected Core."
