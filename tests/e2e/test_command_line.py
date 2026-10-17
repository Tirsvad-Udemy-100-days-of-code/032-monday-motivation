import os
import subprocess
import sys
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parents[2] / "src"


def _run(cwd: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    environ = {"PYTHONPATH": str(SOURCE_DIR)}
    for name in ("SYSTEMROOT", "SYSTEMDRIVE"):
        if name in os.environ:
            environ[name] = os.environ[name]
    return subprocess.run(
        [sys.executable, "-m", "monday_motivation", *arguments],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=environ,
        cwd=cwd,
        timeout=60,
        check=False,
    )


def test_module_dry_run_force_prints_subject(tmp_path: Path) -> None:
    result = _run(tmp_path, "--dry-run", "--force")
    assert result.returncode == 0
    assert "Subject: Monday Motivation" in result.stdout


def test_module_help_exits_zero(tmp_path: Path) -> None:
    assert _run(tmp_path, "--help").returncode == 0
