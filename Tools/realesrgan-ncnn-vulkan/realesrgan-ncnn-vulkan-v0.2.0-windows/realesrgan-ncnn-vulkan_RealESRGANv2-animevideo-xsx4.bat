set Model=RealESRGANv2-animevideo-xsx4
set ThisDir=%~dp0.
set OutputDir=%ThisDir%\\export\\%Model%

if not exist "%OutputDir%" (
  mkdir "%OutputDir%"
)
realesrgan-ncnn-vulkan.exe -i "%ThisDir%\\import" -o "%OutputDir%" -n %Model% -s 4 -f png