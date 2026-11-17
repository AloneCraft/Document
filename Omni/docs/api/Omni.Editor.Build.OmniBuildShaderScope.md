# <a id="Omni_Editor_Build_OmniBuildShaderScope"></a> Class OmniBuildShaderScope

Namespace: [Omni.Editor.Build](Omni.Editor.Build.md)  
Assembly: Omni.Editor.dll  

開発用の Player ビルド（回帰、EarthToMoon、SolarSystem）の間だけ、Scene とパイプラインが使わない Shader の
variant を外します。残す Shader の計算は <xref href="Omni.Editor.Build.OmniBuildShaderClosure" data-throw-if-not-resolved="false"></xref> が行い、この型は
<code>IPreprocessShaders</code>（<xref href="Omni.Editor.Build.OmniBuildShaderStripper" data-throw-if-not-resolved="false"></xref>）を有効にして、外した数を記録するだけです。
製品の Player ビルドには適用しません（利用者のコードが実行時に探す Shader を落とす危険があるため）。

```csharp
public sealed class OmniBuildShaderScope : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniBuildShaderScope](Omni.Editor.Build.OmniBuildShaderScope.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## プロパティ（Properties）

### <a id="Omni_Editor_Build_OmniBuildShaderScope_Active"></a> Active

今有効な範囲（無ければ null）。開発用の実測（census）が、Shader ごとの判定と理由を読むのに使う。

```csharp
public static OmniBuildShaderScope Active { get; }
```

#### 値（Property Value）

 [OmniBuildShaderScope](Omni.Editor.Build.OmniBuildShaderScope.md)

### <a id="Omni_Editor_Build_OmniBuildShaderScope_Closure"></a> Closure

このビルドで残す Shader の集合。

```csharp
public OmniBuildShaderClosure Closure { get; }
```

#### 値（Property Value）

 [OmniBuildShaderClosure](Omni.Editor.Build.OmniBuildShaderClosure.md)

## メソッド（Methods）

### <a id="Omni_Editor_Build_OmniBuildShaderScope_Begin_Omni_Editor_Build_OmniBuildShaderRequest_"></a> Begin\(OmniBuildShaderRequest\)

有効な範囲。ビルドが終わるか失敗したら <code>Dispose</code> で解除する（<code>using</code> で使う）。

```csharp
public static OmniBuildShaderScope Begin(OmniBuildShaderRequest request)
```

#### 引数（Parameters）

`request` [OmniBuildShaderRequest](Omni.Editor.Build.OmniBuildShaderRequest.md)

#### 戻り値（Returns）

 [OmniBuildShaderScope](Omni.Editor.Build.OmniBuildShaderScope.md)

### <a id="Omni_Editor_Build_OmniBuildShaderScope_Dispose"></a> Dispose\(\)

解除して、外した Shader と件数をログに出す。

```csharp
public void Dispose()
```
