# <a id="Omni_Rendering_Radial_Aabb"></a> Struct Aabb

Namespace: [Omni.Rendering.Radial](Omni.Rendering.Radial.md)  
Assembly: Radial.Runtime.dll  

Logical AABBをUnityシリアライザで保持するためのラッパーです。

```csharp
[Serializable]
public struct Aabb
```

## プロパティ（Properties）

### <a id="Omni_Rendering_Radial_Aabb_HasValue"></a> HasValue

```csharp
public bool HasValue { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Rendering_Radial_Aabb_From_Omni_Logical_Aabb__"></a> From\(in Aabb\)

```csharp
public static Aabb From(in Aabb value)
```

#### 引数（Parameters）

`value` [Aabb](Omni.Logical.Aabb.md)

#### 戻り値（Returns）

 [Aabb](Omni.Rendering.Radial.Aabb.md)

### <a id="Omni_Rendering_Radial_Aabb_TryGetValue_Omni_Logical_Aabb__"></a> TryGetValue\(out Aabb\)

```csharp
public bool TryGetValue(out Aabb value)
```

#### 引数（Parameters）

`value` [Aabb](Omni.Logical.Aabb.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
