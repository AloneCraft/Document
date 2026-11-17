# AloneCraft のドキュメント

開発したものの解説をまとめています。

**読む**: <https://alonecraft.github.io/Document/>

| フォルダ | 文書 | 公開の URL |
|---|---|---|
| `Omni/` | Omni 入門リファレンス（Unity で巨大な世界を描く仕組みと、そのデモの部品の解説） | <https://alonecraft.github.io/Document/Omni/> |

## 手元で見る

```bash
python -m pip install -r requirements.txt
python -m mkdocs serve -f Omni/mkdocs.yml
```

`main` に送ると、GitHub Actions が組み立てて GitHub Pages へ公開します。

## Omni の API リファレンスを作り直す

`Omni/docs/api/` は、Omni の本体（`Assets/Omni/Core`、検証用の `Core/Verification` を除く）の public な型から自動で作ったものです。
Unity の DLL が要るので CI では作らず、手元で作ってコミットします。

1. Omni を Unity で一度開き、`*.csproj` を作らせる。
2. DocFX を入れる：`dotnet tool install -g docfx`
3. 次を実行する（Omni の場所は自分の環境に合わせる）。

```bash
python -I tools/generate_omni_api.py G:/Unity/6.6/Omni
```

`Omni/docs/api/` は毎回まるごと作り直します。手で直さないでください（直すなら Omni のソースのコメントを直します）。

## 使い方のページの画像と動画

`Omni/docs/assets/images/lighting/` と `Omni/docs/assets/videos/lighting/` は、Omni の
`Assets/Omni/Development/Verification/Editor/LightingDocumentationCapture.cs` で撮ったものです。

- 動画：`LightingVerificationSceneBuilder.CaptureDocumentationVideosBatch`（バッチの Editor で実行。`-docOut <絶対パス>`）
- Inspector の画像：`LightingVerificationSceneBuilder.CaptureDocumentationInspectorAndExit`（画面付きの Editor で実行。窓が前に出る）
トップの一覧は `index.html` です。文書を足したら、ここと `.github/workflows/pages.yml` にも足します。
