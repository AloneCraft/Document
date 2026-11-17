# <a id="Omni_RadialTerrainBackendState"></a> Enum RadialTerrainBackendState

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

Radial描画用Terrainパッチbackendのライフサイクル状態です。
TerrainDataは常に正本であり、この状態は非保存の描画派生物だけを表します。

```csharp
public enum RadialTerrainBackendState
```

## フィールド（Fields）

`Disabled = 0` 

Terrainは登録されていません。



`Faulted = 5` 

backend構築に失敗し、Native Terrainを復元した状態です。



`Initializing = 1` 

非保存パッチを組み立てています。



`NativeFallback = 4` 

Native Terrainを表示する安全側の代替状態です。



`Ready = 2` 

全patchが有効で、Native Terrain surfaceを停止しています。



`Rebuilding = 3` 

Heightmapまたは穴の更新に伴い一部patchを再構築しています。
