# <a id="Omni_Bake_RadialBakeSpatialQueryContext"></a> Struct RadialBakeSpatialQueryContext

Namespace: [Omni.Bake](Omni.Bake.md)  
Assembly: Radial.Runtime.dll  

refresh境界で完全検証したBake BVHへの非保存参照です。Camera hot pathでは
Binding revisionと配列参照だけを検査し、fingerprint再計算や検証用配列を生成しません。

```csharp
public readonly struct RadialBakeSpatialQueryContext
```

## プロパティ（Properties）

### <a id="Omni_Bake_RadialBakeSpatialQueryContext_Binding"></a> Binding

検証済みRenderer対応表です。

```csharp
public RadialBakeBinding Binding { get; }
```

#### 値（Property Value）

 [RadialBakeBinding](Omni.Bake.RadialBakeBinding.md)

### <a id="Omni_Bake_RadialBakeSpatialQueryContext_Data"></a> Data

検証済みEntryとBVHを所有するBake assetです。

```csharp
public BakeData Data { get; }
```

#### 値（Property Value）

 [BakeData](Omni.Rendering.Radial.BakeData.md)

### <a id="Omni_Bake_RadialBakeSpatialQueryContext_IsCurrent"></a> IsCurrent

現在のBindingとBake配列が完全検証時と同じ参照ならtrueです。

```csharp
public bool IsCurrent { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
