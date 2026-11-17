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
トップの一覧は `index.html` です。文書を足したら、ここと `.github/workflows/pages.yml` にも足します。
