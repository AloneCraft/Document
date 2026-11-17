# <a id="Omni_RadialVfxRendererRegistry"></a> Class RadialVfxRendererRegistry

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

VFXRendererの所属だけをtarget refresh時に記録し、Camera/Repaint hot pathで
Scene走査を行わず最新native BoundsをRadial world Boundsへ変換します。
Boundsの所有・復元自体は共通RadialRendererBoundsRegistryへ委譲します。

```csharp
public static class RadialVfxRendererRegistry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialVfxRendererRegistry](Omni.RadialVfxRendererRegistry.md)

## メソッド（Methods）

### <a id="Omni_RadialVfxRendererRegistry_GetDiagnostics"></a> GetDiagnostics\(\)

```csharp
public static RadialVfxRendererRegistry.Diagnostics GetDiagnostics()
```

#### 戻り値（Returns）

 [RadialVfxRendererRegistry](Omni.RadialVfxRendererRegistry.md).[Diagnostics](Omni.RadialVfxRendererRegistry.Diagnostics.md)
