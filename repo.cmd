:: Copyright (C) 2020 Timothy Lin. timothy.gh.lin@gmail.com
:: 
:: Licensed under the Apache License, Version 2.0 (the "License");
:: you may not use this file except in compliance with the License.
:: You may obtain a copy of the License at
:: 
::      http://www.apache.org/licenses/LICENSE-2.0
:: 
:: Unless required by applicable law or agreed to in writing, software
:: distributed under the License is distributed on an "AS IS" BASIS,
:: WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
:: See the License for the specific language governing permissions and
:: limitations under the License.

::@%windir%\system32\net.exe session 1>NUL 2>NUL || (Echo Error: Repo requires elevated admin rights. Run Repo in the admin command prompt. & EXIT /b 1)
py -3 %~dp0\repo_win32.py %~dp0\repo %*
