# <a id="Omni_Logical_ActiveCameraResolver"></a> Class ActiveCameraResolver

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Editor.dll  

```csharp
[MovedFrom(true, "Omni.Editor.SceneViewRadial", null, "LogicalActiveCameraResolver")]
public static class ActiveCameraResolver
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ActiveCameraResolver](Omni.Logical.ActiveCameraResolver.md)

## メソッド（Methods）

### <a id="Omni_Logical_ActiveCameraResolver_GetRankedCandidates_System_Collections_Generic_List_UnityEngine_Camera__"></a> GetRankedCandidates\(List<Camera\>\)

候補カメラをdepth降順で<code class="paramref">results</code>へ書き出します。

```csharp
public static void GetRankedCandidates(List<Camera> results)
```

#### 引数（Parameters）

`results` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Camera\>

### <a id="Omni_Logical_ActiveCameraResolver_IsCandidate_UnityEngine_Camera_"></a> IsCandidate\(Camera\)

候補カメラかどうかを返します（有効なカメラかつ有効なRadialCameraを持つ）。

```csharp
public static bool IsCandidate(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_ActiveCameraResolver_Resolve"></a> Resolve\(\)

優先順位1番のカメラを返します。候補が無ければnull。

```csharp
public static Camera Resolve()
```

#### 戻り値（Returns）

 Camera
