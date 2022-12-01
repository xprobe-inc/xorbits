# Copyright 2022 XProbe Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .mars_adapters import spawn

# def __dir__():
#     from .mars_adapters import MARS_REMOTE_CALLABLES
#
#     return list(MARS_REMOTE_CALLABLES.keys())


# def __getattr__(name):
#     from .mars_adapters import MARS_REMOTE_CALLABLES
#
#     if name in MARS_REMOTE_CALLABLES:
#         return MARS_REMOTE_CALLABLES[name]
#     else:
#         raise AttributeError(name)