python -m nuitka __main__.py  ^
--windows-icon-from-ico=icon.ico ^
--windows-company-name=NTO ^
--windows-product-name=Recipy_Modify ^
--windows-file-version=1.0 ^
--windows-product-version=1.0 ^
--windows-file-description="Script for ICP200E recipe modifying" ^
--remove-output ^
--onefile

ren "__main__.exe" "Recipy_Modify.exe"

pause