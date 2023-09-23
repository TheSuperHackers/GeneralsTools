set Model=Photo-Conservative-x4
set ThisDir=%~dp0.
set OutputDir=%ThisDir%\\export\\%Model%

if not exist "%OutputDir%" (
  mkdir "%OutputDir%"
)
realesrgan-ncnn-vulkan.exe -i "%ThisDir%\\import" -o "%OutputDir%" -n %Model% -s 4 -f png
