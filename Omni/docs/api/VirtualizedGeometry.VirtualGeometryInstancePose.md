# <a id="VirtualizedGeometry_VirtualGeometryInstancePose"></a> Struct VirtualGeometryInstancePose

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

差し込み口(<xref href="VirtualizedGeometry.IVirtualGeometryInstancePlacement" data-throw-if-not-resolved="false"></xref>)が返す、1 つの camera での姿勢。

```csharp
public readonly struct VirtualGeometryInstancePose
```

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryInstancePose__ctor_UnityEngine_Matrix4x4_UnityEngine_Matrix4x4_VirtualizedGeometry_VirtualGeometryCullSpace_"></a> VirtualGeometryInstancePose\(Matrix4x4, Matrix4x4, VirtualGeometryCullSpace\)

```csharp
public VirtualGeometryInstancePose(Matrix4x4 objectToWorld, Matrix4x4 objectToCull, VirtualGeometryCullSpace cullSpace)
```

#### 引数（Parameters）

`objectToWorld` Matrix4x4

`objectToCull` Matrix4x4

`cullSpace` [VirtualGeometryCullSpace](VirtualizedGeometry.VirtualGeometryCullSpace.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryInstancePose_CullSpace"></a> CullSpace

cull を行う空間(camera の位置、視錐台、near、HZB を使ってよいか)。

```csharp
public readonly VirtualGeometryCullSpace CullSpace
```

#### 値（Field Value）

 [VirtualGeometryCullSpace](VirtualizedGeometry.VirtualGeometryCullSpace.md)

### <a id="VirtualizedGeometry_VirtualGeometryInstancePose_ObjectToCull"></a> ObjectToCull

物体の局所から cull 空間への行列(LOD の画面上の誤差、視錐台と HZB の判定に使う)。

```csharp
public readonly Matrix4x4 ObjectToCull
```

#### 値（Field Value）

 Matrix4x4

### <a id="VirtualizedGeometry_VirtualGeometryInstancePose_ObjectToWorld"></a> ObjectToWorld

描画の行列(unity_ObjectToWorld。照明などに使う)。

```csharp
public readonly Matrix4x4 ObjectToWorld
```

#### 値（Field Value）

 Matrix4x4
