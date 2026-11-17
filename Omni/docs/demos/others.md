# ほかのデモ

ここでは、製品と一緒に配る**公開デモ**を短く紹介します。
公開デモは `Assets/Omni/Demos/` にあり、本体とは別のパッケージで配ります。

!!! tip "開いて何も映らないとき"
    デモは「ふつうの描画」の状態で配られます。
    Scene View の Omni の Overlay から Omni Manager を開き、上部の「対数レンダリング」を選んでください。

## EarthToMoon（地球から月へ）

| | |
|---|---|
| 場所 | `Assets/Omni/Demos/EarthToMoon/` |
| 見せるもの | 地球から月への移動。巨大な座標、天体の間の移動、月面の細部 |
| 使っている Omni の機能 | Logical、Radial、VirtualGeometry（地球と月の地形） |

地球と月の地形は、どちらも VG で描いています。
月の全体の標高は Moon デモのデータを共有しています。
Asteria の大気の部品は、このデモの大気のコードを複製したものです。

## SolarSystem（太陽系）

| | |
|---|---|
| 場所 | `Assets/Omni/Demos/SolarSystem/` |
| 見せるもの | 太陽、8 つの惑星、月や衛星など 32 の天体を、本当の大きさ・本当の距離・本当の時刻（1900〜2050 年）で見て回る |
| 特徴 | 土星の環は、近くは VG の氷の岩、中くらいは粒、遠くは透ける板、の段で描き分ける |

## CosmicScale（宇宙の大きさ）

| Scene | 見せるもの |
|---|---|
| `CosmicScale` | 陽子から観測できる宇宙まで、45 段の大きさの比べ |
| `CosmicHierarchy` | 入れ子になった宇宙の階層（惑星 → 恒星系 → 銀河 …） |
| `CosmicEvents` | 宇宙で起きる出来事 |

Omni の「42 桁の違いを 1 つの Scene に置く」を、いちばん分かりやすく見せるデモです。

## Moon（月）

| | |
|---|---|
| 場所 | `Assets/Omni/Demos/Moon/` |
| 見せるもの | 月のデータのストリーミング（必要な所だけ読み込む） |
| 特徴 | 月の基礎データの出典と配置は `ExternalData/Moon/base-data.manifest.json` に書かれている |

## Quick Start（はじめの一歩）

| | |
|---|---|
| 場所 | `Assets/Omni/Development/Distribution/PackageSamples/QuickStart/`（配るときは Samples のパッケージに入る） |
| 見せるもの | ふつうの描画と Radial を比べる、入門用の例 |

!!! note "もう無いデモ"
    以前あった Galaxy デモは 2026-10-13 に削除されました。開発用の手順やコマンドの一部に名前が残っています。
