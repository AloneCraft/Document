# <a id="Omni_Editor_BatchRendering_RadialSceneResidentCacheDiagnostics"></a> Class RadialSceneResidentCacheDiagnostics

Namespace: [Omni.Editor.BatchRendering](Omni.Editor.BatchRendering.md)  
Assembly: Omni.Editor.dll  

外部Editor自動化からResident cacheだけをA/B計測するための狭い診断入口です。
Runtimeの内部cache型や公開APIは露出しません。

```csharp
public static class RadialSceneResidentCacheDiagnostics
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialSceneResidentCacheDiagnostics](Omni.Editor.BatchRendering.RadialSceneResidentCacheDiagnostics.md)

## メソッド（Methods）

### <a id="Omni_Editor_BatchRendering_RadialSceneResidentCacheDiagnostics_ReportPreciseBasisResidentState"></a> ReportPreciseBasisResidentState\(\)

Precise Basis Resident Cacheの有効状態と現在の統計を返します。

```csharp
public static string ReportPreciseBasisResidentState()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_BatchRendering_RadialSceneResidentCacheDiagnostics_SetPreciseBasisResidentState_System_Boolean_"></a> SetPreciseBasisResidentState\(bool\)

自動化によるA/B計測用にPrecise Basis Resident Cacheを切り替え、変更後の状態を返します。

```csharp
public static string SetPreciseBasisResidentState(bool enabled)
```

#### 引数（Parameters）

`enabled` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

cacheを有効にする場合はtrue、比較のため無効にする場合はfalse。

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
