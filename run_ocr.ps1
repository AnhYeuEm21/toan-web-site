Add-Type -AssemblyName System.Runtime.WindowsRuntime
$asTaskGeneric = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'
}[0]

function Await($asyncOp, $type) {
    $asTask = $asTaskGeneric.MakeGenericMethod($type)
    $netTask = $asTask.Invoke($null, @($asyncOp))
    $netTask.Wait(-1) | Out-Null
    return $netTask.Result
}

[Windows.Media.Ocr.OcrEngine, Windows.Foundation.Diagnostics, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime] | Out-Null

function Get-OcrText([string]$path) {
    try {
        $fileOp = [Windows.Storage.StorageFile]::GetFileFromPathAsync($path)
        $file = Await $fileOp ([Windows.Storage.StorageFile])

        $streamOp = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read)
        $stream = Await $streamOp ([Windows.Storage.Streams.IRandomAccessStream])

        $decOp = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)
        $decoder = Await $decOp ([Windows.Graphics.Imaging.BitmapDecoder])

        $bmpOp = $decoder.GetSoftwareBitmapAsync()
        $bitmap = Await $bmpOp ([Windows.Graphics.Imaging.SoftwareBitmap])

        $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
        if (-not $engine) {
            $lang = [Windows.Globalization.Language]::new("en-US")
            $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($lang)
        }
        $ocrOp = $engine.RecognizeAsync($bitmap)
        $ocrResult = Await $ocrOp ([Windows.Media.Ocr.OcrResult])
        return $ocrResult.Text
    }
    catch {
        return "ERROR: $_"
    }
}

$outputFile = "C:\Users\Admin\Desktop\toan\ocr_summary.txt"
"=== OCR SUMMARY ===" | Out-File -FilePath $outputFile -Encoding utf8

for ($i = 1; $i -le 21; $i++) {
    $fn = ("C:\Users\Admin\Desktop\toan\page_{0:D2}.png" -f $i)
    if (Test-Path $fn) {
        $text = Get-OcrText $fn
        $lines = ($text -split "`r?`n") | Where-Object { $_.Trim().Length -gt 0 }
        $firstLines = ($lines | Select-Object -First 4) -join " || "
        ("PAGE {0:D2}: {1}" -f $i, $firstLines) | Out-File -FilePath $outputFile -Append -Encoding utf8
    }
}

for ($i = 1; $i -le 13; $i++) {
    $fn = ("C:\Users\Admin\Desktop\toan\hinh_{0:D2}.png" -f $i)
    if (Test-Path $fn) {
        $text = Get-OcrText $fn
        $lines = ($text -split "`r?`n") | Where-Object { $_.Trim().Length -gt 0 }
        $firstLines = ($lines | Select-Object -First 4) -join " || "
        ("HINH {0:D2}: {1}" -f $i, $firstLines) | Out-File -FilePath $outputFile -Append -Encoding utf8
    }
}

Write-Host "OCR Summary done successfully!"
