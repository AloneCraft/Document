# <a id="Omni_ExternalDrawPaths"></a> Class ExternalDrawPaths

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

GPU駆動の独自drawなど、Omniが収集するRenderer・Terrain・BRGの外にある描画経路の公開入口です。
外部経路は独自のcamera packet writerを持たず、ここへ要件を登録します。

```csharp
public static class ExternalDrawPaths
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ExternalDrawPaths](Omni.ExternalDrawPaths.md)

## 補足（Remarks）

<p>
providerはCameraごとにメインスレッドで呼ばれます。軽く、例外を出さない実装にしてください。
例外を出したproviderはログを出して自己解除されます。
</p>
<p>
登録はBRG専用のcamera-relative instance dataを要求しません。外部経路のprecise物体は、
<xref href="Omni.RadialGlobalRenderSystem.WriteRadialTransformParameters(UnityEngine.MaterialPropertyBlock%2cOmni.Rendering.Radial.DrawTransform%40)" data-throw-if-not-resolved="false"></xref>と
<xref href="Omni.RadialGlobalRenderSystem.WriteGpuFrameParameters(UnityEngine.MaterialPropertyBlock%2cOmni.Rendering.Radial.GpuFrame%40)" data-throw-if-not-resolved="false"></xref>で物体ごとの値を受け取ります。
</p>

## メソッド（Methods）

### <a id="Omni_ExternalDrawPaths_Register_System_Func_Omni_ExternalDrawRequirements__"></a> Register\(Func<ExternalDrawRequirements\>\)

外部描画経路の要件providerを登録します。戻り値をDisposeすると登録を解除します（複数回のDisposeは無視）。

```csharp
public static IDisposable Register(Func<ExternalDrawRequirements> provider)
```

#### 引数（Parameters）

`provider` [Func](https://learn.microsoft.com/dotnet/api/system.func\-1)<[ExternalDrawRequirements](Omni.ExternalDrawRequirements.md)\>

現在の要件を返す関数。

#### 戻り値（Returns）

 [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

#### 例外（Exceptions）

 [ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)

<code class="paramref">provider</code>がnullのとき。
