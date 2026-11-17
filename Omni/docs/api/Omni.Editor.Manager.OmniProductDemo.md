# <a id="Omni_Editor_Manager_OmniProductDemo"></a> Class OmniProductDemo

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

製品デモ(Build Settingsの先頭に置くScene)です。2026-09-25のユーザー判断で、受入(P11 WebGPU、P12 DX12)を通った
Earth to Moon 2へ切り替え、2026-09-30に旧Earth to Moonを削除して、EarthToMoonの名前へ改めました。

```csharp
public static class OmniProductDemo
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniProductDemo](Omni.Editor.Manager.OmniProductDemo.md)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_OmniProductDemo_CosmicEventsScenePath"></a> CosmicEventsScenePath

宇宙で起きる突発的な現象（パルサー、ブラックホールや中性子星の合体、フレア、超新星、ジェット、銀河の衝突など）を、時間スケールの短い順に連続で見せるSceneです。
2026-10-05のユーザー判断でCosmicScaleデモの3つ目のSceneとして同梱し、Build Settingsには登録しません。Docs/Plans/CosmicEventsDesign.mdを参照してください。

```csharp
public static string CosmicEventsScenePath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniProductDemo_CosmicHierarchyScenePath"></a> CosmicHierarchyScenePath

月 → 地球 → 太陽 → 天の川銀河 → 局所銀河群 → 超銀河団 → フィラメント → 観測可能な宇宙の入れ子を、実際の配置の3D空間で見せるSceneです。
2026-10-03のユーザー判断でCosmicScaleデモの2つ目のSceneとして同梱し、Build Settingsには登録しません。Docs/Plans/CosmicHierarchyDesign.mdを参照してください。

```csharp
public static string CosmicHierarchyScenePath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniProductDemo_CosmicScaleScenePath"></a> CosmicScaleScenePath

サッカーボールから観測可能な宇宙まで、カメラが後退し続けて天体の大きさの違いを見せるSceneです。2026-10-02のユーザー判断で独立した製品デモとして同梱し、
Build Settingsには登録しません。Docs/Plans/CosmicScaleDesign.mdを参照してください。

```csharp
public static string CosmicScaleScenePath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniProductDemo_MoonScenePath"></a> MoonScenePath

月のデータ(高さ)をネットワークからストリーミングして、全球から地面まで詳細化しながら周回するSceneです。Build Settingsには登録しません。
ストリーミングのランタイムは Assets/Omni/Core/Streaming、仕様は Docs/Plans/StreamingRuntime.md と Docs/Plans/MoonDesign.md を参照してください。

```csharp
public static string MoonScenePath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniProductDemo_ScenePath"></a> ScenePath

製品デモのSceneです。

```csharp
public static string ScenePath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniProductDemo_SolarSystemScenePath"></a> SolarSystemScenePath

並存する太陽系の軌道シミュレーション(実寸、JPL暦、NASA画像)のSceneです。2026-09-26のユーザー判断で製品デモとして同梱し、
Build Settingsには登録しません(先頭はEarthToMoonのまま)。Docs/Plans/SolarSystemDesign.mdを参照してください。

```csharp
public static string SolarSystemScenePath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
