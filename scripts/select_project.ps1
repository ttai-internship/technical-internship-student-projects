param(
  [Parameter(Mandatory = $true)]
  [ValidateSet("B00", "B01", "B02", "B03", "M01", "M02", "M03", "A01", "A02", "A03")]
  [string]$Project,

  [Alias("StudentId")]
  [string]$AssignmentId = "local-self-study",

  [ValidateSet("one-week", "one-month", "two-month", "half-year")]
  [string]$Duration = "one-week"
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$arguments = @(
  "scripts/select_project.py",
  "--project", $Project,
  "--assignment-id", $AssignmentId,
  "--duration", $Duration
)
& uv run --locked python @arguments
if ($LASTEXITCODE -ne 0) {
  throw "Project selection failed with exit code $LASTEXITCODE."
}
