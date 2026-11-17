# <a id="Omni_Converter_RadialMaterialApplier"></a> Class RadialMaterialApplier

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

シーン内の永続Materialを事前解析し、参照を維持したままShaderをOmni版へ切り替える、
または永続台帳から元へ戻すEditorツールです。旧生成Materialを参照するSceneの復元も
互換経路として維持します。

```csharp
public static class RadialMaterialApplier
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialMaterialApplier](Omni.Converter.RadialMaterialApplier.md)

## メソッド（Methods）

### <a id="Omni_Converter_RadialMaterialApplier_ApplyToScene"></a> ApplyToScene\(\)

現在アクティブなシーンの全 Renderer と Terrain のマテリアルを
Omni 変換版に差し替えます。

```csharp
public static (int renderers, int terrains) ApplyToScene()
```

#### 戻り値（Returns）

 \([int](https://learn.microsoft.com/dotnet/api/system.int32) [renderers](https://learn.microsoft.com/dotnet/api/system.valuetuple\-system.int32,system.int32\-.renderers), [int](https://learn.microsoft.com/dotnet/api/system.int32) [terrains](https://learn.microsoft.com/dotnet/api/system.valuetuple\-system.int32,system.int32\-.terrains)\)

差し替えた Renderer 数と Terrain 数。

### <a id="Omni_Converter_RadialMaterialApplier_EnsureRadialCameraOnMain"></a> EnsureRadialCameraOnMain\(\)

アクティブシーンの MainCamera に <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> が
付いていることを確認し、なければ追加します。

```csharp
public static RadialCamera EnsureRadialCameraOnMain()
```

#### 戻り値（Returns）

 RadialCamera

### <a id="Omni_Converter_RadialMaterialApplier_ForceRevert"></a> ForceRevert\(\)

キャッシュを使わず、シーン内の Omni マテリアルを元に戻します。
Unity 再コンパイルでキャッシュが消えた後の復元用です。

```csharp
public static (int renderers, int terrains) ForceRevert()
```

#### 戻り値（Returns）

 \([int](https://learn.microsoft.com/dotnet/api/system.int32) [renderers](https://learn.microsoft.com/dotnet/api/system.valuetuple\-system.int32,system.int32\-.renderers), [int](https://learn.microsoft.com/dotnet/api/system.int32) [terrains](https://learn.microsoft.com/dotnet/api/system.valuetuple\-system.int32,system.int32\-.terrains)\)

### <a id="Omni_Converter_RadialMaterialApplier_Validate"></a> Validate\(\)

シーン内の全 Renderer/Terrain のマテリアルを検査し、
差し替え可能かどうかのレポートを返します。

```csharp
public static string Validate()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
