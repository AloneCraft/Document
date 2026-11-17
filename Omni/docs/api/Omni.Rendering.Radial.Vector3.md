# <a id="Omni_Rendering_Radial_Vector3"></a> Struct Vector3

Namespace: [Omni.Rendering.Radial](Omni.Rendering.Radial.md)  
Assembly: Radial.Runtime.dll  

Logical差分ベクトルをUnityシリアライザで保持するためのラッパーです。

```csharp
[Serializable]
public struct Vector3
```

## プロパティ（Properties）

### <a id="Omni_Rendering_Radial_Vector3_HasValue"></a> HasValue

```csharp
public bool HasValue { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Rendering_Radial_Vector3_From_Omni_Logical_Vector3__"></a> From\(in Vector3\)

```csharp
public static Vector3 From(in Vector3 value)
```

#### 引数（Parameters）

`value` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [Vector3](Omni.Rendering.Radial.Vector3.md)

### <a id="Omni_Rendering_Radial_Vector3_TryGetValue_Omni_Logical_Vector3__"></a> TryGetValue\(out Vector3\)

```csharp
public bool TryGetValue(out Vector3 value)
```

#### 引数（Parameters）

`value` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
