"""DocFX が出した Markdown を、MkDocs の API リファレンスとして読みやすく整える。

使い方: python -I omni_api_postprocess.py <docfx の出力フォルダ> <置き場所 (Omni/docs/api)>

- 受け継いだ名前の長い一覧（Inherited Members）を消す。
- 見出しに日本語を添える。
- toc.yml から、名前空間ごとの一覧ページ（index.md）を作る。
"""

import re
import shutil
import sys
from pathlib import Path

HEADINGS = {
    "Inheritance": "継承（Inheritance）",
    "Derived": "派生した型（Derived）",
    "Implements": "実装するインターフェース（Implements）",
    "Constructors": "コンストラクター（Constructors）",
    "Fields": "フィールド（Fields）",
    "Properties": "プロパティ（Properties）",
    "Methods": "メソッド（Methods）",
    "Events": "イベント（Events）",
    "Operators": "演算子（Operators）",
    "Parameters": "引数（Parameters）",
    "Returns": "戻り値（Returns）",
    "Property Value": "値（Property Value）",
    "Field Value": "値（Field Value）",
    "Event Type": "型（Event Type）",
    "Type Parameters": "型引数（Type Parameters）",
    "Remarks": "補足（Remarks）",
    "Examples": "例（Examples）",
    "Exceptions": "例外（Exceptions）",
    "See Also": "関連（See Also）",
    "Extension Methods": "拡張メソッド（Extension Methods）",
    "Classes": "クラス（Classes）",
    "Structs": "構造体（Structs）",
    "Interfaces": "インターフェース（Interfaces）",
    "Enums": "列挙型（Enums）",
    "Delegates": "デリゲート（Delegates）",
    "Namespaces": "名前空間（Namespaces）",
}

HEADING_RE = re.compile(r"^(#{2,4}) (.+?)\s*$")
KIND_ORDER = ["Classes", "Structs", "Interfaces", "Enums", "Delegates"]


def strip_inherited(lines):
    out, skipping = [], False
    for line in lines:
        if line.startswith("#### Inherited Members"):
            skipping = True
            continue
        if skipping and line.startswith("#"):
            skipping = False
        if not skipping:
            out.append(line)
    return out


def translate_headings(lines):
    out = []
    for line in lines:
        m = HEADING_RE.match(line)
        if m and m.group(2) in HEADINGS:
            line = f"{m.group(1)} {HEADINGS[m.group(2)]}"
        out.append(line)
    return out


def parse_toc(toc_path):
    """toc.yml を、[(名前空間, href, {種類: [(名前, href)]})] に読む。YAML ライブラリに頼らない。"""
    namespaces = []
    current = None
    kind = None
    pending_name = None
    for raw in toc_path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("- name: "):
            current = (raw[8:].strip(), None, {})
            namespaces.append(current)
            kind = None
            continue
        if current is None:
            continue
        stripped = raw.strip()
        if raw.startswith("  href: "):
            namespaces[-1] = current = (current[0], stripped[6:], current[2])
        elif stripped.startswith("- name: "):
            name = stripped[8:]
            if name in KIND_ORDER:
                kind = name
                current[2].setdefault(kind, [])
                pending_name = None
            else:
                pending_name = name
        elif stripped.startswith("href: ") and pending_name and kind:
            current[2][kind].append((pending_name, stripped[6:]))
            pending_name = None
    return namespaces


def write_index(namespaces, dest):
    total = sum(len(v) for _, _, kinds in namespaces for v in kinds.values())
    lines = [
        "# API リファレンス",
        "",
        "Omni の本体（`Assets/Omni/Core`）の **public な型**を、ソースコードのコメントから自動で作った一覧です。",
        "検証用（`Core/Verification`）、テスト、デモ、開発用のコードは入っていません。",
        "",
        f"名前空間 {len(namespaces)} 個、型 {total} 個。",
        "",
        "!!! note \"読み方\"",
        "    説明の文は、ソースコードに書かれたコメントそのままです。入門向けの言い換えはしていません。",
        "    部品の役割をやさしく知りたいときは、先に「Omni の基本」と「使い方」を読んでください。",
        "",
        "| 名前空間 | 型の数 |",
        "|---|---|",
    ]
    for ns, href, kinds in namespaces:
        count = sum(len(v) for v in kinds.values())
        lines.append(f"| [{ns}]({href}) | {count} |")
    lines.append("")
    for ns, href, kinds in namespaces:
        lines.append(f"## {ns}")
        lines.append("")
        for kind in KIND_ORDER:
            items = kinds.get(kind)
            if not items:
                continue
            links = "、".join(f"[{name}]({h})" for name, h in items)
            lines.append(f"**{HEADINGS[kind]}**: {links}")
            lines.append("")
    (dest / "index.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main():
    src, dest = Path(sys.argv[1]), Path(sys.argv[2])
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    count = 0
    for path in sorted(src.glob("*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        lines = translate_headings(strip_inherited(lines))
        (dest / path.name).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
        count += 1
    write_index(parse_toc(src / "toc.yml"), dest)
    print(f"{count} pages -> {dest}")


if __name__ == "__main__":
    main()
