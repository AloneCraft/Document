# <a id="Omni_Converter_OmniRadialOutputMigration"></a> Class OmniRadialOutputMigration

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

旧配置 <code>Assets/Radial/User/&lt;パッケージ名&gt;/…</code> の Shader・Shader Graph（とその <code>*_Materials</code>）を、
現在の規則 <code>Assets/Radial/Packages/&lt;パッケージ名&gt;/…</code>（<xref href="Omni.Converter.RadialMaterialConverter.GetOmniOutputPath(System.String)" data-throw-if-not-resolved="false"></xref>）へ
<b>移動</b>します。

```csharp
public static class OmniRadialOutputMigration
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniRadialOutputMigration](Omni.Converter.OmniRadialOutputMigration.md)

## 補足（Remarks）

再生成ではなく移動にするのは、GUID を保つためです。再生成すると、旧ファイルの .meta と GUID 台帳の記録が同じ GUID を
持ったまま二重になり、Material や Scene の参照も壊れます。移動した分は <xref href="Omni.Converter.OmniGuidManifest.RenameEntry(System.String%2cSystem.String)" data-throw-if-not-resolved="false"></xref> で
台帳の記録も付け替えます。
旧配置かどうかは「User 直下のフォルダ名が <code>Packages/</code> にあるパッケージ名で、同名の <code>Assets/</code> フォルダが無い」で決めます。

## メソッド（Methods）

### <a id="Omni_Converter_OmniRadialOutputMigration_EnsureMigrated"></a> EnsureMigrated\(\)

切替・ビルド準備の入口から呼びます。ドメインごとに 1 回だけ旧配置を調べ、あれば <xref href="Omni.Converter.OmniRadialOutputMigration.Migrate" data-throw-if-not-resolved="false"></xref> します。
結果を 1 行のログに残します（移す物が無いときは何も出しません）。

```csharp
public static void EnsureMigrated()
```

### <a id="Omni_Converter_OmniRadialOutputMigration_IsMigrationNeeded"></a> IsMigrationNeeded\(\)

旧配置の資産が残っているか（移行が必要か）を返します。

```csharp
public static bool IsMigrationNeeded()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniRadialOutputMigration_Migrate"></a> Migrate\(\)

旧配置の資産を新配置へ移動し、台帳を付け替えます。移す物がなければ何もしません。

```csharp
public static OmniRadialOutputMigration.Result Migrate()
```

#### 戻り値（Returns）

 [OmniRadialOutputMigration](Omni.Converter.OmniRadialOutputMigration.md).[Result](Omni.Converter.OmniRadialOutputMigration.Result.md)
