"""Omni の Core の公開 API を DocFX で Markdown にして、Omni/docs/api/ に置く。

使い方:
    python -I tools/generate_omni_api.py <Omni のフォルダ> [作業フォルダ]

- Unity が作った *.csproj を使う。先に Omni を Unity で開いておく。
- CI では動かせない（Unity の DLL が要る）。手元で動かし、出来た Markdown をコミットする。
- 対象は Assets/Omni/Core の asmdef のうち、検証用の Core/Verification を除いたもの。
- DocFX は `dotnet tool install -g docfx` で入れる。
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
DOC_ROOT = TOOLS.parent
API_OUT = DOC_ROOT / "Omni" / "docs" / "api"

sys.path.insert(0, str(TOOLS))
import omni_api_postprocess  # noqa: E402


def core_projects(omni_root: Path):
    names = set()
    for asmdef in (omni_root / "Assets" / "Omni" / "Core").rglob("*.asmdef"):
        if "Verification" in asmdef.parts:
            continue
        names.add(json.loads(asmdef.read_text(encoding="utf-8-sig"))["name"])
    projects = []
    for name in sorted(names):
        csproj = omni_root / f"{name}.csproj"
        if not csproj.exists():
            sys.exit(f"{csproj.name} がありません。Omni を Unity で開き、csproj を作ってから動かしてください。")
        projects.append(csproj.name)
    return projects


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    omni_root = Path(sys.argv[1]).resolve()
    work = Path(sys.argv[2] if len(sys.argv) > 2 else r"D:\CodexTemp\OmniApi")
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    config = {
        "metadata": [{
            "src": [{"src": omni_root.as_posix(), "files": core_projects(omni_root)}],
            "output": "md",
            "outputFormat": "markdown",
            "namespaceLayout": "flattened",
            "memberLayout": "samePage",
            "disableGitFeatures": True,
        }]
    }
    (work / "docfx.json").write_text(json.dumps(config, indent=2), encoding="utf-8")

    result = subprocess.run(["docfx", "metadata", "docfx.json"], cwd=work, shell=(sys.platform == "win32"))
    if result.returncode != 0:
        sys.exit(f"docfx metadata が失敗しました（終了コード {result.returncode}）。")

    sys.argv = [sys.argv[0], str(work / "md"), str(API_OUT)]
    omni_api_postprocess.main()
    shutil.rmtree(work)
    print(f"API リファレンスを {API_OUT} に作りました。")


if __name__ == "__main__":
    main()
